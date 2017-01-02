from src.models.post import Post
from src.common.database import Database
import uuid
import datetime
__author__ = "Arjun"

class Blog(object):
    def __init__(self, author, title, description, _id=None):
        self.author = author
        self.title = title
        self.description = description
        self._id = uuid.uuid4().hex if _id is None else _id

    def new_post(self, title, content, date=datetime.datetime.utcnow()):
        post = Post(blog_id=self._id, title=title, content=content, date=date, author=self.author)
        post.save_to_mongo()


    def get_posts(self):
        return Post.from_blog(self._id)

    def save_to_mongo(self):
        Database.insert(collection='blogs', data=self.json())

    def json(self):
        return{
            'author': self.author,
            'title' : self.title,
            'description' : self.description,
            '_id': self._id
        }

    @classmethod
    # we are using static method because mongo does not know what self is
    # cls will take the current class. we can use this method for other classes as well
    def from_mongo(cls, id):
        blog_data = Database.find_one(collection='blogs', query={'_id': id})
        return cls(**blog_data)
