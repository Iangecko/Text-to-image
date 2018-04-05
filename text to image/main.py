from encode import encodeTxt
from decode import decodeIm
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


while True:
    clear()

    choice = input("## IAN'S TEXT TO IMAGE CONVERTER ##\n1. Encode text into an image\n2. Decode image into text\n3. Exit\n")

    clear()

    if choice == "1" or choice == "2" or choice == "3":
        if choice == "1":
            encodeTxt()
        elif choice == "2":
            decodeIm()
        elif choice == "3":
            print("exiting...")
            break
            
    else:
        print("not an option")
    input("\nPress enter to return to menu\n")
