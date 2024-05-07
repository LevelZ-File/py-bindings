project = 'levelz-py'
copyright = '2024, Calculus Games'
author = 'Calculus Games'

extensions = [
    'autoapi.extension',
    'sphinx_favicon'
]

autoapi_dirs = ['../levelz']

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'classic'
html_static_path = ['_static']
favicons = [
    {"rel": "shortcut icon", "type": "image/x-icon", "href": "favicon.ico"},
    {"rel": "icon", "type": "image/png", "href": "favicon.png"},
]
