from pathlib import Path
import streamlit as st
from PIL import Image

current_dir = Path(__file__).parent if '__file__' in locals() else Path.cwd()
css_file = current_dir / 'styles' / 'style.css'
resume_file = current_dir / 'assets' / 'profile-pic.png'

PAGE_TITLE = 'CV Digital | Matheus Fabião'
PAGE_ICON = ':wave:'
NAME = 'Matheus Fabião'
DESCRIPTION = '''
Cientista de Dados, auxiliando empresas por meio do apoio à tomada de decisões baseadas em dados.
'''
EMAIL = 'matheusfabiao.dev@gmail.com'
SOCIAL_MEDIA = {
    'LinkedIn':'',
    'GitHub':''
}
PROJECTS = {
    '🏆Projeto 1':'link 1',
    '🏆Projeto 2':'link 2',
    '🏆Projeto 3':'link 3',
    '🏆Projeto 4':'link 4',
    '🏆Projeto 5':'link 5',
}

st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON
)

st.title('Hello World!')