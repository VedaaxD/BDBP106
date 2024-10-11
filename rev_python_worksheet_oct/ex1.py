from math import pi
def vol_of_cylinder(r,h):
    if r==0 or h==0 :
        print("Invalid input entered.")
    else :
        volume=pi*(r)**2*h
        return volume
def main():
    r=int(input("Enter the radius of the cylinder: "))
    h=int(input("Enter the height of the cylinder: "))
    volume=vol_of_cylinder(r,h)
    rounded_volume=round(volume,2)
    print("The volume of the cylinder is",rounded_volume,"cubic units.")
if __name__=="__main__":
    main()