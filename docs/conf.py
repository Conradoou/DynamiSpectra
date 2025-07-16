from __future__ import unicode_literals
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join("..", "src")))

# Mock de bibliotecas para evitar erros na doc
autodoc_mock_imports = [
    'adjustText', 'altair', 'gseapy', 'kneed', 'matplotlib',
    'networkx', 'numpy', 'pandas', 'scikit-learn', 'sklearn',
    'scipy', 'seaborn', 'statsmodels', 'UpSetPlot',
    'xlrd', 'zipp', 'pycirclize'
]

# -- Informações do Projeto ------------------------------------------------
project = 'DynamiSpectra'
author = 'Iverson Conrado Bezerra'
copyright = '2025, ' + author
version = '1.0'
release = '1.1.0'

# -- Extensões ------------------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.extlinks',
    'sphinx.ext.ifconfig',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx.ext.imgmath',
    'sphinx.ext.imgconverter'
]

source_suffix = '.rst'
master_doc = 'index'

# -- HTML Config ----------------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = '_static/logo1.png'
html_use_smartypants = True
html_last_updated_fmt = '%b %d, %Y'
templates_path = ['_templates']

html_short_title = f'{project}-{release}'

# Use caminho ABSOLUTO para custom.css para funcionar no GitHub Pages subpasta
html_css_files = [
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css',
    '/DynamiSpectra/_static/custom.css',  # caminho absoluto
]
html_js_files = []

html_context = {
    'pdf_url': 'https://dynamispectra.readthedocs.io/_/downloads/en/latest/pdf/',
}

html_sidebars = {
    '**': ['searchbox.html', 'globaltoc.html', 'sourcelink.html'],
}

# Config para GitHub Pages com subpasta
html_baseurl = 'https://conradoou.github.io/DynamiSpectra/'

html_theme_options = {
    'canonical_url': 'https://conradoou.github.io/DynamiSpectra/',
    'style_external_refs': True,  # força URLs absolutas para CSS/JS do tema
}

# Isso evita conflitos ao copiar _static para o GitHub
html_extra_path = []

# Adiciona CSS com caminho absoluto para evitar erro no GitHub Pages
def setup(app):
    app.add_css_file('/DynamiSpectra/_static/custom.css')

# -- PDF (LaTeX) Config ----------------------------------------------------
latex_engine = 'xelatex'
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
    'preamble': r'''
        \usepackage{hyperref}
        \usepackage{amsmath}
        \usepackage{graphicx}
    ''',
    'fncychap': r'\usepackage[Bjornstrup]{fncychap}',
}

latex_documents = [
    ('index', 'DynamiSpectra.tex', 'DynamiSpectra', author, 'manual'),
]

# -- Extra ------------------------------------------------------------------
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

extlinks = {
    'issue': ('https://github.com/Conradoou/DynamiSpectra/issues/%s', '#'),
    'pr': ('https://github.com/Conradoou/DynamiSpectra/pull/%s', 'PR #'),
}

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
