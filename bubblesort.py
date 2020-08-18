#bubble Sort numbers from list
  
def bubbleSort(numbers): 
    n = len(numbers) 
  
    # Traverse through list
    for i in range(n-1): 
    # outer loop will repeat one time more than needed. 
  
        # Last elements are already in place 
        for j in range(0, n-i-1): 
  
            # Swap if the element found is greater 
            if numbers[j] > numbers[j+1] : 
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j] 
  
# list of numbers 
numbers = [345, 324, 85, 2, 64, 12, 34] 
  
bubbleSort(numbers) 
  
for i in range(len(numbers)): 
    print ("%d" %numbers[i])