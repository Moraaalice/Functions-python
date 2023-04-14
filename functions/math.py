def addition(a,b):
    answers = (a+b)
    return answers
    
def subtraction(a,b):
    answers = (a-b)
    return answers

def multiplication(a,b):
    answers = (a*b)
    return answers

def modulus(a,b):
    answers = (a%b)
    return answers  

def sum(*numbers):
    answer = 0
    for number in numbers:
        answer+=number
    return answer
#write a function that accepts any number of intergers and returns the result of
#all of them

def multiply(*num):
    product = 1
    for n in num:
        product*=n
    return product    
        
        
        
    
          
        