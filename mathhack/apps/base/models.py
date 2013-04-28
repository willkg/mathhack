from sqlalchemy import Column, ForeignKey, Integer, Sequence, String

from mathhack.database.classes import Model


class Problem(Model):
    __tablename__ = 'problem'
    
    id = Column(Integer, Sequence('problem_id_seq'), primary_key=True,
                autoincrement=True)
    numerator = Column(Integer()) # the upper value
    denominator = Column(Integer()) # the lower value
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
    
    id = Column(Integer, Sequence('answer_id_seq'), primary_key=True,
                autoincrement=True)
    problem_id = Column(Integer, ForeignKey("problem.id"))
    user_id = Column(Integer, ForeignKey("user.id"))
    timestamp = Column(Integer()) # when the user answered the question
    answer = Column(Integer()) # the answer the user provided
    delay = Column(Integer()) # how long it took to answer
