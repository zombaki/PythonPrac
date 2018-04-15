def digit_sum(x):
  sum=0
  while x>0:
    sum+=x%10
    x=x//10
    print x,sum
    raw_input("Avoid Val")
  return sum

print digit_sum(123)
