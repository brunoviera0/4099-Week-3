CSE-4099 Week3 (GitHub Primer, Python, and Validation)

GitHub Tutorial:
This will serve as a quick user guide to using a GitHub repository.

A GitHub repository is a storage space where your project's files are in one centralized location, allowing you to manage and share code with collaborators. 

The following are the essential git commands you must know to be able to utilize a repository:

git init: create a repository in the current directory

git clone <url>: downloads a repository from an outside source onto your machine

git add <file>: stages changes to be made, specific file

git add .: stages changes to be made, everything

git commit -m "Message": Record changes made

git push origin <branch>: moves your changes onto a branch in the repo, main is the default

git pull origin <branch>: merges changes made to the branch into your current workspace, main for default


Python Examples:

Numpy & Pandas Example- The library pandas is useful because it allows for the handling and manipulation of tabular data. Pandas will enable you to store data in a structured format using DataFrames. With Pandas, you can quickly perform operations on your data, such as addition, multiplication, or filtering.

Numpy is another library very similar to pandas, allowing for efficient data manipulation as well but its main use case involves multi-dimensional arrays and vectorized operations, which are faster and more efficient than using standard Python loops.

First write a Python program "pandas_example.py" that uses the pandas library to manage a dataset of items, including prices and the quantities purchased by a customer. Your program should prompt the user for their name and address, along with the number of plates and cups they wish to purchase. Store the item prices and quantities in a pandas DataFrame, and display a summary of the customer's purchase, including the total due. Lastly, repeat the same process, this time writing the program "numpy_example.py", solving the same prompt using the numpy library, store your data in numpy arrays instead of a pandas DataFrame.

Matplotlab-
