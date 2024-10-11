from math import sqrt
def hypotenuse(s1,s2):
    if s1 == 0 or s2 == 0:
        print("Enter a valid input.")
    else :
        length_of_hypotenuse=sqrt(s1**2+s2**2)
        return length_of_hypotenuse
def main():
    s1=int(input("Enter the side 1 of a triangle: "))
    s2=int(input("Enter the side 2 of a triangle: "))
    length_of_hypotenuse=hypotenuse(s1,s2)
    print("The length of the hypotenuse of the traingle is",length_of_hypotenuse,"units")
if __name__=="__main__":
    main()