from database import SessionLocal
from models import Topic, Quiz, Submission

db = SessionLocal()

# --- Step 1: Add Topics ---
topic1 = Topic(name="Python Basics")
topic2 = Topic(name="SQL Fundamentals")
db.add_all([topic1, topic2])
db.commit()

# --- Step 2: Add Quizzes ---
quiz1 = Quiz(title="Python Variables Quiz", topic_id=topic1.id)
quiz2 = Quiz(title="SQL Joins Quiz", topic_id=topic2.id)
db.add_all([quiz1, quiz2])
db.commit()

# --- Step 3: Add Submissions ---
submission1 = Submission(user_name="Vaishali", score=90, quiz_id=quiz1.id)
submission2 = Submission(user_name="Rohit", score=80, quiz_id=quiz2.id)
db.add_all([submission1, submission2])
db.commit()

print(" Test data added successfully!")
