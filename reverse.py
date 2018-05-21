def reverse(text):
  result=""
  leng=len(text)-1
  for i in range (0,leng+1):
    result+=(text[leng-i])
  return result

print reverse("piyush atn")
