number=15
print(number)
name="Zohaib Younis"
print(name);
print(type(name))
print(len(name))

name2="Shahzaib Younis"
length=len(name2)
print(length)
#here we are doing type casting converting length from int to string so that we can concatenate it with name and name2
print(name+" "+ str(length)+" "+name2)

#function to convert type of variable
'''int()
float()
str()
bool()'''


print("10"+ "20") #this will concatenate the two strings and give us 1020
print(int("10")+ int("20")) #this will convert the strings to integers and then 


#input function
num1=input("Enter first number: ")
num2=input("Enter second number: ")
sum=int(num1)+int(num2)
print("The sum of "+ num1 + " and " + num2 + " is: " + str(sum))
