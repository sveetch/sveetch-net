
.PHONY: help buildout assets scss install delpyc clean

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo
	@echo "  clean  -- to clean your local repository from all stuff created by buildout and instance usage"
	@echo "  buildout -- to run the buildout process"
	@echo "  install -- to run the full install process (buildout, assets, django init), you'll have to create the virtual environment and active it before"
	@echo
	@echo "  assets -- to minify all assets and collect static files"
	@echo "  scss -- to compile all SCSS stuffs with compass"
	@echo

clean: delpyc 
	rm -Rf bin include eggs lib parts django-apps-src develop-eggs .installed.cfg compass/.sass-cache src/webapp_statics/.webassets-cache

scss:
	compass compile -c compass/config.rb compass/

assets:
	django-instance assets build --pythonpath=project/
	django-instance collectstatic --pythonpath=project/ --noinput

install:
	pip install --upgrade setuptools
	python bootstrap.py
	buildout -v
	compass compile -c compass/config.rb compass/
	django-instance syncdb --all --settings=project.settings
	django-instance migrate --fake --settings=project.settings

###########################################################################
# Private interface

# Recursive find to delete all *.pyc files
delpyc:
	find . -name "*\.pyc"|xargs rm -f
