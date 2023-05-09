value = input("Insert a value: ")

try:
    value = int(value)
except ValueError:
    try:
        value = float(value)
    except ValueError:
        if value.lower() == 'true':
            value = True
        elif value.lower() == 'false':
            value = False
        else:
            pass 

if type(value) == int:
    print("The variable is an integer.")
elif type(value) == float:
    print("The variable is a floating-point number.")
elif type(value) == str:
    print("The variable is a string.")
elif type(value) == bool:
    print("The variable is a boolean.")
else:
    print("The type of the variable could not be identified.")
