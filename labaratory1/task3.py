print("Потапенко Іван Валентинович, КМ-92, Лабараторна робота №1, Завдання №3")
x = int(input("Please enter x:"))

if(x<=13):
    y=(-x)**3+9
    print("y = ", y)
elif(x>13):
    y=-3/(x+1)
    print("y = ", y)
else:
    print("Wrong value. Try again.")
input("Press any key to leave.")

