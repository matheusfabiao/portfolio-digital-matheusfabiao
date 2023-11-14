from pathlib import Path
import streamlit as st
from PIL import Image

current_dir = Path(__file__).parent if '__file__' in locals() else Path.cwd()
css_file = current_dir / 'styles' / 'style.css'
resume_file = current_dir / 'assets' / 'Matheus Fabião CV Resume.pdf'
profile_pic = current_dir / 'assets' / 'profile-pic.png'

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

# Load css, pdf and profile pic files
with open(css_file) as file:
    st.markdown(f'<style>{file.read()}</style>', unsafe_allow_html=True)
    
with open(resume_file, 'rb') as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# Hero Section
col1, col2 = st.columns(2, gap='small')
with col1:
    st.image(profile_pic, width=230)
    
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=' 📄 Download CV',
        data=PDFbyte,
        file_name=resume_file.name,
        mime='application/octet-stream'
        )
    st.write('📧', EMAIL)
    
# Social Links
st.write('#')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f'[{platform}]({link})')
    
# Experience & Qualifications
st.write('#')
st.subheader('Experiência e Qualificações')
st.write('''
         - ✔️ 2 anos de experiência em ambiente profissional
         - ✔️ 1 ano de experiência com modelos de IA
         - ✔️ Grande entendimento em estatística aplicada
         - ✔️ Ótimo em trabalho em equipe e comunicação
         - ✔️ Excelência em entendimento de tasks e projetos
         ''')

# Skills
st.write('#')
st.subheader('Habilidades Técnicas')
st.write('''
         - Programação: Python (Scikit-learn, pytorch, pandas), SQL
         - Visualização de Dados: (matplotlib, seaborn, plotly)
         - Modelagem: Regressão Linear, Regressão Logística, Árvores de decisão, Florestas Aleatórias
         - Banco de Dados: Postgres, MongoDB, MySQL, Microsoft SQL Server e Oracle
         ''')

# Work History
st.write('#')
st.subheader('Histórico de Trabalho')
st.write('---')

# Job 1
st.write('🚧', '**Cientista de Dados | Free Lancer**')
st.write('02/2023 - Present')
st.write('''
         - ► Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin lacinia orci quis eleifend placerat. Etiam vel orci neque. Sed feugiat ipsum elit, vitae faucibus libero viverra eu. Suspendisse vehicula tellus vel dapibus pulvinar.
         - ► Praesent accumsan enim in dui pulvinar, a auctor lacus varius. Aliquam erat quam, efficitur euismod efficitur non, dictum in orci. Sed venenatis, justo varius pretium molestie, libero purus luctus felis, at sollicitudin sapien eros vitae nibh.
         - ► Morbi commodo suscipit iaculis. Nulla ultrices fringilla nisi vitae fringilla. Suspendisse nisl justo, sodales sed pharetra ac, scelerisque in massa. Nam vitae nibh vitae leo convallis tincidunt. Ut tempor eu ligula.
         ''')

# Job 2
st.write('#')
st.write('🚧', '**Cientista de Dados | Free Lancer**')
st.write('02/2023 - Present')
st.write('''
         - ► Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin lacinia orci quis eleifend placerat. Etiam vel orci neque. Sed feugiat ipsum elit, vitae faucibus libero viverra eu. Suspendisse vehicula tellus vel dapibus pulvinar.
         - ► Praesent accumsan enim in dui pulvinar, a auctor lacus varius. Aliquam erat quam, efficitur euismod efficitur non, dictum in orci. Sed venenatis, justo varius pretium molestie, libero purus luctus felis, at sollicitudin sapien eros vitae nibh.
         - ► Morbi commodo suscipit iaculis. Nulla ultrices fringilla nisi vitae fringilla. Suspendisse nisl justo, sodales sed pharetra ac, scelerisque in massa. Nam vitae nibh vitae leo convallis tincidunt. Ut tempor eu ligula.
         ''')

# Job 3
st.write('#')
st.write('🚧', '**Cientista de Dados | Free Lancer**')
st.write('02/2023 - Present')
st.write('''
         - ► Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin lacinia orci quis eleifend placerat. Etiam vel orci neque. Sed feugiat ipsum elit, vitae faucibus libero viverra eu. Suspendisse vehicula tellus vel dapibus pulvinar.
         - ► Praesent accumsan enim in dui pulvinar, a auctor lacus varius. Aliquam erat quam, efficitur euismod efficitur non, dictum in orci. Sed venenatis, justo varius pretium molestie, libero purus luctus felis, at sollicitudin sapien eros vitae nibh.
         - ► Morbi commodo suscipit iaculis. Nulla ultrices fringilla nisi vitae fringilla. Suspendisse nisl justo, sodales sed pharetra ac, scelerisque in massa. Nam vitae nibh vitae leo convallis tincidunt. Ut tempor eu ligula.
         ''')

# Projects & Accompliments
st.write('#')
st.subheader('Projetos e Realizações')
st.write('---')
for project,  link in PROJECTS.items():
    st.write(f'[{project}]({link})')