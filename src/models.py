import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()



class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_to_id = Column(Integer, ForeignKey('user.id'), nullable=False )
    user_from_id = Column(Integer, ForeignKey('user.id'), nullable=False )

    #relationships
    user = relationship('User', back_populates="Follower", single_parent=True, 
    uselist=False, cascade="all, delete-orphan")
   

    
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(255))
    firts_name = Column(String(20))
    email = Column(String(200))
    last_name = Column(String(100))
    adderess = Column(String(255))

     #relationships
    follower_id = relationship('Follower', back_populates="user", 
    single_parent=True, cascade="all,delete-orphan")
    commets = relationship("Comment", back_populates="User",cascade="all,delete-orphan")
    

class  Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    author_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    follower_id = Column(Integer)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)

    #relationships
    user = relationship('User', back_populates="Commet", uselist=False, single_parent=True)
    Post = relationship('Post', back_populates="Commet", uselist=False, single_parent=True)


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False) 
    latitude = Column(String(50))
    upload_date = Column(DateTime())

    #relationships
    comment = relationship('Comment', back_populates="Post", uselist=False, single_parent=True)
    user = relationship('User', back_populates="Post", uselist=False, single_parent=True)
    

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(String(50), nullable=False)
    url = Column(String(50), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)

    #relationships
    post = relationship('Post', back_populates="Media", uselist=False, single_parent=True)


class Post_Likes(Base):
    __tablename__ = 'post_likes'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    user_id = Column(Integer,ForeignKey('post.id'), nullable=False )

    #relationships
    post = relationship('Post', back_populates="Post_Likes", uselist=False, single_parent=True)



    def to_dict(self):
        return {}





## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
