import random

def swg(comp,mine):
    if(comp == 's' and mine == 'g'):
        return 1
    elif(comp == 'w' and mine == 's'):
        return 1
    elif(comp == 'g' and mine == 'w'):
        return 1
    elif(comp==mine):
        return -1
    else:
        return 0 


choice = ('s','w','g')
comp = random.randint(0,2)
comp = choice[comp]
mine = input('choose s, w, g: ')
print(f"comp chose: {comp}")
win = swg(comp,mine)

if (win == 1):
    print("You Win")
elif(win == -1):
    print("Draw")  
else:
    print("You loss")    
