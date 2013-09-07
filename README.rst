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

So first you have to install `virtualenv`_ on your system, then you will need some `Devel libraries`_ on your system to compile some modules thereafter with `buildout`_.

To start, clone the project where you want then enter it and initialize the environment : ::

    virtualenv --no-site-packages --setuptools .
    source bin/activate

Then for a quick test install :

    make install

Or for a production install (Apache+fcgid) :

    make install PROD=1

If success, you will have to synchronize database :

    make sync

And for production you also to do this :

    make assets

Also in production you will need to edit the ``project/settings_production.py`` to fit your database access and SMTP host, if you target to publish the site with **Apache2+fcgid** there is a ``etc/apache.cfg`` ready to use for your virtual host.

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

There is also a ``requirements.txt`` file than you can use with `virtualenv`_ + `pip`_. This document will only treat about the `buildout`_ way.
