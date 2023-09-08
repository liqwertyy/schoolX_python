arr = list(map(int, input(" введите массив чисел: ").split())) 

indexes = [] 
for i in range(1, len(arr)): 
    if arr[i] - arr[i-1] > 1:  
        indexes.append(i) 
    
if len(indexes) == 0:  
    print("Не найдено")  
else:  
    print(indexes)  
