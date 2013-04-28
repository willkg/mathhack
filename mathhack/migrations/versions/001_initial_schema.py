from sqlalchemy import *
from migrate import *


from mathhack.database.classes import Model


meta = MetaData()


problem = Table(
    'problem', meta,
    Column('id', Integer, Sequence('problem_id_seq'), primary_key=True,
           autoincrement=True),
    Column('numerator', Integer()),
    Column('denominator', Integer()),
    Column('operation', String()),
    Column('answer', Integer()))


user = Table(
    'user', meta,
    Column('id', Integer, Sequence('user_id_seq'), primary_key=True,
           autoincrement=True),
    Column('email', String()),
    Column('name', String()))


answer = Table(
    'answer', meta,
    Column('id', Integer, Sequence('answer_id_seq'), primary_key=True,
           autoincrement=True),
    Column('problem_id', Integer, ForeignKey("problem.id")),
    Column('user_id', Integer, ForeignKey("user.id")),
    Column('timestamp', Integer()),
    Column('answer', Integer()),
    Column('delay', Integer()))


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    problem.create()
    user.create()
    answer.create()


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    problem.drop()
    user.drop()
    answer.drop()
