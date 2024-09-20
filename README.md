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





#validations 
using HTML and Flask:

Project: Address and Password Validator
This project provides an address and password validation system using Flask and client-side JavaScript validation. The application gives HTML forms to the user and validates the input using Javascript before submitting the form. if requirements are met the validated data is then returned and displayed on the same form page.

Files Included:
main.py: This is the main Flask application that handles the routing and rendering of HTML forms.
address.html: This file contains the address input form and the JavaScript validation for addresses.
password.html: This file contains the password input form and the JavaScript validation for passwords.
Requirements:
requirements.txt:



This file defines the runtime environment for the Google App Engine, specifying that the application uses Python 3.9.

Folder Structure:
app.yaml
main.py
requirements.txt
└── templates
    address.html
    password.html
    
How to Run:
Set Up Environment:

Ensure you have the necessary files:
Authenticate your Google Cloud account:

Run the following commands:
$gcloud app create
$gcloud auth login

After authenticating and selecting the region, deploy the app:
$gcloud app deploy

Once deployed, you can access the app by running:
$gcloud app browse
This will provide a URL similar to: https://cs-course-app.ue.r.appspot.com/

Validate Address and Password:

Visit the URL and enter an address on the first page to validate.

/passwords endpoint:
Enter a password by visiting the /password endpoint to validate a password.


if requirements are not met:
  the screen will prompt you with requirements

if requirements are met:
  screen will give a successful message in greeen.
