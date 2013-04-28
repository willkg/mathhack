from flask import (Blueprint, current_app, render_template, redirect,
                   request, session, url_for)

from mathhack.database import get_session

from mathhack.apps.base.models import User


blueprint = Blueprint('base', __name__,
                      template_folder='templates')


@blueprint.route('/')
def index():
    return render_template('base/index.html')


@blueprint.route('/login', methods=['POST'])
def login():
    """Handles the POST from the login form."""
    username = request.POST.get('username', '')

    if not username:
        return render_template('base/index.html', {
                'errors': 'Bad username'
        })

    db = get_session(current_app)
    user = db.query(User).filter_by(name=username).first()
    if not user:
        return render_template('base/index.html', {
                'errors': 'Bad username'
        })

    session['username'] = user.name
    return redirect(url_for('dashboard'))


@blueprint.route('/dashboard')
def dashboard():
    """Shows the user's dashboard page."""
    # TODO: pull results from past problem sets from the db and
    # send to template.

    return render_template('base/dashboard.html', {
            'username': session['username']
    })


@blueprint.route('/problemset')
def problem_set():
    """Initial problem set page."""

    return render_template('base/problem_set.html')
