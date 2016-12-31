from database import Database
__author__ = "Arjun"

class Post(object):

    def __init__(self, blog_id, title, content, author, id, date):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.id = id
        self.date = date

    def save_to_mongo(self):
        Database.insert('posts', self.json())

    def json(self):
        return{
            'id' : self.id,
            'blog_id' : self.blog_id,
            'author' : self.author,
            'content' : self.content,
            'title' : self.title,
            'date' : self.date
        }