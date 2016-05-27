#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Brian D'
SITENAME = u'sending'
SITEURL = ''

DISPLAY_CATEGORIES_ON_MENU = False
OUTPUT_RETENTION = ('.git',)

GOOGLE_ANALYTICS = 'UA-58834179-1'

PATH = 'content'

THEME = '/Users/bdunlay/Projects/blog/pelican-themes/clean-blog'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/_i3d'),
          ('LinkedIn', 'http://linkedin.com/in/briandunlay'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
