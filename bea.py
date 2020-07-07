n=int(input())
x=int(input())
result=1
while n>0:
    if n&1:
      res*=x
    x*=x
    n=>>n
print(res)
