import pandas as pd
import json


def gradient_descent_method(l_rate=0.03, epoch=250):
    # read data
    f_name = "./data.csv"
    df = pd.read_csv(f_name)
    for column in df.columns:
        if df[column].isnull().any():
            raise Exception("the data file don't exist")
    X = df.loc[:, 'km']
    Y = df.loc[:, 'price']
    # Normalize data
    mean = X.mean()
    std = X.std()
    s_X = (X - mean) / std
    # find the theta0 and theta1
    theta0 = 0
    theta1 = 0
    epochs = epoch
    l_r = l_rate
    m = int(len(X))
    for i in range(epochs):
        b = 0
        a = 0
        for j in range(0, m):
            y_e = theta0 + (theta1 * s_X[j])
            b += (y_e - Y[j])/m
            a += ((y_e - Y[j]) * s_X[j])/m
        theta0 = theta0 - (l_r * b)
        theta1 = theta1 - (l_r * a)
    print(f"theta0 :{theta0}  theta1: {theta1}")
    param = {
        "theta0": theta0,
        "theta1": theta1,
        "mean": mean,
        "std": std
    }
    j_file = json.dumps(param)
    with open("model.json", 'w') as file:
        file.write(j_file)


def main():
    try:
        gradient_descent_method()
    except Exception as e:
        print(f"Error: {e}")
    pass


if __name__ == "__main__":
    main()
