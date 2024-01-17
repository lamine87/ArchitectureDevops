import os
import numpy as numpy

def main(): 
    a = float(os.environ["MYVAR1"])
    b= float(os.environ["MYVAR"])
    print("Affiche A * B : " (a*b))
    # valeurAB = float(os.environ["A"]) * float(os.environ["B"])
    # print("Affiche A * B : " + str(valeurAB))
    

if __name__ == "__main__":
    main()

