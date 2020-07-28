total = 0
def Start():
    a = str(input('Will you go first or second '))
    if a == 'first':
       print('Player 1 starts')  
 
def Add():
    b = input('enter 1 or 2 ')
    if b == '1':
        total + 1
        print(total)
        if b == '2':
             return(total.append(2))
             print(total)
             print('Player 2 turn')
Start()
while total != 20:             
 Add()


        
