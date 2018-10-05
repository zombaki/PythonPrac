def f(v, i, S):
  if i >= len(v):
      if S == 0:
          return 1
      else:
        return 0
  count = f(v, i + 1, S)
  count += f(v, i + 1, S - v[i])
  return count

v = [1, 2, 3, 8, 10]
sum = 7
print(f(v, 0, sum))
