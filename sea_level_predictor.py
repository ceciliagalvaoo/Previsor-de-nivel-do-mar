import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np
def draw_plot():
    # Ler os dados do arquivo
    df = pd.read_csv('epa-sea-level.csv')
    # Criar o diagrama de dispersão
    plt.figure(figsize=(12, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data')
    # Criar a primeira linha de melhor ajuste usando todos os dados
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_all = np.arange(df['Year'].min(), 2051)
    plt.plot(years_all, slope * years_all + intercept, color='red', label='Fit (All Data)')
    # Criar a segunda linha de melhor ajuste usando dados desde o ano 2000
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = np.arange(2000, 2051)
    plt.plot(years_recent, slope_recent * years_recent + intercept_recent, color='green', label='Fit (2000-Present)')
    # Adicionar rótulos e título
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    # Salvar o gráfico e retornar os dados para teste
    plt.savefig('sea_level_plot.png')
    return plt.gca()