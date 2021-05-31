from plotly import express as px
import pandas as pd
import dominate
import geopandas as gpd
from dominate.tags import *
from dominate.util import raw

url = 'https://raw.githubusercontent.com/painel-covid-19/painel-covid-19.github.io/main/data/df_cidades_campi.csv'

df = pd.read_csv(url)

df_redencao = df.loc[(df['city_ibge_code']== 2311603)]
df_sfc = df.loc[(df['city_ibge_code']== 2929206)]
df_acarape = df.loc[(df['city_ibge_code']== 2300150)]

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

redencao = px.line(
    df_redencao,
    x="date",
    y="last_available_confirmed",
    height=400,
    width=650,
).update_layout(
    title='Confirmados Diários de Redenção',
    yaxis={'title':'Casos Confirmados'},
    xaxis={'title': ''},
    template = "plotly_dark",
    font_color=colors['text']
)

redencao_obitos = px.line(
    df_redencao,
    x="date",
    y="last_available_deaths",
    height=400,
    width=650,
).update_layout(
    title='Óbitos Acumulados de Redenção',
    yaxis={'title':'Óbitos Diários'},
    xaxis={'title': ''},
    template = "plotly_dark",
    font_color=colors['text']
)

acarape = px.line(
    df_acarape,
    x="date",
    y="last_available_confirmed",
    height=400,
    width=650,
).update_layout(
    title='Confirmados Diários de Acarape',
    yaxis={'title':'Casos Confirmados'},
    xaxis={'title': ''},
    template = "plotly_dark",
    font_color=colors['text']
)

acarape_obitos = px.line(
    df_acarape,
    x="date",
    y="last_available_deaths",
    height=400,
    width=650,
).update_layout(
    title='Óbitos acumulados de Acarape',
    yaxis={'title':'Óbitos Diários'},
    xaxis={'title': ''},
    template = "plotly_dark",
    font_color=colors['text']
)

sfc = px.line(
    df_sfc,
    x="date",
    y="last_available_confirmed",
    height=400,
    width=650,
).update_layout(
    title='Confirmados Diários de São Francisco do Conde',
    yaxis={'title':'Casos Confirmados'},
    xaxis={'title': ''},
    template = "plotly_dark",
    font_color=colors['text']
)

sfc_obitos = px.line(
    df_sfc,
    x="date",
    y="last_available_deaths",
    height=400,
    width=650,
).update_layout(
    title='Óbitos Acumulados de São Francisco do Conde',
    yaxis={'title':'Óbitos Diários'},
    xaxis={'title': ''},
    template="plotly_dark",
    font_color=colors['text']
)

'''
with open('p_graph.html', 'w') as f:
    f.write(redencao.to_html(full_html=False, include_plotlyjs='cdn'))
    f.write(redencao_obitos.to_html(full_html=False, ))
    f.write(acarape.to_html(full_html=False, ))
    f.write(acarape_obitos.to_html(full_html=False, ))
    f.write(sfc.to_html(full_html=False, ))
    f.write(sfc_obitos.to_html(full_html=False, ))
'''


def criar_pagina():
    doc = dominate.document(title='Painel Covid')

    with doc.head:
        link(href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0/dist/css/bootstrap.min.css", rel="stylesheet",
             integrity="sha384-wEmeIV1mKuiNpC+IOBjI7aAzPcEZeedi5yW5f2yOq55WWLwNGmvvx4Um1vskeMj0",
             crossorigin="anonymous")

    with doc.body:
        with div(cls='container-fluid bg-dark'):
            with div(cls='row'):
                with div(cls='col'):
                    with div(cls='row m-1 text-info text-center'):
                        h1('Painel Covid-19')
                        with div(cls='col-2'):
                            with div(cls='card bg-secondary text-info text-center'):
                                with div(cls='card-header'):
                                    h6('Óbitos de Acarape')
                                with div(cls='card-body'):
                                    div(f"{df_acarape['last_available_deaths'].iloc[1]}")
                        with div(cls='col-2'):
                            with div(cls='card bg-secondary text-info text-center'):
                                with div(cls='card-header'):
                                    h6(' Casos Confirmados de Acarape')
                                with div(cls='card-body'):
                                    div(f"{df_acarape['last_available_confirmed'].iloc[1]}")
                        with div(cls='col-2'):
                            with div(cls='card bg-secondary text-info text-center'):
                                with div(cls='card-header'):
                                    h6('Óbitos de Redenção')
                                with div(cls='card-body'):
                                    div(f"{df_redencao['last_available_deaths'].iloc[1]}")
                        with div(cls='col-2'):
                            with div(cls='card bg-secondary text-info text-center'):
                                with div(cls='card-header'):
                                    h6('Casos Confrimados de Redenção')
                                with div(cls='card-body'):
                                    div(f"{df_redencao['last_available_confirmed'].iloc[1]}")
                        with div(cls='col-2'):
                            with div(cls='card bg-secondary text-info text-center'):
                                with div(cls='card-header'):
                                    h6('Óbitos de São Francisco Do Conde')
                                with div(cls='card-body'):
                                    div(f"{df_sfc['last_available_deaths'].iloc[1]}")
                        with div(cls='col-2'):
                            with div(cls='card bg-secondary text-info text-center'):
                                with div(cls='card-header'):
                                    h6(' CasosConfirmados de São Francisco Do Conde')
                                with div(cls='card-body'):
                                    div(f"{df_sfc['last_available_confirmed'].iloc[1]}")
                    with div(cls='row m-1'):
                        with div(cls='col-6 mr-1'):
                            raw(redencao.to_html(full_html=False, include_plotlyjs='cdn'))
                        with div(cls='col-6'):
                            raw(redencao_obitos.to_html(full_html=False, ))
                    with div(cls='row m-1'):
                        with div(cls='col-6 mr-1'):
                            raw(acarape.to_html(full_html=False, include_plotlyjs='cdn'))
                        with div(cls='col-6'):
                            raw(acarape_obitos.to_html(full_html=False, ))
                    with div(cls='row m-1'):
                        with div(cls='col-6 mr-1'):
                            raw(sfc.to_html(full_html=False, include_plotlyjs='cdn'))
                        with div(cls='col-6 '):
                            raw(sfc_obitos.to_html(full_html=False, ))
    print(doc)


criar_pagina()
