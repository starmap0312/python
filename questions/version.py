# Compare two Version numbers (return latest version)

def compare(v1, v2):

    arr1 = [int(i) for i in v1.split(".")]
    arr2 = [int(i) for i in v2.split(".")]
    n1 = len(arr1)
    n2 = len(arr2)
 
    if n1 > n2:
      for i in range(n2, n1):
         arr2.append(0)
    elif n2 > n1:
      for i in range(n1, n2):
         arr1.append(0)
    
    for i in range(len(arr1)):
      if arr1[i] > arr2[i]:
         return v1
      elif arr2[i] > arr1[i]:
         return v2
    return v1

print(compare("1.0.31", "1.0.27")) # "1.0.31"
print(compare("1.0.31", "1.1")) # "1.1"
print(compare("1.01", "1.02")) # "1.02"
