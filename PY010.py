# python program to callculate GST
# GST for gold is 3%
from datetime import date
today = date.today()

gram = float(input("enter total gold is gram::: "))
goldprice = int(input(f'Enter gold rate per gram as on {today}::  '))

totalprice = gram*goldprice
print(f'Total price for gold{totalprice}')
gst = (totalprice/100)*3
print(f'GST for {totalprice} is : {gst}')
grandtotal = totalprice + gst
print(f'total ammount :{grandtotal}')