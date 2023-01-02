message = ("Hello Mr\Ms")
name = str (input("Enter your name"))
age = int (input("Enter your age"))

address = str (input("Enter your address"))
message2 = ("thanks for beening one of our community,\t\t Enjoy")
print(message, name, age, address, message2)


first_number = ""
second_number = ""

def get_inputs():
    global first_number , second_number

    first_number = input("Welcome , Enter 1st number: ")
    second_number = input("Enter 2nd number: ")

def valibdate_values(value1 : str , value2 : str):
    return value1.isdigit() and value2.isdigit()

def print_oprations():
    print("1_+\n2_-\n3_*\n4_/\n5_^\n6_%")
    opr_value = input("Enter your opration: ")
    return opr_value

def check_opration_and_return_result(opration:str) -> int:
    if opration =="+" or opration == "1":
        return int(first_number) + int(second_number)
    if opration =="-" or opration == "2":
        return int(first_number) + int(second_number)
    if opration =="*" or opration == "3":
        return int(first_number) + int(second_number)
    if opration =="/" or opration == "4":
        return int(first_number) + int(second_number)
    if opration =="^" or opration == "5":
        return int(first_number) + int(second_number)
    if opration =="%" or opration == "6":
        return int(first_number) + int(second_number)

get_inputs()
validation_result = valibdate_values(first_number , second_number)

if validation_result:
    opr = print_oprations()
    result = check_opration_and_return_result(opr)
    print(result)
else:
    print("Invalid inputs")
    
    
   
  
number1 = input("Enter 1st number")
number2 = input("Enter 2nd number")
number3 = input("Enter 3th number")
number4 = input("Enter 4th number")
number5 = input("Enter 5th number")

numbers = [number1, number2, number3, number4, number5]

print("The biggest number" , max(number1, number2, number3, number4, number5))
print("The smallest number" , min(number1, number2, number3, number4, number5))


