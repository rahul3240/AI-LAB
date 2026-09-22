def fact(n):
  factorial=1
  i=1
  while i<n+1:
    factorial=factorial*i
    i+=1
  return factorial

n=int(input("enter a number:"))
print("factorial of",n,"is",fact(n))
