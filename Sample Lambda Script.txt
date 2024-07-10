import sys
import json
import boto3
import snowflake.connector
import configparser
	
def load_table(cur, table_name, file_name):
	#Open sql file and read query
	f = open('load_'+table_name+'.sql', 'r')
	sql_command = f.read()
	f.close()
	#Executing the COPY INTO query to load data from S3 stage to snowflake table
	try:
		cur.execute(sql_command+" FILES=('"+file_name+"');")
		return 0
	except:
		return 1

def delete_table(cur, table_name, file_name):
	#Open sql file and read query
	f1 = open('delete_'+table_name+'.sql', 'r')
	sql_command = f1.read()
	f1.close()
	#Executing the merge query to load data from stage to final snowflake table
	try:
		cur.execute(sql_command+" ;")
		return 0
	except:
		return 1
		
def merge_table(cur, table_name, file_name):
	#Open sql file and read query
	f1 = open('merge_'+table_name+'.sql', 'r')
	sql_command = f1.read()
	f1.close()
	#Executing the merge query to load data from stage to final snowflake table
	try:
		cur.execute(sql_command+" ;")
		return 0
	except:
		return 1
		
def truncate_table(cur, table_name, file_name):
	#Open sql file and read query
	f2 = open('truncate_'+table_name+'.sql', 'r')
	sql_command = f2.read()
	f2.close()
	#Executing the truncate query to delete data from  stage table
	try:
		cur.execute(sql_command+" ;")
		return 0
	except:
		return 1

def insert_table(cur, table_name,file_name):
	#Open sql file and read query
	f1 = open('insert_'+table_name+'.sql', 'r')
	sql_command = f1.read()
	f1.close()
	#Executing the merge query to load data from stage to final snowflake table
	try:
		cur.execute(sql_command+" ;")
		return 0
	except:
		return 1
				
		
		
		
def validate_load(cur, table_name, query_id):
	#Validating the query for any errors
	cur.execute("select * from table(validate("+table_name+", job_id=>'"+query_id+"'))")


#Lambda Handler
def lambda_handler(event, context):
    
	#Creating S3 client
	s3 = boto3.client('s3')
	print(event)
	#Getting the bucket and file details
	s3_bucket = event['Records'][0]['s3']['bucket']['name']
	obj_key = event['Records'][0]['s3']['object']['key']
	
	print("INFO Creating connection to snowflake")
	#Creating connection to snowflake account
	config = configparser.ConfigParser()
	config.read('sf_prd_config.ini')
	
	ctx = snowflake.connector.connect(
		user=config['sfAccPrd']['usr'],
		password=config['sfAccPrd']['pass'],
		account=config['sfAccPrd']['acc']
		)
	cur = ctx.cursor()
	
	#Extracting the table name and file name
	table = obj_key.split('/')[0]
	file = obj_key.split('/')[1]
	
	
	print("INFO Setting default database and schema")
	try:
		#Setting default warehouse, database and schema
		cur.execute("USE warehouse LOADING_PRD_FRANCHISE_WH")
		cur.execute("USE PRD_FRANCHISE.BATCH")
	except:
		print("ERROR Failed to set default database and schema")
		sys.exit()

		#Deleting table
	print("INFO Truncate file " + file + " to snowflake table " + table)
	load_status = truncate_table(cur, table, file)
	if load_status != 0:
		print("Failed to truncate file " + file + " to snowflake table " + table)
		sys.exit()
		
	#Loading table
	print("INFO Loading file " + file + " to snowflake table " + table)
	load_status = load_table(cur, table, file)
	if load_status != 0:
		print("Failed to load file " + file + " to snowflake table " + table)
		sys.exit()
		

		
	#Insert history table
	print("INFO Insert file " + obj_key + " to snowflake table " )
	load_status = insert_table(cur, table, file)
	if load_status != 0:
		print("Failed to Insert file " + obj_key + " to snowflake table " )
		sys.exit()
		
		
	#Merging table
	print("INFO Merge file " + file + " to snowflake table " + table)
	load_status = merge_table(cur, table, file)
	if load_status != 0:
		print("Failed to merge file " + file + " to snowflake table " + table)
		sys.exit()
	
	#Fetching the query ID
	q_id = cur.sfqid
		
	print("INFO Snowflake Query ID: " + q_id)
		
	try:
		#Validating load
		print("INFO Validating load for table " + table)

	finally:
		cur.close()
		print("INFO Data load completed")
	
	ctx.close()
	
	
	#Returning some details for verification
	return {
		'statusCode': 200,
		'bucket name' : s3_bucket,
		'bucket key' : obj_key,
		'table' : table,
		'query id' : q_id,
		#'out' : val_out				 
		}
	
