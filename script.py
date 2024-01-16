import os

def main():
    valeurAB = float(os.environ["A"])*float(os.environ["B"])
    print("Affiche A * B : " + valeurAB)
     

if __name__ == "__main__":
    main()
