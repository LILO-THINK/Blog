import pandas as pd
from jinja2 import Template
import os

# Carregar a planilha
df = pd.read_csv('posts_oldblog.csv')

# Função para reformatar a data de mm/dd/aaaa para dd/mm/aaaa
def reformat_date(date_str):
    return pd.to_datetime(date_str, format='%m/%d/%Y').strftime('%d/%m/%Y')

# Aplicar a função de reformatação à coluna 'date' e criar uma nova coluna 'formatted_date'
df['formatted_date'] = df['date'].apply(reformat_date)

# Carregar o template
with open('template.md', 'r') as file:
    template = Template(file.read())

# Definir o caminho do diretório de destino
    dest_dir = '../_posts/'

# Certificar-se de que o diretório de destino existe
    os.makedirs(dest_dir, exist_ok=True)

# Função para gerar o nome do arquivo
def generate_filename(row):
    date_str = pd.to_datetime(row['date']).strftime('%Y-%m-%d')
    title_str = row['title'].replace(' ', '-').lower()
    return f"{date_str}-{title_str}.md"

# Gerar arquivos Markdown
for index, row in df.iterrows():
    # Gerar o nome do arquivo
    id_filename = generate_filename(row)
    
    # Adicionar a propriedade id à linha
    row['id'] = id_filename

    # Criar a propriedade filename com o caminho completo
    row['filename'] = f"Blog/_posts/{id_filename}"

    # Definir o conteúdo do template com os valores da linha
    content = template.render(
        title=row['title'],
        date=row['formatted_date'],  # Usar a data formatada
        categories=row['categories'],
        mainLink=row['mainLink'],
        links=row['links'],
        text=row['text'],
        id=row['id'],
        filename=row['filename']
    )
    
    # Escrever o arquivo Markdown
    with open(os.path.join(dest_dir, id_filename), 'w') as file:
        file.write(content)

print("Markdown Files - sucess!")
