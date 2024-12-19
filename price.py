import json
import os


def predict_price(mileage: float):
    theta1 = 0
    theta0 = 0
    if os.path.exists('model.json') is True:
        j_file = None
        with open("model.json", 'r') as file:
            j_file = file.read()
        param = json.loads(j_file)
        # print(param)
        theta0 = param['theta0']
        theta1 = param['theta1']
        mean = param['mean']
        std = param['std']
        mileage = (mileage - mean)/std
    y_p = theta0 + (theta1 * mileage)
    if y_p < 0:
        y_p = 0
    print(f"the estaimated price: {y_p}")


def main():
    try:
        mileage = float(input("enter the mileage of the car: "))
        # print(mileage, type(mileage))
        if mileage < 0:
            raise Exception("mileage can't be negative")
        predict_price(mileage)
    except ValueError:
        print("please enter a number")
    except Exception as e:
        print(f"{e}")


if __name__ == "__main__":
    main()
