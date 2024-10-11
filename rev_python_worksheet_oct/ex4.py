def check_prime(n):
    if n==0 or n==1:
        print("The number is neither prime nor composite.")
    if n<0:
        print("You can only enter only positive integers.")
    if n==2 :
        print("Two is the only even prime number.")
    if n>2 :
        for i in range(2,n):
            if n % i == 0 :
                print("The number",n, " is a composite number")
                return
        else :
            print("The number", n, "is a prime number.")
def main():
    n=int(input("Enter a number: "))
    check_prime(n)
if __name__=="__main__":
    main()