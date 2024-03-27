def insecure_eval(input_string):
    return eval(input_string)

user_input = input("Enter a string: ")
print(insecure_eval(user_input))