def hello(*names):
    for name in names:
         print(f"Hello{names}")
         
def student_attribute(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")  

def my_country(Country="Burundi"):
    print(f"Hello from{Country}")               
   