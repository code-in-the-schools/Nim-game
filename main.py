

def Start():
    a = str(input('Will you go first or second '))
    if a == 'first':
      print('Player 1 starts')  

total = 0

def Add(amount):
    t = 0
    b = str(input('enter 1 or 2 '))
    if b == '1':
      t += 1
      print(amount)
    if b == '2':
      t += 2
    
    amount += t
    print(amount)
    print('Player 2 turn')
    b = str(input('enter 1 or 2 '))
    if b == '1':
      t += 1
      print(amount)
    if b == '2':
      t += 2
    
    amount += t
    print(amount)
    print('Player 1 turn')
    

Start()

while total < 20:   

  Add(total) 
 
 
if total == 20:
     print('You Win!!!')


