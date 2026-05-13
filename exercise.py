Two_Digit_Number = input("Enter a two digit number: ")
#here string indexing is used to access the individual digits of the number
first_digit = Two_Digit_Number[0]
second_digit = Two_Digit_Number[1]

#conversion of string to integer is done so that we can perform addition on the digits
sum=int(first_digit) + int(second_digit)
print("The sum of the digits is: " + str(sum))