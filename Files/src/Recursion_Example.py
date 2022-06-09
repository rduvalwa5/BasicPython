'''
Created on Jun 2, 2022

https://www.w3schools.com/python/gloss_python_function_recursion.asp
'''

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)