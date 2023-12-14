from load_csv import load
import matplotlib.pyplot as plt
import numpy as np


def prepare_data(df, country):
    """Returns a Series containing the population of the given country"""
    try:
        data = df.loc[df["country"] == country].drop(columns=["country"]).T
    except KeyError:
        exit("Column 'country' not found")
    data = data.replace({'M': '', 'k': ''}, regex=True)
    data.index = data.index.astype(int)
    data = data.squeeze().astype(float)
    return data.loc[1800:2050]


def plot_data(morocco_data, france_data):
    """Plots the population of Morocco and France"""
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
    """Plots the population of Morocco and France"""
    df = load("population_total.csv")
    morocco_data = prepare_data(df, "Morocco")
    france_data = prepare_data(df, "France")
    plot_data(morocco_data, france_data)


def main():
    aff_pop()


if __name__ == "__main__":
    main()
