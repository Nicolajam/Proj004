Python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def main (data_path):
    data = pd.read_csv(data_path)

    X = data.drop("target", axis = 1)
    y = data["target"]

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    print ("Model training completed!")

    if __name__ == "__main__":
        import sys
        data_path = sys.argv[1]
        main(data_path)