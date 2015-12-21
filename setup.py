#!/usr/bin/python3
from distutils.core import setup

# find out if pymongo, mongodb, mutagen and tornado are installed

setup(
	name='Ampnado',
	version='1.0',
	description='Home Media Streaming Server',
	author='Charlie Smotherman',
	author_email='porthose.cjsmo.cjsmo@gmail.com',
	#url=github
	packages=['ampnado'],
	package_dir = {'ampnado': 'ampnado/src'},
	package_data = {'ampnado': ['docs/*'], ['logs/*'],
		['static/css/*'], ['static/images/*'], ['static/js/*'], ['static/favicon.ico'],
		['templates/*'], ['tests/*']},
	scripts['ampnado/ampnado', 'ampnado/server'],

)