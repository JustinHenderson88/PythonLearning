# write your code here
import time

def greet(bot_name, birth_year):
    #print output from input using formatted string
    print(f"Hello my name is {bot_name}")
    print(f"I was created in {birth_year}")

def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')

#prompt user to guess age
def guess_age():
    print("Let me guess your age.")
    print("Enter remainders of dividing your age by 3, 5 and 7.")
    rm1 = int(input()) #get remainders from user
    rm2 = int(input())
    rm3 = int(input())
    #formula for guessing users age
    age = (rm1 * 70 + rm2 * 21 + rm3 * 15) % 105
    #print age
    print(f"Your age is {age}; that's a good time to start programming")

def count():
    print('Now I will prove to you that I can count to any number you want.')
    # read a number and count to it here
    user_input = int(input(' '))
    n = 0
    while n <= user_input: #count number 
        print(f"{n} !")
        n += 1


def test():
    print("Let's test your programming knowledge.")
    # write your code here
    print('''Why do we use methods?
    1. To repeat a statement multiple times.
    2. To decompose a program into several small subroutines.
    3. To determine the execution time of a program.
    4. To interrupt the execution of a program.''')
    answer = int(input())
    if answer == 2:
        print('Completed, have a nice day!')
    else:
        print('Please, try again.')


def end():
    print('Congratulations, have a nice day!')
    

greet('Jarvis', '2020')  # change as needed
remind_name()
guess_age()
count()
test()
end()


