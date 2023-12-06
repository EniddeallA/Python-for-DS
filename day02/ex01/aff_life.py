from load_csv import load
import matplotlib.pyplot as plt

def aff_life():
    df = load("life_expectancy_years.csv")
    data = df.loc[df["country"] == "Morocco"]
    data = data.drop(columns=["country"]).T
    
    plt.plot(data)
    plt.title("Life expectancy in Morocco")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.show()

aff_life()