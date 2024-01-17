import os
import numpy as numpy

def main(): 
        
    # valeurAB = float(os.environ["a"]) * float(os.environ["b"])
    # print("Affiche A * B : " + str(valeurAB))
    
    a = int(os.environ["a"])
    b = int(os.environ["b"])
    ab = a*b
    print(a)
    print(b)
    print(ab)
    print("Affiche A * B : " +ab)
    
    print(f'log(ab) = {numpy.log(ab)}')
    print(f'log(a) + log(b) = {numpy.log(a) + numpy.log(b)}')
    

if __name__ == "__main__":
    main()

