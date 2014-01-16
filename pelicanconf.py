#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Erlio GmbH'
SITENAME = u'Erlio GmbH'
SITEURL = 'http://erl.io'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

OUTPUT_PATH = '.'

DEFAULT_PAGINATION = 10

THEME = './erlio_theme'

#MENUITEMS = (('Blog', 'blog.html'),)
DIRECT_TEMPLATES = (('index'),)
INDEX_SAVE_AS = 'blog.html'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
