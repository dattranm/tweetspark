# Twitter Sentiment Analysis using Spark Streaming [Python, Apache Spark, ElasticSearch, Kibana] 

To run this, first the prerequisite is to install Apache Spark, Elasticsearch, Kibana, and Python version 3.8 +. This program is intended to be run on Linux Ubuntu.

Step 1: Type the command 
````
start-all.sh 
````
into the terminal, and follow through all the steps required in the command, including inputting the user password

Step 2: Open terminal in the appropriate Elasticsearch folder, and type in 

````
./bin/elasticsearch
````
to start the Elasticsearch daemon

Step 3: Open terminal in the location of stream.py file, and type in 
````
python3 stream.py
````
to initiate the pipeline

Step 4: Open terminal in the location of spark.py file, and type in 
````
python3 spark.py
````
to start streaming real-time Tweet

Step 5: Open terminal in the appropriate Kibana folder, and type in 
````
./bin/kibana
````
to start the Kibana daemon

Congratulations! You have the program running! The Kibana Dashboard will be hosted in your localhost, through the address 
````
http://localhost:5601
````
