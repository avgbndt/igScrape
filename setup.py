try:
	from setuptools import setup
except ImportError:
	from disutils.core import setup

config = {
	'description' : 'Scrape Instagram Last Posts comments',
	'author' : 'avgbndt',
	'url' : 'https://www.evil-ai.com',
	'download_url' : 'None',
	'author_email' : 'avgbndt@gmail.com',
	'version' : '0.3',
	'install_requires' : ['nose','pandas','requests'],
	'packages' : ['NAME'],
	'scripts' : [],
	'name' : 'igScrape'
}

setup(**config)