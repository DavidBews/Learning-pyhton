### dancey boy 3 

import time

dance_cycle = 0
dance_style = input("Please choose a dance style, 1, 2 or 3: ")

dance1_1 = " 0 \n<|>\n /\ \n"
dance1_2 = "\r <0>\n  |\n /> \n"

dance2_1 = " 0/ \n <|\n /> \n"
dance2_2 = "\\0 \n |>\n <\ \n"

dance3_1 = " \\0> \n  |\n /\ \n"
dance3_2 = " <0/ \n  |\n /\ \n"

while dance_cycle <  5:
    if dance_style == "1":
        print(dance1_1)
        time.sleep(0.5)
        print(dance1_2)
        time.sleep(0.5)
        
    elif dance_style == "2":
        print(dance2_1)
        time.sleep(0.5)
        print(dance2_2)
        time.sleep(0.5)
    
    elif dance_style == "3":
        print(dance3_1)
        time.sleep(0.5)
        print(dance3_2)
        time.sleep(0.5)
    
    else:
        print("Thanks for trying to break dancey boy 3! No dance for you")
        time.sleep(5)
        dance_cycle = dance_cycle + 10
    dance_cycle = dance_cycle + 1

