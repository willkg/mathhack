#!/usr/bin/env python
import os

from buchner.helpers import call_command
from flask.ext.script import Manager
from flask.ext.funnel.manager import manager as funnel_manager

from migrate.exceptions import DatabaseAlreadyControlledError
from migrate.versioning import api as migrate_api

from mathhack.wsgi import app
from mathhack.apps.base.utils import generate_equations


manager = Manager(app)

# Add the Flask-Funnel manager as a submanager
manager.add_command('funnel', funnel_manager)

app_path = os.path.join(os.path.dirname(__file__), 'mathhack')
db_repo = os.path.join(app_path, 'migrations')
db_url = app.config.get('DATABASE_URL')


def get_db_version():
    """Returns the current version of the database"""
    return migrate_api.db_version(url=db_url, repository=db_repo)


@manager.command
def db_create():
    """Create the database"""
    try:
        migrate_api.version_control(url=db_url, repository=db_repo)
        db_upgrade(verbose=False)
        print 'Database created: {0}'.format(app.config['DATABASE_URL'])
    except DatabaseAlreadyControlledError:
        print 'ERROR: Database is already version controlled.'
    print 'Done!'


@manager.command
def db_downgrade(version):
    """Downgrade the database"""
    v1 = get_db_version()
    migrate_api.downgrade(url=db_url, repository=db_repo, version=version)
    v2 = get_db_version()

    if v1 == v2:
        print 'No changes made.'
    else:
        print 'Downgraded: %s ... %s' % (v1, v2)
    print 'Done!'


@manager.command
def db_upgrade(version=None, verbose=True):
    """Upgrade the database"""
    v1 = get_db_version()
    migrate_api.upgrade(url=db_url, repository=db_repo, version=version)
    v2 = get_db_version()

    if verbose:
        if v1 == v2:
            print 'Database already up-to-date.'
        else:
            print 'Upgraded: %s ... %s' % (v1, v2)
        print 'Done!'


@manager.command
def db_version():
    """Get the current version of the database"""
    print get_db_version()
    print 'Done!'


@manager.command
def new_migration(description):
    """Create a new migration"""
    migrate_api.script(description, db_repo)
    print 'New migration script created.'
    print 'Done!'


@manager.command
def install_npm_modules():
    """Uses npm to dependencies in node.json"""
    # This is a little weird, but we do it this way because if you
    # have package.json, then heroku thinks this might be a node.js
    # app.
    call_command('cp node.json package.json', verbose=True)
    call_command('npm install', verbose=True)
    call_command('rm package.json', verbose=True)
    print 'Done!'


@manager.command
def populate_equations():
    generate_equations()
    print 'Done!'


if __name__ == '__main__':
    manager.run()
