import pandas as pd
import matplotlib.pyplot as plt


def training_model(km, price, l_rate=0.03, epochs=250):
    theta0 = 0
    theta1 = 0
    m = len(km)
    km_s = (km - km.mean())/km.std()
    for i in range(epochs):
        a = 0
        b = 0
        for j in range(m):
            y_e = theta0 + theta1 * km_s[j]
            a += (y_e - price[j])/m
            b += ((y_e - price[j]) * km_s[j])/m
        theta0 -= l_rate * a
        theta1 -= l_rate * b
        y_p = theta0 + theta1 * km_s
        # plt.plot(km, y_p, ls=':' )
    # print(f"theta0: {theta0} theta1: {theta1}")
    plt.plot(km, y_p,  color='blue')
    return theta0, theta1


def main():
    file_name = "../data.csv"
    df = pd.read_csv(file_name)
    # print(df)
    km = df.loc[:, 'km']
    price = df.loc[:, 'price']
    training_model(km, price)
    plt.scatter(km, price, color='red')
    plt.xlabel("mileage (in Km)")
    plt.ylabel("price (in Euro)")
    plt.show()


if __name__ == "__main__":
    main()
