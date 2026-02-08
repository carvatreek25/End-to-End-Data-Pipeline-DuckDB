pip install faker pandas
import pandas as pd
from faker import Faker
import random

fake = Faker('pt_BR')  # Gera nomes e dados no padrão brasileiro

def gerar_dados(n_registros=100):
    dados = []
    planos = ['Mensal', 'Trimestral', 'Anual']
    status = ['Ativo', 'Inativo', 'Pendente']

    for i in range(n_registros):
        dados.append({
            'id_cliente': i + 1,
            'nome': fake.name(),
            'email': fake.email(),
            'data_nascimento': fake.date_of_birth(minimum_age=18, maximum_age=70).strftime('%Y-%m-%d'),
            'plano': random.choice(planos),
            'status': random.choice(status),
            'data_adesao': fake.date_between(start_date='-2y', end_date='today').strftime('%Y-%m-%d'),
            'valor_mensalidade': round(random.uniform(89.90, 199.90), 2)
        })
    
    return pd.DataFrame(dados)

# Gerando 500 registros fictícios
df_academia = gerar_dados(500)

# Salvando para usar na sua ingestão
df_academia.to_csv('data/clientes_academia.csv', index=False, encoding='utf-8')
print("Arquivo 'clientes_academia.csv' gerado com sucesso!")


