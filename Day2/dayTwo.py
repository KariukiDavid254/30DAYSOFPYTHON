temperature = float(input("Enter temperature in Fahrenheit: ")) #prompts the user to enter a temperature in Fahrenheit
#float() function is used to convert the user input from a string to a float

raining = input("Is it raining? (yes/no): ").lower() == "yes" #prompts the user to enter whether it is raining or not

if temperature < 50:
    print("outfit: Coat, hat, scarf, and gloves.")
elif 50 <= temperature <= 70 and not raining:
    print("outfit: Sweater or light jacket.")
elif 50 <= temperature <= 70 and raining:
    print("outfit: Rain jacket and boots.")
elif temperature > 70 and not raining:
    print("outfit: T-shirt and shorts.")
elif temperature > 70 and raining:
    print("outfit: Light jacket and rain boots.")
else:
    print("Unable to suggest an outfit based on the provided information.")
