total = 0
def Start(i):
    a = str(input('Will you go first or second '))
    if i == 'first':
       Add(i)  
 
def Add(i):
    b = input('enter 1 or 2 ')
    if i == '1':
         return(1 + total)
    else:
             return(2 + total)
             
Start(i)


        
