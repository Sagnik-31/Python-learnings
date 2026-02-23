 # format specifiers = {value:flags} format a value based on what flags are inserted.

price1 = 23133.34455
price2 = 23421.65767
price3 = 57397.87009

print(f"Price 1 is ${price1:+,.2f}")
print(f"Price 2 is ${price2:20}") # padding
print(f"price 1 is ${price1:<20}") # left justified
print(f"price 1 is ${price1:>20}") # right justified
print(f"price 1 is ${price1:^20}") # center aligned

