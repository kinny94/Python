from post import Post
from database import Database
import uuid
import datetime
__author__ = "Arjun"

class Blog(object):
    def __init__(self, author, title, description, id=None):
        self.author = author
        self.title = title
        self.description = description
        self.id = uuid.uuid4().hex if id is None else id

    def new_post(self):
        title = input("Enter post Title: ")
        content = input("Enter post content: ")
        date = input("Enter post date or leave blank for today (DDMMYY): ")
        if date == "":
            date = datetime.datetime.utcnow()
        else:
            date = datetime.datetime.strptime(date, "%d%m%Y")
        post = Post(blog_id=self.id, title=title, content=content, date=date, author=self.author)
        post.save_to_mongo()


    def get_posts(self):
        return Post.from_blog(self.id)

    def save_to_mongo(self):
        Database.insert(collection='blogs', data=self.json())

    def json(self):
        return{
            'author': self.author,
            'title' : self.title,
            'description' : self.description,
            'id': self.id
        }

    @classmethod
    # we are using static method because mongo does not know what self is
    # cls will take the current class. we can use this method for other classes as well
    def from_mongo(cls, id):
        blog_data = Database.find_one(collection='blogs', query={'id': id})
        return cls(author=blog_data['author'], title=blog_data['title'], description=blog_data['description'], id=blog_data['id'])

