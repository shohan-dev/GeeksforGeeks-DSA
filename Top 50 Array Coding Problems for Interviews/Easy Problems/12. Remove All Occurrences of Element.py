def removeElement(arr, ele):
  
    count =0
    for i in arr:
        if i==ele:
            continue
        count +=1          
                
    return count
  
if __name__ == "__main__":
    arr = [0, 1, 3, 0, 2, 2, 4, 2]
    ele = 2
    print(removeElement(arr, ele))