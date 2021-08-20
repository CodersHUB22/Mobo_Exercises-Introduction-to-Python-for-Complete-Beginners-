from mod4 import*                       

input = str(input("1.Circle \n2.Rectangle \n3.Triangle \nChoose your question: "))

if input == "1":
    Circle()
elif input == "2":
    Rectangle()
elif input == "3":
    Triangle()
else:
    print("Invalid Input. Terminating Program")
    
        