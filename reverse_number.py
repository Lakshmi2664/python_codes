num =int(input())
rev = 0
while n>0:
  digit = n%10
  rev = rev*10+digit
  num //=10
print(rev)
