# -*- coding: utf-8 -*-
import sys, os

source_suffix = '.rst'
master_doc = 'index'
project = u'ドキュメントジェネレータSphinx'
copyright = u'2013, Takayuki SHIMIZUKAWA'
version = release = '6.0'
exclude_patterns = ['_build']
templates_path = ['_templates']
pygments_style = 'sphinx'
extensions = ['sphinxjp.themecore']
html_logo = 'sphinx-logo.png'
html_static_path = ['_static']
locale_dirs = ['locale']
html_use_index = False

#html_theme = 'html'
html_theme = 's6'
#html_theme = 'bizstyle'
#language = 'ja'
language = 'en'


def setup(app):
    app.add_stylesheet('custom.css')

