def tryCatch(s):
    while True:
        try:
            userIn = float(input(s))
            break
        except:
            print("Error. Please enter a number.")
    
    return userIn

def risk():
    name = input("Enter file name: ")
    name = name + ".txt"
    
    while True:
        type = input("What file mode would you like to use? \n'a' adds to end of file \n'w' rewrites file content\n>> ")
        if type != 'a' and type != 'w':
            print("Error. Please enter 'a' or 'w'")
        else:
            break
    
    file = open(name, type)
    userIn = ""
    while True:
        userIn = input("Enter ticker: ")
        if userIn == "quit":
            break
        stock = userIn
        price = tryCatch("Enter the entry price: ")
        loss = tryCatch("Enter the stop loss: ")
        target = tryCatch("Enter the price target: ")
        
        down = (1-(loss/price))*100
        down = round(down, 2)
        
        up = ((target-price)/price)*100
        up = round(up, 2)
        
        risk = up/down
        risk = round(risk, 2)
        
        s = stock + " buy @ " + str(price) + ", target " + str(target) + ", stop loss @ " + str(loss) + ": DS %" + str(down) + ", US: %" + str(up) + ", RR: " + str(risk)
        file.write(s + "\n\n")
    
    file.close()
    
    
risk()


            
          
    
    
    