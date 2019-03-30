import uuid
import datetime
from database import Database

__author__ = 'dhairya'


class Post(object):

    def __init__(self, blog_id, title, content, author, date=datetime.datetime.utcnow(), id=None):
        # default parameters always need to be in the end
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.date = date
        self.id = uuid.uuid4().hex if id is None else id

    def save_to_mongodb(self):
        # Posts.save_to_mongo()
        Database.insert(collection='posts', data=self.jason())

    def jason(self):
        return {
            'id' : self.id,
            'blog_id' : self.blog_id,
            'author' : self.author,
            'content' : self.content,
            'title' : self.title,
            'created_date' : self.date
        }

    @classmethod
    def from_mongo(cls,id):
        post_data = Database.find_one(collection= "posts", query={'id': id})
        return cls(blog_id=post_data['blog_id'],
                   title=post_data['title'],
                   content=post_data['content'],
                   author=post_data['author'],
                   date=post_data['date'],
                   id=post_data['id'])

#    @staticmethod
#    def from_mongo(id):
#       # Post.from_mongo(123)
#        return Database.find_one(collection= "posts", query={'id': id})

    @staticmethod
    def from_blog(id):
        # Post.from_blog(1)

        return [post for post in Database.find(collection= "posts", query={'blog_id': id})]
