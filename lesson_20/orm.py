from sqlalchemy import create_engine
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (
    Session,
    sessionmaker,
    relationship,
    backref,
)

engine = create_engine("sqlite:///lesson_20.db", echo=True)
Base = declarative_base()
session: Session = sessionmaker(bind=engine)()


# One-to-One Relation

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    user_name = Column(String(length=50), unique=True, index=True)
    profile = relationship(
        "Profile",
        uselist=False,
        backref=backref("user", uselist=False)
    )
    posts = relationship("Post", backref="user")

    def __repr__(self):
        return f"<User(id={self.id}, name={self.user_name})>"


class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True)
    prof_name = Column(String(length=50))
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)

    def __repr__(self):
        return f"<Profile(id={self.id}, name={self.prof_name})>"


# One-to-Many Relation
class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    body = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))


Base.metadata.create_all(engine)

user = User(user_name="george")
prof = Profile(prof_name="george profile")
post = Post(title="Europe", body="Europe is a world's part.")
user.profile = prof
user.posts.append(post)

session.add_all([user, prof, post])
session.commit()

print(post.user.profile.prof_name)

