from sqlalchemy import Column, Integer

from mathhack.database.classes import Model

class Problem(Model):
    __tablename__ = 'problem'
    
    id = Column(Integer, Sequence('problem_id_seq'), primary_key=True,
                autoincrement=True)
    numerator = Column(Integer())
    denominator = Column(Integer())
    operation = Column(String())
    answer = Column(Integer())

class User(Model): 
    __tablename__ = 'user'
    
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True,
                autoincrement=True)
    email = Column(String())
    name = Column(String())


class Answer(Model):
    __tablename__ = 'answer'
    
    problem_id = Column(Integer, ForeignKey("problem.id"))
    user_id = Column(Integer, ForeignKey("user.id"))
    timestamp = Column(Integer())
    answer = Column(Integer())
    delay = Column(Integer())
