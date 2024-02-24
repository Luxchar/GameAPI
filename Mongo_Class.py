from pymongo import MongoClient
import json
import os
from dotenv import load_dotenv
import logging
load_dotenv()
# Configure logging
logging.basicConfig(level=logging.INFO)  # Adjust log level as needed
log = logging.getLogger(__name__)

class MongoAPI:
    def __init__(self, data):
        # Database configurations
        self.mongo_url = os.getenv("MONGO_URL")
        
        
        # connect to the database
        self.client = MongoClient(self.mongo_url)
      
        database = os.getenv("DATABASE_NAME")
        collection = data['collection']
        cursor = self.client[database]
        self.collection = cursor[collection]
        self.data = data
    
    def read(self):
        documents = self.collection.find()
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output

    def write(self, data):
            log.info('Writing Data')
            new_document = data['Document']
            response = self.collection.insert_one(new_document)
            output = {'Status': 'Successfully Inserted',
                    'Document_ID': str(response.inserted_id)}
            return output
    def update(self):
        filt = self.data['Filter']
        updated_data = {"$set": self.data['DataToBeUpdated']}
        response = self.collection.update_one(filt, updated_data)
        output = {'Status': 'Successfully Updated' if response.modified_count > 0 else "Nothing was updated."}
        return output

    def delete(self, data):
            filt = data['Document']
            response = self.collection.delete_one(filt)
            output = {'Status': 'Successfully Deleted' if response.deleted_count > 0 else "Document not found."}
            return output

if __name__ == '__main__':
    data = {
        
        "collection": "games",
    }
    # Print the value
    database_name = os.getenv("DATABASE_NAME")
    print("DATABASE_NAME value:", database_name)
    
    mongo_obj = MongoAPI(data)
    print(json.dumps(mongo_obj.read(), indent=4))