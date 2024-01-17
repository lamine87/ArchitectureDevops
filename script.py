import os
import numpy as numpy

def main(): 
    a = int(os.environ["a"])
    b = int(os.environ["b"])
    print(a)
    print(b)
    print("Affiche A * B : " (a*b))
    # valeurAB = float(os.environ["A"]) * float(os.environ["B"])
    # print("Affiche A * B : " + str(valeurAB))
    

if __name__ == "__main__":
    main()

