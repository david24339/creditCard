#import the exit module to use the exit command
import sys

#implementation of the checkCard function which takes a card number as an argument.
def checkCard(number):
    multiply2=""
    conter = 0
    #multiply each element with even index including 0 and concatenate each result as a string.
    while conter < len(number):
        multiply2=multiply2 + str(int(number[conter])*2)
        conter += 2
    #add each digit(each character in multiply2).
    new = 0
    # iterate through each character, transform it into a number and add all of them. 
    for i in multiply2:
        new = new + int(i)
        
    #iterate through all the digit that were not multiplied by two and add them.
    new2 = 0
    conter2 = 1

    #multiply element with odd index (without including 0) and store the result in a variable.
    while conter2 < len(number):
        new2 = new2 +int(number[conter2])
        conter2 += 2

    #add the sum of digits of the numbers multiply by 2 with the sum of the number not multiply by two and make the result a string.
    david = str(new + new2)

    #if the last digit of that string is 0, then the credit card or debit card is valid and the function return True.
    if david[len(david)-1]== "0":
        return True

    #otherwise it is not and the function return False.
    else:
        return False

#implementation of  the cardIssuer function which takes as input the card number.
def cardIssuer(number):
    #if the card number start with 34 or 37, then it is American Express.
    if number[0:3] == "34" or number[0:3] == "37":
        print("American Express")

    #if the card number start with 4, then it is VISA.
    elif number[0] == "4":
        print("VISA")

    #if the card number start with 5, then it is Mastercard.
    elif number[0] == "5":
        print("Mastercards")

    #if the card number start with 6, then it is Discover Card.
    elif number[0] == "6":
        print("Discover Cards")
#implementation of the main function of our program.
def main():
    #print a welcome message and describe our program to the user.
    print("------------------------------------")
    print("Welcome to the credit card checker")
    print("------------------------------------")
    print()
    #Take the card number as an input from the user.
    cardNumber = input("Please input your credit card number(e.g 1234567893456789):")

    #Check whether the user colaborate and inputted only number
    if not (cardNumber.isdigit()):
        print("You probably type a character that is not a number. TRY AGAIN")
        sys.exit(0)
        
    #call the checkCard function to check the card number.
    result=checkCard(cardNumber)

    #If the checkCard function return True ,then print a message to the user that the card number inputted is correct and run the cardIssuer. function
    if result == True:
        print("correct")
        #call the cardIssuer function determine whether it is VISA ,Masterclass ,American Express or Discover Card. 
        cardIssuer(cardNumber)

    #if the checkCard function return False, then print a message to let them know that number inputted is incorrect.
    else :
        print("incorrect")
    
main()