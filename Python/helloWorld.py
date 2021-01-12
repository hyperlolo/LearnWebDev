import random

def hello():
    print("Hello World")
    
def randomNum():
    stmt = "This is a random number between 1 and 20: {rand}"
    print(stmt.format(rand = random.randint(1, 20)))
    

def start():
    hello()
    randomNum()
    
    
start()