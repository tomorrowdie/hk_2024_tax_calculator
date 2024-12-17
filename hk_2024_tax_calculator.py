#######################################
# Program name: Tax calculator
# Purpose: This program is to calculate Hong Kong Tax
# Input: Income, Marriage, no of children
# Output: tax amount
# Author: John @ Angry Factory
# Date: 7 Nov 2024
# Version: 1.0 --- 7 Nov 2024
#########################################

ALLOWANCE = 132_000
CHILD_ALLOWANCE = 130_000

L1_LIMIT = 50_000 # first level of the tax boundary
L1_RATE = 0.02
L1_TAX = 1_000
L2_LIMIT = 100_000
L2_RATE = 0.06
L2_TAX = 3_000
L3_LIMIT = 150_000
L3_RATE = 0.10
L3_TAX = 5_000
L4_LIMIT = 200_000
L4_RATE = 0.14
L4_TAX = 7_000
L5_RATE = 0.17

TOP_RATE = 0.15

# input the income and marriage
income = float(input('What is your total income? '))
married = input('Are you married?')

# calculate the taxable
if married == 'N':
    taxable = income - ALLOWANCE*2
else:
    taxable = income - ALLOWANCE

# deduct the taxable for children
number_of_children = int(input('no of children? '))
taxable = taxable - number_of_children * CHILD_ALLOWANCE

if taxable < 0:
    print('No need to pay tax') # no tax because income < taxxable
    tax = 0
elif taxable <= L1_LIMIT:
    tax = taxable * L1_RATE
elif taxable <= L2_LIMIT:
    charging_tax = taxable - L1_LIMIT
    tax = L1_TAX + charging_tax * L2_RATE
elif taxable <= L3_LIMIT:
    charging_tax = taxable - L2_LIMIT
    tax = L1_TAX + L2_TAX+ charging_tax * L3_RATE
elif taxable <= L4_LIMIT:
    charging_tax = taxable - L3_LIMIT
    tax = L1_TAX + L2_TAX+ L3_TAX + charging_tax * L4_RATE
else:
    charging_tax = taxable - L4_LIMIT
    tax = L1_TAX + L2_TAX+ L3_TAX + L4_TAX + charging_tax * L5_RATE

top_tax = income * TOP_RATE
if tax > top_tax:
    tax = top_tax
print('Your tax amount is :', tax)