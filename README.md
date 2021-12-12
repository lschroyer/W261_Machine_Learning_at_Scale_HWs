# Repository for projects completed during the UC Berkeley Masters of Information and Data Science (MIDS) W261 course, "Machine Learning at Scale"
class website: https://www.ischool.berkeley.edu/courses/datasci/261

The course covers fundamental concepts of MapReduce parallel computing, through the eyes of Hadoop, MrJob, and Spark, while diving deep into Spark Core, data frames, the Spark Shell, Spark Streaming, Spark SQL, MLlib, and more, as well as on hands-on algorithmic design and development in parallel computing environments (Spark), developing algorithms (decision tree learning), graph processing algorithms (pagerank/shortest path), gradient descent algorithms (support vectors machines), and matrix factorization.

Projects in this repo included developing the following algorithms from scratch:
- Map Reduce in the Command Line
- Naive Bayes Implementation in Hadoop
- Synonym Detection in PySpark
- Distributed Linear Regression in PySpark
- Search engine optimization (SEO) using PageRank on Wikipedia pages in PySpark  

Then using mllib in Pyspark, I created a ML model that utilizes 2015-2019 airport and weather data (>30,000 million rows of data in HDFS) to predict airline flight delays over two hours in advance of the scheduled departure time with over 70% model accuracy.
