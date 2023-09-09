print('''Press 1 to start
Press anything to stop''')
x=int(input("Enter your choice :"))
stk=[]
top=-1
while x==1:
    print('''Press 1 to insert
Press 2 to delete
Press 3 to display
Press 4 to exit''')
    y=int(input("Enter your operation :"))
    if(y==1):
        if(top==4):
            print("\n\nStack is overflowing\n\n")
            break
        e=int(input("Enter the thing you want to add:"))
        stk.append(e)
        top=top+1
    elif(y==2):
        if(top==-1):
            print("\n\n\nStack is empty\n\n\n")
        else:
            stk.remove(e)
            top=top-1
    elif(y==3):
        if(top==-1):
            print("\n\nStack is empty\n\n")
            break
        else:
            print(stk)
    elif(y==4):
        break
    else:
        print("Wrong input")
