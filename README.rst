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
.. _pip: http://www.pip-installer.org/

Just a project to build my personal site.

Install
=======

This project is made to be build with `buildout`_ system in a `virtualenv`_ environment. 

So first you have to install `virtualenv`_ on your system, then you will need some `Devel libraries`_ on your system to compile some modules thereafter with `buildout`_.

To start, clone the project where you want then enter it and initialize the environment : ::

    virtualenv --no-site-packages --setuptools .
    source bin/activate

Then for a quick test install :

    make install

If success, you will have to synchronize database :

    make sync

And for production you also have to do this :

    make assets

Buildout environment configs and Django settings
************************************************
    
If you use the ``development.cfg`` or ``production.cfg`` config files with buildout, you will have to create the appropriate settings.

With ``development.cfg`` you should do a ``settings_development.py`` file like this : ::

    from project.settings import *

    INTERNAL_IPS = () # Fill this to your machine IP (the client, not your server) enable django-debug-toolbar

    # Database access, only required if you don't want to use the sqlite3 database, else remove it
    DATABASES = {
        'default': {
            'NAME': 'sveetchnet',
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'USER': 'django',
            'PASSWORD': 'django',
        }
    }

With ``production.cfg`` you should do a ``settings_production.py`` file like this : ::

    from project.settings import *

    DEBUG = TEMPLATE_DEBUG = False

    ASSETS_DEBUG = False
    ASSETS_ROOT = STATIC_ROOT
    ASSETS_AUTO_BUILD = False

    # Fast-cgi options
    FCGI_OPTIONS = {
        'method': 'threaded',
        'daemonize': 'false',
    }

    # SMTP Settings to send Applications emails
    EMAIL_HOST = 'localhost'
    EMAIL_PORT = 25
    EMAIL_SUBJECT_PREFIX = '[sveetch.net] '

    # Database access
    DATABASES = {
        'default': {
            'HOST': 'localhost',
            'NAME': 'sveetchnet',
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'USER': 'login',
            'PASSWORD': 'password',
        }
    }

You should fit your database access and SMTP host and if you target to publish the site with **Apache2+fcgid** there is a ``etc/apache.cfg`` ready to use for your virtual host.

Devel libraries
***************

This is the devel libraries needed to compile some Python libraries, note that the package name can differ for your distribution.

For psycopg2 (a Postgresl driver for Python)
--------------------------------------------

* libpq
* python

For Pillow
----------

* libjpeg
* zlib
* libfreetype

Without buildout
****************

There is also a ``requirements.txt`` file than you can use with `virtualenv`_ + `pip`_. This document will only treat about the `buildout`_ way. Take care that this file will not be allways synchronized with current dependancies, if really needed you can do it yourself from the ``versions.cfg`` file.

Usage
=====

With the buildout install, you won't never use the common ``managed.py`` script to launch Django instance but ``django-instance`` script that was installed in you ``bin/`` directory during the buildout process.

So to launch the Django development server with defaut settings, you will do (from the ``project`` directory) : ::

    django-instance runserver 0.0.0.0:8001
