# cis129_lab03_coffeeShop.py

"""
Created on Thu Jun 13 15:17:34 2024

@author: Cliff Bowman

Provide a receipt for items purchased
"""

"""Input values"""
coffee = int(input('Enter the number of coffees purchased:  '))
muffin = int(input('Enter the number of muffins purchased:  '))
bagel = int(input('Enter the number of bagels purchased:  '))
danish = int(input('Enter the number of danishes purchased:  '))

"""Tallying totals for each item at current prices"""
coffee_tot = coffee * 5.00
muffin_tot = muffin * 4.00
bagel_tot = bagel * 2.00
danish_tot = danish * 2.50

"""Deteermining the tax"""
tax = ((coffee_tot + muffin_tot + bagel_tot + danish_tot) * 6) / 100

"""The following snipet seems more complicated than it should be.  I had multiple rounding
problems in my test runs, e.g. total displaying as $21.1900000000001.  I am sure a more proper way
exists, but I muliplied the total by 100 to move the decimal to the right two places, floor
divided by 1 to remove the extra digits, then divided by 100 to move the decimal back to the left."""

total = (((tax + coffee_tot + muffin_tot + bagel_tot + danish_tot)  * 100) // 1) / 100

"""printing the number of items purchased"""
print('\n') #blank line between input and results

print('****************************************\
      \nK & C Coffee and Muffin Shop\
      \nNumber of coffees bought?\n', coffee)
print('Number of muffins bought?\n', muffin)
print('Number of bagels bought?\n', bagel)
print('Number of danishes bought?\n', danish, '\
      \n****************************************')

print('\n\n')

"""putting together the receipt for printing"""
print('*****************************************')

"""printing "coffee" or "coffees" on the receipt"""
if coffee == 1:
    print(coffee, 'Coffee at $5 each:  $', coffee_tot)  
elif coffee > 1:
    print(coffee, 'Coffees at $5 each:  $', coffee_tot) #make coffees plural

"""printing "muffin" or "muffins" on the receipt"""
if muffin == 1:
    print(muffin, 'Muffin at $4 each:  $', muffin_tot)    
elif muffin > 1:
    print(muffin, 'Muffins at $4 each:  $', muffin_tot) #make muffins plural

"""printing "bagel" or "bagels" on the receipt"""
if bagel == 1:
    print(bagel, 'Bagel at $2 each:  $', bagel_tot)  
elif bagel > 1:
    print(bagel, 'Bagels at $2 each:  $', bagel_tot) #make bagels plural

"""printing "danish" or "danishes" on the receipt"""
if danish == 1:
    print(danish, 'Danish at $2.50 each:  $', danish_tot)    
elif danish > 1:
    print(danish, 'Danishes at $2.50 each:  $', danish_tot) #make danishes plural
    
print('6% tax:  $', tax)
print('---------')
print('Total:  $', total, '\
      \n*****************************************')

print('\nK & C greatly appreciates your business.')
print('\n          Come Again Soon!')
      
      
