from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri="mongodb+srv://rohithrajreganti:rohithrajreganti@cluster0.rd7dn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri,server_api=ServerApi('1'),tlsAllowInvalidCertificates=True)

try:
    client.admin.command('ping')
    print("success")
except Exception as e:
    print(e)

