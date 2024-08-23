from langchain_unstructured import UnstructuredLoader
import pandas as pd
from io import StringIO

def process_file():
    file_path = 'poc_planilha_3.xlsx'

    # Carregue o arquivo
    loader = UnstructuredLoader(file_path)
    docs = loader.load()

    # Extraia a tabela do arquivo
    table_html = docs[0].metadata.get('text_as_html')
    table_io = StringIO(table_html)
    
    # Use Pandas para ler a tabela HTML
    df = pd.read_html(table_io)[0]
    
    # Retorne o DataFrame como dicionário
    return df.to_dict()