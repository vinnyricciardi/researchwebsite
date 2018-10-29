#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import platform

def is_windows():
    if platform.system() == 'Windows': return True
    else: return False

def system_path(path):
    """Return path with forward or backwards slashes as necessary based on OS"""
    if is_windows(): return path.replace('/', '\\')
    else: return path.replace('\\', '/')

LOAD_CONTENT_CACHE = False

AUTHOR = u'Vinny Ricciardi'
SITENAME = u'DISHING DATA'

# Potential names:
# dishingdata
# eatabledata
# digestingdata
# whosfeeds.us
# data4food

HIDE_SITENAME = True
SITESUBTITLE = u'bridging data science & food security'
# HOMEPAGE_IMG_TXT = "What if we had multiple natural disasters at once - how would it affect our food system?<br/>This map shows synchrony of natural disasters over the last 100 years."
HOMEPAGE_IMG_TXT = """
This site shares my research on our <br/>
global food system 
"""
#  <br/>
# and tech tips I run into while tinkering with code.

SITEURL = 'https://vinnyricciardi.github.io/'
PATH = 'content/'
PAGE_PATHS = ['images']
OUTPUT_PATH = 'output/'
DELETE_OUTPUT_DIRECTORY = True
TIMEZONE = 'EST'
DEFAULT_LANG = 'en'
USE_PAGER = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Ramankutty Lab', 'http://www.ramankuttylab.com/'),
    ('Institute for Resources, Environment, and Sustainability', 'http://ires.ubc.ca/'),
    ('Liu Institute for Global Issues', 'http://liu.arts.ubc.ca/'),
    ('Public Scholars Initiative', 'https://www.grad.ubc.ca/psi'),
    ('Aleph Policy Iniative', 'http://alephpolicy.org/'),
         )
         
# Social widget
SOCIAL = (
    ('LinkedIn', 'https://www.linkedin.com/in/vinnyr/'),
    ('Twitter', 'https://twitter.com/vinnyricciardi'),
    ('GitHub', 'https://github.com/vinnyricciardi/'),
    ('Research Gate', 'https://www.researchgate.net/profile/Vincent_Ricciardi'),
    ('Email', 'mailto:vinnyricciardi@gmail.com'),
         )
         

DEFAULT_PAGINATION = 7

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
TAG_URL = 'tags/{slug}.html'
TAG_SAVE_AS = 'tags/{slug}.html'
TAGS_URL = 'tags.html'
USE_FOLDER_AS_CATEGORY = True

# Generate archive
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'

################## Add custom css #########################
TYPOGRIFY = True
STATIC_PATHS = ['images', 'extra']
STATIC_EXCLUDE_SOURCES = False

EXTRA_PATH_METADATA = {'extra/custom.css':    {'path':'static/custom.css'},
                       'extra/href_scroll.js':{'path':'theme/js/href_scroll.js'},
                       'extra/jquery.zoom.js':{'path':'theme/js/jquery.zoom.js'},
                       }

for k in EXTRA_PATH_METADATA.keys(): # Fix backslash paths to resources if on Windows
    EXTRA_PATH_METADATA[system_path(k)] = EXTRA_PATH_METADATA.pop(k)
    

####################### Theme-Specific Settings #########################
THEME = 'theme/pelican-bootstrap3'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# Pelican Theme-Specific Variables
BOOTSTRAP_THEME =  'cosmo' #'lumen' #'cosmo'#'sandstone'#'lumen'

SITELOGO = 'images/favicon.png'
SITELOGO_SIZE = 20
FAVICON = 'images/favicon.png'
AVATAR = 'images/headshot.png'
BANNER = 'images/banner.jpg'

ABOUT_ME = """
            Vinny Ricciardi is a PhD Candidate of<br>
            Resource Management & Environmental Studies<br>
            at the University of British Columbia.<br><br>
            """


# HOMEPAGE_TXT = """ 
#                 Welcome to farming data. This site shares my research on our global food system 
#                 and tech tips I run into while tinkering with code. 
#                 <br><br>
#                 This site is also where I try out new tools. Sorry in advance if there are some bugs floating around!
#                 """



# HOMEPAGE = """
# <p class="intro">{}</p>
# <center><img src="images/bugs.png" alt="" style="width:10%;height:10%;"></center>
# <br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
# <br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
# """.format(HOMEPAGE_TXT)

HIDE_SIDEBAR = True
DISPLAY_ARTICLE_INFO_ON_INDEX = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = False
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = True
SHOW_ARTICLE_CATEGORY = False
SHOW_ARTICLE_TAG = False
SHOW_ARTICLE_DATE = False
TAG_CLOUD_MAX_ITEMS = 20

# DISQUS_SITENAME =  'https-vinnyricciardi-github-io'
# DISQUS_NO_ID = True
# DISQUS_DISPLAY_COUNTS = True


# PYGMENTS_STYLE = 'monokai'

# PATH_METADATA= '(?P<subcategory_path>.*)/.*'

BOOTSTRAP_NAVBAR_INVERSE = False
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

MENUITEMS = [
    # ('About', [
    #     ('Dishing Data', '/aboutme/aboutdishingdata/'),
    #     ('About Me', '/aboutme/bio/'),
    #     ('Curriculum Vitae', '/aboutme/curriculumvitae/'),
    #     ('Email', 'mailto: vinnyricciardi@gmail.com'),
    #     ]),
    ('About Me', '/aboutme/bio/'),
    ('CV', '/aboutme/curriculumvitae/'),
    ('Research Projects', [
        ('Farm Size', '/smallholders/Farm_Size_Project/index.html'),
        ('&nbsp&nbsp How much food do smallholders produce?', '/smallholders/Global_production/index.html'),
        # ('&nbsp&nbsp Systematic Review', '/misc/Place_Holder/index.html'),        # To be replaced with jupyter notebook
        # ('&nbsp&nbsp Climate Impacts', '/misc/Place_Holder/index.html'),          # To be replaced with jupyter notebook
        # ('&nbsp&nbsp Public Support', '/misc/Place_Holder/index.html'),           # To be replaced with jupyter notebook
        ('Mountain Farming', '/mtnadaptation/Mtn_Adaptation_Project/index.html'), 
        ('&nbsp&nbsp Climate adaptation in mountains: Are they enough?', '/mtnadaptation/Mtn_Adaptation_Project/index.html')    
        ]),
    # ('Tools and Tricks', '/category/toolsntricks.html'),
    ('News', '/news/news/index.html')
    ]

############################ Plugins ######################################
MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['plugins']
PLUGINS = ['ipynb.markup', 
           'i18n_subsites', 
           'simple_footnotes', 
           'feed_summary',
           'page_hierarchy', 
           'extract_toc',
           'sitemap',
           'photos']

IPYNB_IGNORE_CSS = False
IGNORE_FILES = ['.ipynb_checkpoints']
FEED_USE_SUMMARY = True
SUMMARY_MAX_LENGTH = 100

# MARKDOWN = ['fenced_code']
# MARKDOWN = ['toc', 'fenced_code', 'codehilite(css_class=highlight)', 'extra']
# MARKDOWN = ['codehilite(css_class=highlight)', 'extra']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'daily',
        'indexes': 'daily',
        'pages': 'daily'
    }
}

############################ Photo Galleries ######################################
PHOTO_LIBRARY = 'galleries/'
PHOTO_GALLERY = (3000, 2000, 300)


############################ Analytics ######################################
GOOGLE_ANALYTICS = 'UA-112689863-1'
