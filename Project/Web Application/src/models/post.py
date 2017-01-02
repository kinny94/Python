import datetime
import uuid
from src.common.database import Database
__author__ = "Arjun"

class Post(object):

    def __init__(self, blog_id, title, content, author, _id=None, date=datetime.datetime.utcnow()):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self._id = uuid.uuid4().hex if _id is None else _id
        self.date = date

    def save_to_mongo(self):
        Database.insert(collection='posts', data=self.json())

    def json(self):
        return{
            '_id' : self._id,
            'blog_id': self.blog_id,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'date': self.date
        }

    @classmethod
    def from_mongo(cls, id):
        post_data =  Database.find_one(collection='posts', query={'_id': id})
        return cls(**post_data)         # we can only do this if the name in the database and name here is same


    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='posts', query={'blog_id': id})] # we do this while returning a list
