.. _Foundation: http://foundation.zurb.com/old-docs/f3/
.. _modular-scale: https://github.com/scottkellum/modular-scale
.. _Compass: http://compass-style.org/
.. _Django: http://www.djangoproject.com/
.. _rvm: http://rvm.io/
.. _yui-compressor: http://developer.yahoo.com/yui/compressor/
.. _django-debug-toolbar: http://github.com/django-debug-toolbar/django-debug-toolbar/
.. _django-admin-tools: http://pypi.python.org/pypi/django-admin-tools/
.. _django-assets: https://github.com/miracle2k/django-assets
.. _buildout: http://www.buildout.org/
.. _virtualenv: http://www.virtualenv.org/

Just a project to build my personal site.

Install
=======

This project is made to be build with `buildout`_ system in a `virtualenv`_ environment. 

But there is also a ``requirements.txt`` file than you can use with `virtualenv`_+`pip`_. 
This document will only treat about the `buildout`_ way.

So to start, clone the project where you want then enter it and type that : ::

    virtualenv --no-site-packages --setuptools .
    source bin/activate

Sometime, you `setuptools`_ installation on your system is too old (<0.8), if you don't know about it just upgrade it (at this point you should be in your virtual environment so there are no risk for your system) : 

    pip install --upgrade setuptools

*TODO: infos about needed devel libs to build Pillow and psycopg2.*

Then you can start to install the apps : ::

    python bootstrap.py
    buildout -v

*TODO: infos for the project settings and the database*