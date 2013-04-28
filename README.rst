========
 README
========

Summary
=======

Mathhack is something we threw together on a Saturday at Brian's
house.


Install and configure
=====================

1. Create a virtual environment.
2. Run::

       pip install -r requirements.txt


Run server
==========

Run::

    $ python manage.py runserver


That will launch the server process on http://127.0.0.1:5000/ which
means that it's running on port 5000 on your computer and is available
only to you---it is not available to other computers on the network
you're on.

If you want to make it available to other computers, do::

    $ python manage.py runserver --host HOST --port PORT

where:

* ``HOST`` is your ip address or the host you want to bind to and 
* ``PORT`` is the port number you want to use


Run tests
=========

Run::

    $ nosetests
