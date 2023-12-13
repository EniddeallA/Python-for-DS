from load_csv import load
import matplotlib.pyplot as plt


def projection_life():
    """Plot the life expectancy in Morocco from 1960 to 2015."""
    le_df = load("life_expectancy_years.csv")
    gdp_df = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    le_1900 = le_df["1900"]
    gdp_1900 = gdp_df["1900"]
    plt.scatter(gdp_1900, le_1900)
    plt.xlabel('GDP')
    plt.ylabel('Life Expectancy')
    plt.title('1900')
    plt.xscale('log')
    plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])
    plt.show()


def main():
    projection_life()


if __name__ == "__main__":
    main()
