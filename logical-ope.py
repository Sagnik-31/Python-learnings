'''
or = atleast one condition must be true
and = both conditions must be true
not = inverts the condition (not false, not true)
'''
temp = 20
sunny = True

if temp <= 0 or temp >= 30:
  print("temperature is bad")
else:
  print("temperature is good")

if not sunny:
    print("it is sunny outside")
else:
 print("it is cloudy outside")
