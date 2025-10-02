from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()   # ye line bilkul upar honi chahiye

class Topic(Base):
    __tablename__ = "topics"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    quizzes = relationship("Quiz", back_populates="topic")

class Quiz(Base):
    __tablename__ = "quizzes"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    topic_id = Column(Integer, ForeignKey("topics.id"))
    topic = relationship("Topic", back_populates="quizzes")
    submissions = relationship("Submission", back_populates="quiz")

class Submission(Base):
    __tablename__ = "submissions"
    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String)
    score = Column(Integer)
    quiz_id = Column(Integer, ForeignKey("quizzes.id"))
    quiz = relationship("Quiz", back_populates="submissions")