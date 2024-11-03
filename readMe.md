This is a web-based application for a machine learning model that is used to predict the probability of a patient having a heart disease.

I started by creating a virtual environment and installed the libraries I wanted(they can be found in the requirements.txt file)and then imported the installed libraries 

I loaded the data using the pandas library.
I analyzed my data by getting the first and last rows of the dataset and getting the summary statistics

I went on to process my data by checking for handling missing values and removing duplicates from the dataset.
I then encoded the columns that needed encoding to have a uniform range.
some values need stardandizing and I did so to prevent some features from influencing the predictions

I used four models which I train and evaluated based on their accuracy score and then I chose the best model for deployment.

In deployment I used streamlit which is a simple python web framework for this kind of project


How to run this application locally. The instructions are for the zipped folder

step1: Prerequisites
Ensure you have Python installed on your machine
Install pip, which usually comes with Python.

Download the App

Download the zipped folder containing the app files.
Extract the contents of the zipped folder to a location on your computer.
Navigate to the App Directory
Open your terminal or command prompt and type cd path\to\extracted\folder

Create a virtual environment (this is optional but recommended to keep dependencies isolated)
use command python -m venv myvenv for windows( on mac you use python3 -m venv myvenv)
Activate the virtual environment using (myvenv\Scripts\activate on windows and source myvenv/bin/activate on macOS/Linux)

Install Dependencies
run the command (pip install -r requirements.txt)

Run the app
use command (streamlit run main.py)

Your default browser will open a web page for you displaying FeytiCare, our amazing app.
