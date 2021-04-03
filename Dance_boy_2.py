### dance boy 2
import time

state = 0

dance_style = input("Please choose a dance stle, 1, 2 or 3: ")

while state < 4:
    if dance_style == "1":

        print (" 0")
        print("/|\\")
        print(" /\ \n")
    
        time.sleep(0.3)
        
        print (" 0")
        print("<|>")
        print(" /\ \n")
        
        time.sleep(0.3)
        
        print ("\\0")
        print(" |>")
        print(" /\ \n")
        
        time.sleep(0.3)
        
        print ("\\0/")
        print(" |")
        print(" /\ \n")
        
        time.sleep(0.3)
        state = state + 1
    
    elif dance_style == "2":
        print("<0>")
        print(" |")
        print("/\ \n")

        time.sleep(0.3)

        print(" 0")
        print("<|>")
        print("/\ \n")

        time.sleep(0.3)

        print("<0>")
        print(" |")
        print("/\ \n")

        time.sleep(0.3)

        print(" 0")
        print("<|>")
        print("/\ \n")

        time.sleep(0.3)
        state = state + 1
        
    elif dance_style == "3":
        print(" 0")
        print("/|\\")
        print("<\ \n")

        time.sleep(0.3)
        
        print(" 0")
        print("<|>")
        print("/> \n")

        time.sleep(0.3)

        print(" 0>")
        print("/|")
        print("<\ \n")

        time.sleep(0.3)

        print(" 0")
        print("<|>")
        print("/> \n")

        time.sleep(0.3)
        state = state + 1

    else:
        print("Thanks for trying to break this!")
        time.sleep(4)
        state = state + 5
