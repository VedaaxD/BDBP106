def check_triangle(a,b,c):
    if a+b < c and b+c < a and c+a < b :
        print("Triangle cannot be formed with the sides",a,b,c)
    else :
        print("Triangle can be formed with the sides",a,b,c)
def main():
    a=int(input("Enter the first side of the triangle: "))
    b=int(input("Enter the second side of the triangle: "))
    c=int(input("Enter the third side of the triangle: "))
    if a<=0 or b<=0 or c<=0 :
        print("Enter valid positive integers for the sides.")
    else:
        check_triangle(a,b,c)
if __name__=="__main__":
    main()