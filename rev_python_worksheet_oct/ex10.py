def replace_with_and(words):
    replaced=words.replace("," , " and ")
    print(replaced)
def main():
    words=input("Enter two words separated by comma: ")
    if words.count(',') != 1:
        print("Enter two words separated by comma.")
    else:
        replace_with_and(words)
if __name__=="__main__":
    main()