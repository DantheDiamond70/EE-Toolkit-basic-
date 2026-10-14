def toolkit():
    
    
    
    print("===EE TOOLKIT===\n")
    print("Ohm's Law\n")
    
    
    while True:
    
        text = input("Calculate?: V, I, R (or quit)\n")
    
        if text.lower() == "quit":
            print("Stopped Successfully")
            return
           
        elif text.upper() == "V":
            print("Calculating Voltage:\n")
            Voltage()
            break
            
        elif text.upper() == "I":
            print("Calculating Ampere:\n")
            Current()
            break
            
        elif text.upper() == "R":
            print("Calculating Resistance:\n")
            Resistance()
            break
            
        else:
            print("Enter V, I, R or quit only")
  
def Voltage():
       
    while True:
        
        i = input("Enter amount of Current (or quit): ")
        
        if i.lower() == "quit":
           print("Stopped Successfully")
           return
      
        try:
            i = float(i)
            print(i)
            break
            
        except ValueError:
            print("That is not a number, try again.")
        continue
           
    while True:
    
        r = input("enter amount of Resistance: ")
        
        try:
            r = float(r)
            print(r)
       
            if r < 0:
                print("Resistance can't be in negative")
                continue
            
            v = i * r
            print("voltage:",v,"V")
            break
           
        except ValueError:
            print("That is not a number, try again.")
        continue
    
    while True:
            
        e = input("Continue, Main menu or Quit?\n")
        if e.lower() == "continue":
            print("Calculating Voltage:\n")
            Voltage()
            return
        elif e.lower() == "main menu":
            toolkit()
            return
        elif e.lower() == "quit":
            print("Stopped Successfully")
            return
        else:
            print("Please choose between the three")
            continue
        
        
def Current():
    while True:
     
        v = input("Enter amount of Voltage (or quit): ")
            
        if v.lower() == "quit":
            print("Stopped Successfully")
            return
                
            
        try:
            v = float(v)
            print(v)
            break
        except ValueError:
           print("That is not a number, try again.")
        continue
           
           
    while True:
    
        r = input("Enter amount of Resistance: ")
        
        try:
            r = float(r)
            print(r)
            
       
            if r < 0:
                    print("Resistance can't be in negative")
                    continue
            elif r == 0:
                    print("Cannot be divided by zero")
                    continue
            i = v / r
            print("Current:",i,"A")
            break
         
         
        except ValueError:
            print("That is not a number, try again.")
        continue
        
            
    while True:
            
        e = input("Continue, Main menu or Quit?\n")
        if e.lower() == "continue":
            print("Calculating Current:\n")
            Current()
            return
        elif e.lower() == "main menu":
            toolkit()
            return
        elif e.lower() == "quit":
            print("Stopped Successfully")
            return
        else:
            print("Please choose between the three")
            continue
        
        
def Resistance():
    while True:
     
        v = input("Enter amount of Voltage (or quit): ")
        
        if v.lower() == "quit":
            print("Stopped Successfully")
            return
            
            
        try:
            v = float(v)
            print(v)
            break
        except ValueError:
           print("That is not a number, try again.")
        continue
        
    while True:
    
        i = input("Enter amount of Current: ")
        
        try:
            i = float(i)
            print(i)
       
            if i == 0:
                 print("Cannot be divided by zero")
                 continue
            elif i < 0:
                print("Current can't be a negative number")
                continue
            r = v / i
            print("Resistance:",r,"Ω")
            break          
            
        except ValueError:
            print("That is not a number, try again.")
        continue
      
    while True:
            
        e = input("Continue, Main menu or Quit?\n")
        if e.lower() == "continue":
            print("Calculating Resistance:\n")
            Resistance()
            return
        elif e.lower() == "main menu":
            toolkit()
            return
        elif e.lower() == "quit":
            print("Stopped Successfully")
            return
        else:
            print("Please choose between the three")
            continue
        
toolkit()