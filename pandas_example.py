#import pandas library
import pandas as pd

#customer details
name = input("Name: ")
address = input("Address: ")

#item data, name and price
data = {
    'Item': ['Plates', 'Cups'],
    'Price': [2, 4]
}
df = pd.DataFrame(data) #dataframe

#quantities
num_plates = int(input("How many plates? "))
num_cups = int(input("How many cups? "))

#add quantities to the DataFrame
df['Quantity'] = [num_plates, num_cups]

#calculate total for each item and overall total
df['Total'] = df['Price'] * df['Quantity']
total_cost = df['Total'].sum()

#results
print(f"\n{name}\n{address}")
print(df[['Item', 'Quantity', 'Total']])
print(f"Amount Due = ${total_cost}")
