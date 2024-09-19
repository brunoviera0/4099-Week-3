#import pandas library
import numpy as np

#customer details
name = input("Name: ")
address = input("Address: ")

#data in numpy (np) arrays
items = np.array(['Plates', 'Cups'])
prices = np.array([2, 4])

#quantities
num_plates = int(input("How many plates? "))
num_cups = int(input("How many cups? "))

#store quantities in a numpy array
quantities = np.array([num_plates, num_cups])

#calculate total for each item and overall total
totals = prices * quantities
total_cost = np.sum(totals)

#results
print("\nCustomer Information:")
print(f"Name: {name}")
print(f"Address: {address}")

print("\nInvoice:")
for i, item in enumerate(items): #iterate through numpy array to print result
    print(f"{item}: Quantity = {quantities[i]}, Unit Price = ${prices[i]}, Total = ${totals[i]}")

print(f"\nTotal Amount Due: ${total_cost}")

