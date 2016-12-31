import datetime
import uuid
from database import Database
__author__ = "Arjun"

class Post(object):

    def __init__(self, blog_id, title, content, author, id=None, date=datetime.datetime.utcnow()):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.id = uuid.uuid4().hex if id is None else id
        self.date = date

    def save_to_mongo(self):
        Database.insert('posts', self.json())

    def json(self):
        return{
            'id' : self.id,
            'blog_id': self.blog_id,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'date': self.date
        }

    @classmethod
    def from_mongo(cls, id):
        post_data =  Database.find_one(collection='posts', query={'id': id})
        return cls(blog_id=post_data['blog_id'], title=post_data['title'], content=post_data['title'], author=post_data['author'], id=post_data['id'], date=post_data['date'])


    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='posts', query={'blog_id': id})] # we do this while returning a list
