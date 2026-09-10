from multiprocessing import Process, freeze_support
import time

def calculate(number):
    print(f"Processing {number}")
    
    result = 0
    
    for i in range(10_000_000):
        result += i * number 
    print(f"Completed {number}")

if __name__ == '__main__':  
    freeze_support()
    
    p1 = Process(
        target= calculate, args=(1,)
    )  
    p2 = Process(
        target= calculate, args=(2,)
    ) 
    p3 = Process(
        target= calculate, args=(3,)
    )     

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    print("All calculations completed..!!!")