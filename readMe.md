This is a web-based application for a machine laerning model that is used to predict the
probability of a patient having a heart disease.

I started by creating a virtual environment and installed the libraries I wanted(they can be found in the requirements.txt file)and then imported the installed libraries 

I loaded the data using the pandas library.
I analyzed my data by getting the first and last rows of the dataset and getting the summary statistics

I went on to process my data by checking for handling missing values and removing duplicates from the dataset.
I then encoded the columns that needed encoding to have a uniform range.
some values need stardandizing and I did so to prevent some features from influencing the predictions

I used four models which I train and evaluated based on their accuracy score and then I chose the best model for deployment.

In deployment I used streamlit which a simple python web framework for this kind of project.

I tested this app using 3 test cases and they were all positive.
Test1, data=[45,1,3,110,264,0,1,132,0,1.2,1,0,3] the target result was 0 and the predicted result was also 0 hence returning the statement for negative chance
Test2, data=[41,0,1,130,204,0,0,172,0,1.4,2,0,2]the target result was 0 and the predicted result was also 0 hence returning the statement for negative chance
Test3, data=[52,1,0,125,212,0,1,168,0,1.0,2,2,3] the target result was 0 and the predicted result was also 0 hence returning the statement for negative chance


How to run this application locally. The instructions are for the zipped folder

step1: Prerequisites
Ensure you have Python installed on your machine (version 3.12 or later).
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

Your default browser will open a web page for you for FeytiCare, our amazing app.

Thank you 

This readME file will be updated to for more other information soon
