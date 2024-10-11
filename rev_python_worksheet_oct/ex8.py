def article(n):
    vowels=['a','e','i','o','u']
    first_char=n[0].lower()
    if first_char in vowels :
        print("The article for the corresponding noun is 'an'.")
    else :
        print("The article for the corresponding noun is 'a'.")
def main():
    vowels = []
    n=str(input("Enter a noun: ")).strip()
    if n=="":
        print("Enter a valid noun.")
    else :
        article(n)
if __name__=="__main__":
    main()