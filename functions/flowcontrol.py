def even_numbers():
    x = range(10)
    for i in x:
        if i%2 == 0:
            print(i)
even_numbers()
#print odd numbers
def odd_numbers():
    y = range(20)
    for i in y:
        if i%2 !=0:
            print(i)
odd_numbers() 

def divisible_by_five():
    n = range(100)
    for i in n:
        if i%5==0:
            print(f"${i}is divisible by 5")
        else:
            print(f"${i}not divisible by 5")
divisible_by_five()   

def multiple_comparisons():
    x = range(30)
    for i in x:
        if i%2==0:
            print(f"${i} is divisible by 2")
        elif i%3==0:
            print(f"${i}is divisible by 3")
        elif i%5==0:
            print(f"${i}is divisible by 5")
        else:
            print(f"${i} is not divisble by 2,3,5")   
multiple_comparisons()

def combine_comprasions():
    x = range(30)   
    for i in x:
        if i%2==0 and i%3==0:
            print(f"${i}is divisible by both 2 and 3") 
        elif i%2==0 or  i%3==0:
            print(f"${i}is divisible by either two or three")                                            
        else:
            print(f"${i} is not divisble by 2 or 3")
combine_comprasions() 

def while_loop():
    x = 1
    while x<10:
        print("Hello world")
        x+=1
while_loop()

def break_statement():
    x = 1
    while x<10:
        print("Hello")
        x+=1
        if x==5:
            break
break_statement()                
           