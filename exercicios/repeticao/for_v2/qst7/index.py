n = int(input("Digite o valor de n: "))

for i in range(2, n):  
    primo = True     
    for j in range(2, i):  
        if i % j == 0:     
            primo = False
            break        
    if primo:          
        print(i)