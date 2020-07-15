# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading the file
data=pd.read_csv(path)

#Code starts here

# Step 1 
#Reading the file


#Creating a new variable to store the value counts
loan_status= data['Loan_Status'].value_counts()

#Plotting bar plot
loan_status.plot(kind = 'bar')


# Step 2
#Plotting an unstacked bar plot
property_and_loan = data.groupby(['Property_Area','Loan_Status']).size().unstack()

#Changing the x-axis label
plt.xlabel('Property Area')

#Changing the y-axis label
plt.ylabel('Loan Status')

#Rotating the ticks of X-axis
plt.xticks(rotation = 45)

# Step 3
#Plotting a stacked bar plot
education_and_loan = data.groupby(['Education','Loan_Status']).size().unstack()

#Plotting a stacked bar plot to compare education status and Loan status
education_and_loan.plot(kind= 'bar', stacked = False)

#Changing the x-axis label
plt.xlabel('Education Status')

#Changing the y-axis label
plt.ylabel('Loan Status')

#Rotating the ticks of X-axis
plt.xticks(rotation = 45)
# Step 4 
#Subsetting the dataframe based on 'Education' column
graduate = data[data['Education'] == 'Graduate']
graduate.head(10)

#Subsetting the dataframe based on 'Education' column
not_graduate = data[data['Education'] == 'Not Graduate']
not_graduate.head(10)

#Plotting density plot for 'Graduate'
graduate['LoanAmount'].plot(kind = 'density', label = 'Graduate')

#Plotting density plot for 'Graduate'
not_graduate['LoanAmount'].plot(kind = 'density', label = 'Not Graduate')

#For automatic legend display
plt.legend()

# Step 5
#Setting up the subplots
fig , (ax_1, ax_2, ax_3) = plt.subplots(nrows = 3, ncols = 1, figsize = (10,12))

#Plotting scatter plot
ax_1.scatter(data['ApplicantIncome'],data['LoanAmount'])


#Setting the subplot axis title
ax_1.set(title = 'Applicant Income')


#Plotting scatter plot
ax_2.scatter(data['CoapplicantIncome'],data['LoanAmount'])

#Setting the subplot axis title
ax_2.set(title = 'Coapplicant Income')

#Creating a new column 'TotalIncome'
data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']

#Plotting scatter plot
ax_3.scatter(data['TotalIncome'],data['LoanAmount'])


#Setting the subplot axis title
ax_3.set(title = 'Total Income')







