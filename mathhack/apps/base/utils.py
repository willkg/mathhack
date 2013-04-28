# TODO: import the equation model

from flask import current_app
from mathhack.database import get_session
from mathhack.apps.base.models import Problem

def generate_equations():
    db = get_session(current_app)

    problem = Problem(numerator=1, denominator=1, operation="x", answer=1)
    db.add(problem)
    problem = Problem(numerator=1, denominator=2, operation="x", answer=2)
    db.add(problem)
    problem = Problem(numerator=1, denominator=3, operation="x", answer=3)
    db.add(problem)
    problem = Problem(numerator=1, denominator=4, operation="x", answer=4)
    db.add(problem)
    problem = Problem(numerator=1, denominator=5, operation="x", answer=5)
    db.add(problem)
    problem = Problem(numerator=1, denominator=6, operation="x", answer=6)
    db.add(problem)
    problem = Problem(numerator=1, denominator=7, operation="x", answer=7)
    db.add(problem)
    problem = Problem(numerator=1, denominator=8, operation="x", answer=8)
    db.add(problem)
    db.commit()

