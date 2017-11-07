import boto3
import pandas as pd
from StringIO import StringIO
s3 = boto3.client('s3')
bucket_name = 'hadoop-techfield-training'
file_name = 'us-500.csv'
csv_obj = s3.get_object(Bucket=bucket_name, Key=file_name)
body = csv_obj['Body']
csv_string = body.read().decode('utf-8')
df = pd.read_csv(StringIO(csv_string))
print df

#################################################
import boto3
import findspark
findspark.init()
#from pyspark import SparkContext
from StringIO import StringIO
s3 = boto3.client('s3')
bucket_name = 'hadoop-techfield-training'
file_name = 'us-500.csv'
csv_obj = s3.get_object(Bucket=bucket_name, Key=file_name)
body = csv_obj['Body']
csv_string = body.read().decode('utf-8')


from pyspark import SparkContext
from pyspark.sql import SQLContext
import pandas as pd

sc = SparkContext('local','example')  # if using locally
sql_sc = SQLContext(sc)
df = pd.read_csv(StringIO(csv_string))
# assuming the file contains a header
# pandas_df = pd.read_csv('file.csv', names = ['column 1','column 2']) # if no header
s_df = sql_sc.createDataFrame(df)
print s_df
sc.stop()