try:
    number = int(input("Enter a number: "))
    print("The number is entered is", number)

except ValueError as ex:
    print("Exception:", ex)