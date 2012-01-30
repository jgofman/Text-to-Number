##Jacob Gofman
##Due November 24th

##Conversion of Number Strings to Numbers

units_digit = {'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,
               'eight':8,'nine':9} ## set of numbers for units
tens_digit = {'ten':10,'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,
               'fifteen':15,'sixteen':16,'seventeen':17,'eighteen':18,'nineteen':19,'twenty':20,
              'thirty':30,'forty':40,'fifty':50,'sixty':60,'seventy':70,'eighty':80,'ninety':90} ## set of numbers for tens
large_nums = {'hundred':100,'thousand':1000,'million':1000000} ## set of large numbers

string = ''
input_string = ''
new_string = ''
output = 0

def get_operation(): ## primary function, decide which operation to perform
    operation = raw_input('What would you like to do? Please type "convert", "multiply", \
"divide", "add", or "subtract". ')
    if operation == 'convert': convert_to_number()
    elif operation == 'multiply': multiply_strings()
    elif operation == 'divide': divide_strings()
    elif operation == 'add': add_strings()
    elif operation == 'subtract': subtract_strings()
    else:
        print('\nInvalid entry.\n')
        get_operation()
    return

def convert_to_number(): ## main function, convert text to number
    string = str(raw_input('Please type a number with no more than 6 digits in text form: '))
    ## user input
    string = string.lower()
    ## convert to lowercase
    new_string = string.split()
    ## split into set
    new_string.reverse()
    ## change the order to read from the end
    if ('and') in new_string: new_string.remove('and')
    ## remove 'and' from set

    output = 0 ## final output
    temporary_output = 0 ## output for first 3 numbers
    temporary_output2 = 0 ## output for second 3 numbers
    temporary_output3 = 0 ## output for third 3 numbers
    ## can handle up to 999,999,999
    conv_number = 0 ## number from string converted to number pulled from set
    last_term = '' ## last term
    scale = 'hundred' ## decides what to multiply by
    
    for numword in new_string: ## per word in string set
        if ((numword == 'thousand') or (numword == 'million')): scale = numword ## decide scale
        if ((scale == 'hundred') and ((numword != 'thousand') or (numword != 'million'))):
            ##how to handle 100s (first 3 numbers)
            if ((numword in units_digit) and (last_term == 'hundred')):
                ## if number after hundred is in the units set then multiply them
                multiplier = units_digit.get(numword)
                temporary_output += (multiplier*conv_number)
                conv_number = multiplier*conv_number
                last_term = numword
            elif (numword in units_digit):
                ## add units
                conv_number = units_digit.get(numword)
                temporary_output += conv_number
                last_term = numword
            elif (numword in tens_digit):
                ## add tens
                conv_number = tens_digit.get(numword)
                temporary_output += conv_number
                last_term = numword
            elif (numword == 'hundred'):
                ## add hundred
                conv_number = large_nums.get(numword)
                last_term = numword
            else:
                print('Invalid input. Please try again.') ## handle NaN cases
                get_string()
        elif (scale == 'thousand'):
            ## how to handle 1000, same idea but multiply the converted number by 1000
            if ((numword in units_digit) and (last_term == 'hundred')):
                multiplier = units_digit.get(numword)
                temporary_output2 += ((multiplier*conv_number) * 1000)
                conv_number = multiplier*conv_number
                last_term = numword
            elif (numword in units_digit):
                conv_number = units_digit.get(numword)
                temporary_output2 += (conv_number * 1000)
                last_term = numword
            elif (numword in tens_digit):
                conv_number = tens_digit.get(numword)
                temporary_output2 += (conv_number * 1000)
                last_term = numword
            elif (numword == 'hundred'):
                conv_number = large_nums.get(numword)
                last_term = numword
            elif (numword == 'thousand'):
                scale = numword
            else:
                print('Invalid input. Please try again.')
                get_string()
        elif (scale == 'million'):
            ## how to handle 1000000s, same idea but multiply the converted number by 1000000
            if ((numword in units_digit) and (last_term == 'hundred')):
                multiplier = units_digit.get(numword)
                temporary_output3 += ((multiplier*conv_number) * 1000000)
                conv_number = multiplier*conv_number
                last_term = numword
            elif (numword in units_digit):
                conv_number = units_digit.get(numword)
                temporary_output3 += (conv_number * 1000000)
                last_term = numword
            elif (numword in tens_digit):
                conv_number = tens_digit.get(numword)
                temporary_output3 += (conv_number * 1000000)
                last_term = numword
            elif (numword == 'hundred'):
                conv_number = large_nums.get(numword)
                last_term = numword
            elif (numword == 'million'):
                scale = numword
            else:
                print('Invalid input. Please try again.')
                get_string()
        else:
            print('Error.')
            get_string()
    output = temporary_output + temporary_output2 + temporary_output3 ## add all the temporary outputs to the final output
    print('\nThe number you entered was ' + str(output) + '. \n')
    return(output)

def multiply_strings(): ## obtain numbers separately, then multiply and print
    num1 = convert_to_number() 
    num2 = convert_to_number()

    total = int(num1) * int(num2)
    print('The product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(total) + '.')
    return

def add_strings(): ## obtain numbers separately, then add and print
    num1 = convert_to_number()
    num2 = convert_to_number()

    total = int(num1) + int(num2)
    print('The sum of ' + str(num1) + ' added to ' + str(num2) + ' is ' + str(total) + '.')
    return

def divide_strings(): ## obtain numbers separately, then divide and print
    num1 = convert_to_number()
    num2 = convert_to_number()

    total = int(num1) / int(num2)
    print('The dividend of ' + str(num1) + ' divided by ' + str(num2) + ' is ' + str(total) + '.')
    return

def subtract_strings(): ## obtain numbers separately, then subtract and print
    num1 = convert_to_number()
    num2 = convert_to_number()

    total = int(num1) - int(num2)
    print('The remainder of ' + str(num1) + ' minus ' + str(num2) + ' is ' + str(total) + '.')
    return

get_operation()
