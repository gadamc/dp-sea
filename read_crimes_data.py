
sqlContext = SQLContext(sc)

#typically hostname == username.cloudant.com
hostname = "gadamc-datapalooza.cloudant.com"
username = "newalmossystipsesperedel"  #API key-password pair generated by Cloudant
password = "77498c6d7a5b4455f29640e06814d1467319cb75"

databaseName = "crimes"
# in the future will be able to pull not just from database, but from a map-reduce view result!
# this is available in a Scala notebook now. 

cloudantdata = sqlContext.read.format("com.cloudant.spark").option("cloudant.host",hostname).option("cloudant.username", username).option("cloudant.password",password).load(databaseName)

cloudantdata = cloudantdata.cache() #important, or will pull data from cloudant on each 'action'
cloudantdata.printSchema()

print cloudantdata.count()

cloudantdata.filter("properties.naturecode = 'BE'").take(2)
