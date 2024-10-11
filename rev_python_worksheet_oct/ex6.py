# from itertools import product
def num_operations(a,b):
    if b==0 :
        print("Enter valid numbers.")
    else :
        sum=a+b
        print("The sum of the numbers is",sum)
        product=a*b
        print("The product of the numbers is",product)
        difference=a-b
        print("The difference of the numbers is", difference)
        quotient=a/b
        print("The quotient of the numbers is",round(quotient,2))
        remainder=a%b
        print("The remainder of the numbers is",remainder)
def main():
    a=int(input("Enter any number a : "))
    b=int(input("Enter any number b : "))
    num_operations(a,b)
if __name__=="__main__":
    main()