#importing python scripts
import part1
import part2
import part3



menu_open = ""
close = ""


def menu():
    global menu_open, close
    while True:
        print("\n")
        try:
            menu_open = input("Enter '1' to Open Student Version: \n"
                              "Enter '2' to Open Staff Version with the Horizontal Histogram: \n"
                              "Enter '3' to Open Staff Version with the Vertical Histogram: \n"
                              "Enter 'q' to Quit: ")
        except ValueError:
            print("Please Enter '1' '2' '3' or 'q'")
        else:
            if menu_open == "q":
                print("'q' Pressed, Quit Programme")
                quit()
            elif menu_open == "1":                   #The student version
                print("-" * 70)
                print("Student Version \n")
                part1.validation()
                print("-" * 70)
            elif menu_open == "2":                              #Staff Version with the Horizontal Histogram
                print("-" * 70)
                print("Staff Version with the Horizontal Histogram \n")

                while True:
                    part2.validation()
                    close = part2.run_again()

                    if close == 'q':
                        break

                print("-" * 70)
            elif menu_open == "3":                             #Staff Version with the Vertical Histogram
                print("-" * 70)
                print("Staff Version with the Vertical Histogram \n")

                while True:
                    part3.validation()
                    close = part3.run_again()

                    if close == 'q':
                        break

                print("-" * 70)
          
            
            else:
                print("Please Enter '1' '2' '3' or 'q'")


menu()
