def Password_Validator(Password):
    Special_Characters = "!@#$%^&*()_-+~"
    Length = 8

    Size = Upper = Lower = Digit = Spcl = Space = False

    if len(Password) < Length:
        print("Length of password doesn't match. Valid Length = 8")
    else:
        Size = True

    for x in Password:
        if x.islower():
            Lower = True
        elif x.isupper():
            Upper = True
        elif x.isdigit():
            Digit = True
        elif x in Special_Characters:
            Spcl = True
        elif x == ' ':
            Space = True

    if (Size and Upper and Lower and Digit and Spcl) and (not Space):
        print("Password is Valid")
        return True
    else:
        if Space:
            print("Must not cotain Space")
        print("Must have")
        if not Upper:
            print("atleast one uppercase letter")
        if not Lower:
            print("atleast one lowercase letter")
        if not Digit:
            print("atleast one number")
        if not Spcl:
            print("atleast one special character")
        
        return False

attempts = 3
attempts_completed = 0

while attempts_completed < attempts:
    password = input("Enter Password: ")

    if Password_Validator(password):
        break
    else:
        attempts_completed += 1
        print("Attempts left:", attempts - attempts_completed)

if attempts_completed == attempts:
    print("Only three attempts are allowed, try again later")