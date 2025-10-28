# db.py
from pymongo import MongoClient, errors
from config import MONGO_URI, MONGO_DB, MONGO_COLLECTION

class MongoDB:
    def __init__(self):
        self.client = MongoClient(MONGO_URI)
        self.db = self.client[MONGO_DB]
        self.col = self.db[MONGO_COLLECTION]
        self.col.create_index("job_id", unique=True)

    def is_seen(self, job_id):
        return self.col.find_one({"job_id": job_id}) is not None

    def mark_seen(self, job):
        try:
            self.col.insert_one(job)
            return True
        except errors.DuplicateKeyError:
            return False
