val lines = sc.textFile("twitter.edges")
val followers = lines.map(line => line.split(": ")(1)).flatMap(line => line.split(",")).map(user => (user, 1))
var total_followers = followers.reduceByKey(_ + _)
var res = total_followers.filter(count => count._2 > 1000)
res.saveAsTextFile("output")
System.exit(0)