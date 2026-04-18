import streamlit as st
import pandas as pd
import plotly.express as px


# 1. CARREGAMENTO E PREPARAÇÃO DOS DADOS

car_data = pd.read_csv('vehicles_us.csv')

# Criando a coluna 'manufacturer' (Fabricante) pegando a primeira palavra da coluna 'model'
car_data['manufacturer'] = car_data['model'].apply(lambda x: x.split()[0])


# 2. CABEÇALHO E TABELA DE DADOS

st.header('Análise de Anúncios de Vendas de Veículos')
st.write('Dashboard interativo para análise de dados de veículos usados nos EUA.')

st.subheader('Visualização dos Dados')
st.write('Confira os 1000 anúncios mais recentes:')

# Tabela com scroll interno
st.dataframe(car_data.head(1000), height=400)


# 3. GRÁFICO DE BARRAS: VEÍCULOS POR FABRICANTE

st.subheader('Tipos de Veículos por Fabricante')
st.write('Distribuição dos tipos de carroceria oferecidos por cada marca.')

# Usamos o px.histogram para contar e colorimos pela coluna 'type'
fig_bar = px.histogram(car_data, x="manufacturer", color="type",
                       title="Veículos por Fabricante e Tipo")
st.plotly_chart(fig_bar, use_container_width=True)

st.divider()


# 4. HISTOGRAMAS COMPARATIVOS

st.subheader('Análise de Distribuição (Histogramas)')

opcao_histograma = st.selectbox(
    'Selecione a análise comparativa desejada:',
    ['Preço por Condição', 'Ano do Modelo por Condição']
)

# Funcionalidade do botão
if st.button('Gerar Histograma'):
    st.write(f'Gerando histograma para: {opcao_histograma}')

    if opcao_histograma == 'Preço por Condição':
        fig_hist = px.histogram(car_data, x="price", color="condition",
                                title="Distribuição de Preços baseada na Condição",
                                barmode='overlay')

    elif opcao_histograma == 'Ano do Modelo por Condição':
        fig_hist = px.histogram(car_data, x="model_year", color="condition",
                                title="Idade dos Veículos por Condição",
                                barmode='overlay')

    # Mostrando gráfico
    st.plotly_chart(fig_hist, use_container_width=True)

st.divider()


# 5. GRÁFICO DE DISPERSÃO (Checkbox solto no final)

st.subheader('Relação de Preço e Quilometragem')

# Criando a Checkbox
build_scatter = st.checkbox('Criar um gráfico de dispersão')

# Ao marcar a caixa
if build_scatter:
    st.write(
        'Criando gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros...')

    # Criar a figura
    fig_scatter = px.scatter(car_data, x="odometer", y="price", color="condition",
                             # Mostra o nome do modelo ao passar o mouse
                             hover_data=['model'],
                             title="Preço vs Quilometragem por Condição")

    # Exibir a figura no site
    st.plotly_chart(fig_scatter, use_container_width=True)
