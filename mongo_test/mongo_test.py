import pymongo
import random

client = pymongo.MongoClient("mongodb://localhost:27017")
print('连接数据库成功',  client)

mongodb_name = 'mongo_test'

db = client[mongodb_name]

u = {
	'name': 'xiao',
	'age' : 18,
	'随机值': random.randint(0, 3), 
}

db.user.insert(u)

user_list = list(db.user.find())
print('所有用户', user_list)

query = {
	'随机值': 1,
}

print('random 1', list(db.user.find(query)))




