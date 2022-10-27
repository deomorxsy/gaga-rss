import pymongo

DATABASE = "hlsaver"

class DBHelper:
    def __init__(self):
        client = pymongo.Mongoclient()
        self.db = client[DATABASE]


    def get_user(self, email):
        return self.db.users.find_one({"email": email})

    def add_user(self, email, salt, hashed):
        self.db.users.insert({"email": email, "salt": salt, "hashed": hashed})


    def add_entry(self, feed_uri, owner):
        new_id = self.db.feed.insert({"feed_uri": feed_uri})
        return new_id

    def update_entry(self, feed_uri):
        self.db.feed.update({"_id": _id}, {"$set": {"feed_uri": feed_uri}})

    def get_entries(self, owner_id):
        return list(self.db.tables.find({"owner": owner_id}))

    def delete_entry(self, feed_id):
        self.db.tables.remove({"_id": ObjectId(table_id)})



