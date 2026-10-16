def toolkit():
    
    
    
    print("===EE TOOLKIT===\n")
    print("Electrical Calculations\n")
    
    
    while True:
    
        text = input("Calculate?: V, I, R, W, kWh (or quit)\n")
    
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
            
        elif text.upper() == "W":
            print("Calculating Power:\n")
            power()
            break
        elif text.upper() == "KWH":
            print("Calculating Electrical Energy:\n")
            energy()
            break
            
        else:
            print("Enter V, I, R, W, kWh or quit only")
  
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
        
def power():
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
      
            p1 = v * i
            print("Power:",p1,"W")
            break          
            
        except ValueError:
            print("That is not a number, try again.")
        continue
        
    while True:
            
        e = input("Calculate energy, Continue, Main menu or Quit?\n")
        if e.lower() == "continue":
            print("Calculating Power:\n")
            power()
            return
        elif e.lower() == "main menu":
            toolkit()
            return
        elif e.lower() == "quit":
            print("Stopped Successfully")
            return
        elif e.lower() == "calculate energy":
            energy1(p1)
            return p1
        else:
            print("Please choose between the four")
            continue
            
def energy1(p1):
    print("Calculating Electrical Energy:\n")
    while True:
        
        p = float(p1)
        h1 = input("Enter total hours: ")
        
        try:
            h1 = float(h1)
            print(h1)
        
            if h1 < 0:
                print("Hours cannot be in negative")
                continue
            
            kwh = (p / 1000) * h1
            print("Energy:",kwh,"kWh")
            break
            
        except ValueError:
            print("That is not a number, try again.")
            continue
        
    while True:
            
        e = input("Continue, Main menu or Quit?\n")
        if e.lower() == "continue":
            print("Calculating Electrical Energy:\n")
            energy()
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

def energy():
    
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
       
            p = v * i
            print("Power:",p,"W")
            break          
            
        except ValueError:
            print("That is not a number, try again.")
        continue
        
    while True:
    
        h = input("Enter total hours: ")
        
        try:
            h = float(h)
            print(h)
       
            if h < 0:
                print("Time can't be a negative number")
                continue
            kwh = (p / 1000) * h
            print("Electrical Energy:",kwh,"kWh")
            break          
            
        except ValueError:
            print("That is not a number, try again.")
        continue
        
    while True:
            
        e = input("Continue, Main menu or Quit?\n")
        if e.lower() == "continue":
            print("Calculating Electrical Energy:\n")
            energy()
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