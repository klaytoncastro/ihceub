# -*- coding: utf-8 -*-

# Informações básicas
AUTHOR = 'Seu Nome'
SITENAME = 'Meu Blog'
SITEURL = ''

# Caminho para o conteúdo
PATH = 'content'

# Configurações de localidade e idioma
TIMEZONE = 'America/Sao_Paulo'
DEFAULT_LANG = 'pt_BR'
DEFAULT_DATE_FORMAT = '%d de %B de %Y'

# Não gerar feeds durante o desenvolvimento
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Links adicionais
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://jinja.palletsprojects.com/'))

# Configurações adicionais (opcionais) para personalização
THEME = 'notmyidea'  # Tema padrão do Pelican
DISPLAY_PAGES_ON_MENU = True  # Mostrar páginas no menu

# Caminho para arquivos estáticos, como imagens
STATIC_PATHS = ['images']
