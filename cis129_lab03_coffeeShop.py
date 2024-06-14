# -*- coding: utf-8 -*-

# cis129_lab03_coffeeShop.py

"""
Created on Thu Jun 13 15:17:34 2024

@author: Cliff Bowman

Provide a receipt for coffee and muffins purchased
"""

coffee = int(input('Enter the number of coffees purchased:  '))
muffin = int(input('Enter the number of muffins purchased:  '))

coffee_tot = coffee * 5.00
muffin_tot = muffin * 4.00
tax = ((coffee_tot + muffin_tot) * 6) / 100
total = (((tax + coffee_tot + muffin_tot)  * 100) // 1) / 100

print('\n') #blank line between input and results

print('****************************************\
      \nMy Coffee and Muffin Shop\
      \nNumber of coffees bought?\n', coffee)

print('Number of muffins bought?\n', muffin, '\
      \n****************************************')

print('\n\n')

print('*****************************************')

"""printing "coffee" or "coffees" on the receipt"""
if coffee == 1:
    print(coffee, 'Coffee at $5 each:  $', coffee_tot)  
if coffee > 1:
    print(coffee, 'Coffees at $5 each:  $', coffee_tot) #make coffees plural

"""printing "muffin" or "muffins" on the receipt"""
if muffin == 1:
    print (muffin, 'Muffin at $4 each:  $', muffin_tot)    
if muffin > 1:
    print(muffin, 'Muffins at $4 each:  $', muffin_tot) #make muffins plural
    
print('6% tax:  $', tax)
print('---------')
print('Total:  $', total, '\
      \n*****************************************')
      
      