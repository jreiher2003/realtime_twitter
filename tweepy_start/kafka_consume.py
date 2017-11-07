
"""
RUNNING PROGRAM;
1-Start Apache Kafka
./kafka/bin/kafka-server-start.sh ./kafka/config/server.properties
2-Run kafka_push_listener.py (Start Producer)
ipython >> run kafka_push_listener.py
3-Run kafka_twitter_spark_streaming.py (Start Consumer)
PYSPARK_PYTHON=python3 ./bin/spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.2.0 ~/home/vagrant/kafka_consume.py
bin/spark-submit --jars home/ubuntu/spark-streaming-kafka-0-8:2.2.0.jars ~/home/vagrant/jason_sanchez/tw/.py
"""
# import os
# os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.0.2 pyspark-shell'
import sys
import findspark 
findspark.init()
from pyspark import SparkContext 
from pyspark.streaming import StreamingContext 
from pyspark.streaming.kafka import KafkaUtils 
import json 

if __name__ == "__main__":
    if len(sys.argv) != 3:
        # print("Usage: direct_kafka_wordcount.py <broker_list> <topic>", file=sys.stderr)
        exit(-1)

    #create spark context to connect spark cluster 
    sc = SparkContext(appName="Jeff's awesome twitter feed analysis")
    ssc = StreamingContext(sc, 2)

    # Create Kafka Stream to Consume Data Comes From Twitter Topic 
    # localhost:2181 = Defualt Zookeeper consumer address 
    brokers, topic = sys.argv[1:]
    kvs = KafkaUtils.createDirectStream(ssc, [topic], {"metadata.broker.list": brokers})
    # kafkaStream = KafkaUtils.createStream(ssc, "localhost:2181", "spark-streaming", {"twitter": 1})
    #Parse Twitter Data as json
    parsed = kvs.map(lambda v: json.loads(v[1]))

    #Count the number of words in each tweets per User
    user_counts = parsed.map(lambda tweet: (tweet['text'], 1)).reduceByKey(lambda x,y: x + y)

    #Print the User tweet counts
    user_counts.pprint()

    #Start Execution of Streams
    ssc.start()
    ssc.awaitTermination()