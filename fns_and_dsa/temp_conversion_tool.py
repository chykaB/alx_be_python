fahrenheit_to_celsius_factor = 5/9
celcius_to_fehrenheit_factor = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * fahrenheit_to_celsius_factor

def convert_to_fahrenheit(celsius):
    return celsius * celcius_to_fehrenheit_factor + 32

temperature = int(input("Enter the temperature to convert: "))
check = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
if check == "F":
    convert_to_c = convert_to_celsius(temperature)
    print(f"{temperature}\u00B0F is {convert_to_c}\u00B0C")
elif check == "C":
    convert_to_f = convert_to_fahrenheit(temperature)
    print(f"{temperature}\u00B0C is {convert_to_f}\u00B0F")
    
    
else:
    print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
