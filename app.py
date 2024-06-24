import random


num = random.randrange(1000, 10000)

n = int(input("Guess the 4 digit number: "))


if n == num:
    print("Great! You guessed the number in just 1 try! You're a Mastermind!")
else:
    
    ctr = 0

    while n != num:
        
        ctr += 1

        count = 0

        n_str = str(n)

        
        num_str = str(num)

       
        correct = ['X']*4

       
        for i in range(0, 4):
            
            if n_str[i] == num_str[i]:
                
                count += 1
                
                correct[i] = n_str[i]

        
        if count > 0:
            print("Not quite the number. But you did get", count, "digit(s) correct!")
           
            print("Correct digits in correct positions: ", end='')
            for k in correct:
                print(k, end=' ')
            print('\n')
        else:
            
            print("None of the numbers in your input match.")

        print('\n')

        
        n = int(input("Enter your next choice of numbers: "))

   
    if n == num:
        
        ctr += 1
        print("You've become a Mastermind!")
        print("It took you only", ctr, "tries.")
