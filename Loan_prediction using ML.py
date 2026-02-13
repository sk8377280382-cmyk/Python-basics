
# Loan prediction using Decision Tree classifier
import pandas as pd
from sklearn.tree import DecisionTreeClassifier


# Sample Training Data
data = {"Income": [50000,30000,80000,20000,90000],
        "CreditScore":[700,600,750,500,800],
        "LoanApproved":[1,0,1,0,1]
        }
#convert to Datafram
df = pd.DataFrame(data)

# input features (X) and Output Label(Y)
X = df[["Income","CreditScore"]]
Y = df[["LoanApproved"]]

# Created Decision Tree Model
model = DecisionTreeClassifier()

#Train Model
model.fit(X,Y)

# User Input
income = int(input("Enter Income:"))
credit = int(input("Enter Credit Score:"))

#prediction
result = model.predict ([[income, credit]])

#output
if result[0] == 1:
    print("Loan Approved")
else:
    print("Loan Rejected")
