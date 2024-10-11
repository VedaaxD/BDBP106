def find_median(a,b,c):
    num_list=[a,b,c]
    num_list.sort()
    median=num_list[1]
    return median
def main():
    a=int(input("Enter the 1st number: "))
    b=int(input("Enter the 2nd number: "))
    c=int(input("Enter the 3rd number: "))
    median=find_median(a,b,c)
    print("The median of the given numbers are",median)
if __name__ == "__main__":
        main()