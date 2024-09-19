#import pandas library
import pandas as pd

#invoice data
data = {
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'Alice'],
    'Amount': [50, 30, 20, 40],
    'Status': ['Paid', 'Unpaid', 'Paid', 'Unpaid']
}

#create a data frame
df = pd.DataFrame(data)

#find the total invoice amount
total_amount = df['Amount'].sum()
print(f'Total Invoice Amount: ${total_amount}')

#find the average invoice amount
average_amount = df['Amount'].mean()
print(f'Average Invoice Amount: ${average_amount:.2f}')

#unpaid invoices
unpaid_invoices = df[df['Status'] == 'Unpaid']
print('Unpaid Invoices:')
print(unpaid_invoices)
