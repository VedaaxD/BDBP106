def wavelength(w):
    if w<380 or w>750:
        print("Enter a valid wavelength in the range of visible light.")
    if w in range(380,450) :
        print("The colour for the given wavelength is Violet.")
    if w in range(450,495) :
        print("The colour for the given wavelength is Blue.")
    if w in range(495,570):
        print("The colour for the given wavelength is Green.")
    if w in range(570,590):
        print("The colour for the given wavelength is Yellow.")
    if w in range(590,620):
        print("The colour for the given wavelength is Orange.")
    if w in range(620,751):
        print("The colour for the given wavelength is Red.")
def main():
    w=int(input("Enter the wavelength: "))
    wavelength(w)
if __name__=="__main__":
    main()