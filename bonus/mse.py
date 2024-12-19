from draw import training_model
import pandas as pd
import numpy as np
import math


def mse(y_p, price, m):
    n_df = pd.DataFrame()
    n_df['y_p'] = y_p
    n_df['price'] = price
    print("the predict values and actual values:\n")
    print(n_df)
    v_y_p = y_p.values
    v_price = price.values
    e = v_y_p.reshape(-1, 1) - v_price.reshape(-1, 1)
    print("the differences  between predict value and real value:\n")
    print(e)
    e = np.square(e)
    print("the square of the difference:\n")
    print(e)
    mse = np.sum(e[:, 0], axis=0)/m
    print(f"the mean square error: {mse}")
    print(f"the root mean square error: {math.sqrt(mse)}")
    return e


def main():
    f_name = '../data.csv'
    df = pd.read_csv(f_name)
    # print(df)
    km = df['km']
    price = df['price']
    theta0, theta1 = training_model(km, price)
    y_p = theta0 + theta1 * ((km - km.mean()) / km.std())
    m = len(km)
    mse(y_p, price, m)


if __name__ == '__main__':
    main()
