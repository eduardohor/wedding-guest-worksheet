import pandas as pd

list_df = pd.read_csv('lista-convidados-wp.csv')

list_df = list_df.rename(
    columns={'Unnamed: 8': 'Convidados'}).sort_values(by='Convidados')

names_list = list_df['Convidados']

names_list.to_excel('Lista de Convidados.xlsx', index=False)
