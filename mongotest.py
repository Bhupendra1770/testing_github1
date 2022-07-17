import pymongo

client = pymongo.MongoClient("mongodb+srv://bhupendra:Rajput77@cluster0.xlf2p.mongodb.net/?retryWrites=true&w=majority")
db = client.test
#client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
#db = client.test
print(db)

d = {
    "name":"aman",
    "email":"aman@gmail.com",
    "surname":"rajput"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)

"hi"