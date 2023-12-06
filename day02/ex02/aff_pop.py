from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def prepare_data(df, country):
    data = df.loc[df["country"] == country].drop(columns=["country"]).T
    data = data.replace({'M': ''}, regex=True).astype(float) * 1e6
    data.index = data.index.astype(int)
    data = pd.to_numeric(data.squeeze(), errors='coerce')
    return data.loc[1800:2050]

def plot_data(morocco_data, france_data):
    plt.plot(morocco_data, label='Morocco', color='blue')
    plt.plot(france_data, label='France', color='green')
    plt.title("Population Comparison: Morocco vs France")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend()

    plt.xticks(morocco_data.index[::40])

    y_ticks = np.arange(20000000, france_data.dropna().max(), 20000000)
    y_labels = [f'{int(x/1e6)}M' for x in y_ticks]
    plt.yticks(y_ticks, y_labels)

    plt.show()

def aff_pop():
    df = load("population_total.csv")
    morocco_data = prepare_data(df, "Morocco")
    france_data = prepare_data(df, "France")
    plot_data(morocco_data, france_data)

aff_pop()