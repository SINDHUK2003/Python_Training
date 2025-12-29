import random

Value = random.randint(1, 10)

#print(Value)

ans = False

while not ans:
    predict = int(input("Enter your prediction: "))

    if predict == Value:
        ans = True
        print("Correct Prediction")
    else:
        difference = abs(predict - Value)

        if difference >= 5:
            print("Predicted Value is Far")
        elif difference >= 2:
            print("Predicted Value is Close")
        else:
            print("Value is Very Close")
