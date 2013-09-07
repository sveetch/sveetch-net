
.PHONY: help buildout assets scss install sync delpyc clean

# Define environment arguments
BUILDOUTARGS=
SETTINGSARGS=project.settings
ifdef PROD
BUILDOUTARGS=-c production.cfg
SETTINGSARGS=project.settings_production
endif
ifdef DEV
BUILDOUTARGS=-c development.cfg
SETTINGSARGS=project.settings_development
endif

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
	django-instance collectstatic --pythonpath=project/ --noinput --settings=$(SETTINGSARGS)
	django-instance assets build --pythonpath=project/ --settings=$(SETTINGSARGS)

install:
	pip install --upgrade setuptools
	mkdir -p eggs
	python bootstrap.py
	buildout -v $(BUILDOUTARGS)
	chmod 0777 project/static
	chmod 0777 project/media

sync:
	django-instance syncdb --all --settings=$(SETTINGSARGS)
	django-instance migrate --fake --settings=$(SETTINGSARGS)

###########################################################################
# Private interface

# Recursive find to delete all *.pyc files
delpyc:
	find . -name "*\.pyc"|xargs rm -f
