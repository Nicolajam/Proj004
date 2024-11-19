Python
import pandas as pd

def main():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databasers/iris/iris.data"
    output_path = "data/iris.csv"

    data = pd.read_csv(url)
    data.to_csv(output_path, index=False)

    print (f"Data downloaded and saved to: {output_path}")
    if __name__ == " __main__ ":
        main()