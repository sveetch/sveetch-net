
.PHONY: help buildout assets scss install sync delpyc clean

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo
	@echo "  install -- to proceed to a new install of this project. Use clean command before if you want to reset a current install"
	@echo "  clean  -- to clean your local repository from all stuff created by buildout and instance usage"
	@echo "  delpyc  -- to remove all *.pyc files, this is recursive from the current directory"
	@echo
	@echo "  assets -- to minify all assets and collect static files"
	@echo "  scss -- to compile all SCSS stuffs with compass"
	@echo

delpyc:
	find . -name "*\.pyc"|xargs rm -f

clean: delpyc 
	rm -Rf bin include eggs local lib parts django-apps-src develop-eggs .installed.cfg compass/.sass-cache project/webapp_statics/.webassets-cache

scss:
	compass compile -c compass/config.rb compass/

assets:
	bin/django-instance collectstatic --pythonpath=project/ --noinput
	bin/django-instance assets build --pythonpath=project/

syncdb:
	bin/django-instance syncdb --all
	bin/django-instance migrate --fake

install: build_project syncdb

build_project:
	virtualenv --no-site-packages --setuptools .
	bin/pip install --upgrade setuptools
	bin/pip install --upgrade pip
	mkdir -p eggs
	bin/python bootstrap.py
	bin/buildout -v
