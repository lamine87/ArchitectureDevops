import os
import numpy as np

def main(): 
    
    a = int(os.environ["a"])
    b = int(os.environ["b"])
    ab = a*b
    print(a)
    print(b)
    print(ab)
    print("Affiche A * B : " + str(ab))
    
    print(f'log(ab) = {np.log(ab)}')
    print(f'log(a) + log(b) = {np.log(a) + np.log(b)}')
    

if __name__ == "__main__":
    main()

