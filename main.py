def Start():
    a = str(input('Will you go first or second '))
    if a == 'first':
       print('Player 1 starts')  
total = 0
def Add():
    total = 0
    b = int(input('enter 1 or 2 '))
    if b == '1':
        total += 1
        print(total)
    if b == '2':
        total += 2
    print(total)
    print('Player 2 turn')
    b = int(input('enter 1 or 2 '))
    if b == '1':
        total += 1
        print(total)
    if b == '2':
     total += 2
    print(total)
    print('Player 1 turn')
Start()
while total != 20:             
 Add()


        
