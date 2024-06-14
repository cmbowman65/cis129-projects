# cis129_lab03_coffeeShop.py

"""
Created on Thu Jun 13 15:17:34 2024

@author: Cliff Bowman

Provide a receipt for items purchased
"""

coffee = int(input('Enter the number of coffees purchased:  '))
muffin = int(input('Enter the number of muffins purchased:  '))
bagel = int(input('Enter the number of bagels purchased:  '))
danish = int(input('Enter the number of danishes purchased:  '))

coffee_tot = coffee * 5.00
muffin_tot = muffin * 4.00
bagel_tot = bagel * 2.00
danish_tot = danish * 2.50
tax = ((coffee_tot + muffin_tot + bagel_tot + danish_tot) * 6) / 100
total = (((tax + coffee_tot + muffin_tot + bagel_tot + danish_tot)  * 100) // 1) / 100

print('\n') #blank line between input and results

print('****************************************\
      \nK & C Coffee and Muffin Shop\
      \nNumber of coffees bought?\n', coffee)

print('Number of muffins bought?\n', muffin
print('Number of bagels bought?\n', bagel

print('Number of danishes bought?\n', danish, '\
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

"""printing "bagel" or "bagels" on the receipt"""
if bagel == 1:
    print(bagel, 'Bagel at $2 each:  $', bagel_tot)  
if bagel > 1:
    print(bagel, 'Bagels at $2 each:  $', bagel_tot) #make bagels plural

"""printing "danish" or "danishes" on the receipt"""
if danish == 1:
    print (danish, 'Danish at $2.50 each:  $', danish_tot)    
if danish > 1:
    print(danish, 'Danishes at $2.50 each:  $', danish_tot) #make danishes plural
    
print('6% tax:  $', tax)
print('---------')
print('Total:  $', total, '\
      \n*****************************************')

print('\nWe greatly appreciate your business.')
print('\n        Come Back Soon!')
      
      
