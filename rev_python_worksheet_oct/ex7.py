def get_square_and_cube(a):
    if a == 0 :
        print("Enter integers.")
    else:
        square=a**2
        cube=a**3
        print("The square and cube of the number",a,"is",square,"and",cube,"respectively")
def main():
    a=int(input("Enter a number: "))
    get_square_and_cube(a)
if __name__=="__main__":
    main()