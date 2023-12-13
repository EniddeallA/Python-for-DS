from load_csv import load
import matplotlib.pyplot as plt


def aff_life():
    """Plot the life expectancy in Morocco from 1960 to 2015."""
    df = load("life_expectancy_years.csv")
    try :
        data = df.loc[df["country"] == "Morocco"]
    except KeyError:
        exit("Column 'country' not found")  
    data = data.drop(columns=["country"]).T
    plt.plot(data)
    plt.title("Life expectancy in Morocco")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.legend(["Morocco"])
    plt.show()


def main():
    aff_life()


if __name__ == "__main__":
    main()
