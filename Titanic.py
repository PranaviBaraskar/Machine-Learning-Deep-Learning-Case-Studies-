#------------***------------***-----------***------------***-----------***------------***-----------***------------***-----------***------------***-----------***

# - MACHINE LEARNING ON DATASET [TITANIC DATASET] USING LINEAR REGRESSION

#------------***------------***-----------***------------***-----------***------------***-----------***------------***-----------***------------***-----------***


#==================================================================================================================
# Importing All Required Libraries
#==================================================================================================================

import math
import numpy as np 
import pandas as pd 
import seaborn as sns
from seaborn import countplot
import matplotlib.pyplot as plt 
from matplotlib.pyplot import figure, show
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

#===========================================================================================================================================================
# FUNCTION NAME : TitanicLogistic(), Function Performing Accuracy to Titanic Datasets
#===========================================================================================================================================================

def TitanicLogistic():

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

    #Step 1 : Load Data
    titanic_data = pd.read_csv('TitanicDataset.csv')

    print("First 5 Entries from loaded Dataset")
    print(titanic_data.head())

    print("Number of Passangers are "+str(len(titanic_data)))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

    # Step 2 : Analyze data
    print("Visualisation : Survived and non Survived Passangers")
    figure()
    target = "Survived"

    countplot(data = titanic_data, x = target).set_title("Survived and Non Survived Passangers")
    show()

    print("Visualisation : Survived and non Survived Passangers based on Gender")
    figure()
    target = "Survived"

    countplot(data = titanic_data, x = target, hue = "Sex").set_title("Survived and non Survived Passangers based on Gender")
    show()

    print("Visualisation : Survived and non Survived Passangers class")
    figure()
    target = "Survived"

    countplot(data = titanic_data, x = target, hue = "Pclass").set_title("Survived and non Survived Passangers class")
    show()

    print("Visualisation : Survived and non Survived Passangers Age")
    figure()
    titanic_data['Age'].plot.hist().set_title("Survived and non Survived Passangers Age")
    show()

    print("Visualisation : Survived and non Survived Passangers based on the fare")
    figure()
    titanic_data["Fare"].plot.hist().set_title("Survived and non Survived Passangers based on the fare")
    show()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

    #step 3 : Data Cleaning
    titanic_data.drop("zero", axis = 1, inplace = True)

    print("First 5 entries from loaded dataset after removing zero column")
    print(titanic_data.head(5))

    print("Value of Sex Column")
    print(pd.get_dummies(titanic_data["Sex"]))

    print("Values of Sex column after removing one field ")
    Sex = pd.get_dummies(titanic_data["Sex"],drop_first = True)
    print(Sex.head(5))

    print("Values of plass coluns after removing one field")
    Pclass = pd.get_dummies(titanic_data["Pclass"],drop_first = True)
    print(Pclass.head(5))

    print("Values of data set after concatenating irrelevent columns")
    titanic_data = pd.concat([titanic_data,Sex,Pclass],axis = 1)
    print(titanic_data.head(5))

    print("Value of data set after removing irrelevent columns")
    titanic_data.drop(['Sex','sibsp','Parch','Embarked'], axis = 1, inplace = True)
    print(titanic_data.head(5))

    x = titanic_data.drop("Survived", axis = 1)
    y = titanic_data["Survived"]

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

    # Step 4 : Data Training
    xtrain, xtest, ytrain, ytest = train_test_split(x,y,test_size = 0.5)

    logmodel = LogisticRegression()

    logmodel.fit(xtrain,ytrain)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

    # Step 4 : Data Testing
    prediction = logmodel.predict(xtest)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

    # Step 5 : Calculate Accuracy
    print("Classification report of logistic Regression is : ")
    print(classification_report(ytest,prediction))

    print("Confusion Matrix of Logostic Regression is : ")
    print(confusion_matrix(ytest,prediction))

    print("Accuracy of logistic Regression is : ")
    print(accuracy_score(ytest,prediction))

#===========================================================================================================================================================
# FUNCTION NAME : main(), Execution starts from main function
#===========================================================================================================================================================

def main():
    print("----------- Welcome to our Application --------------")
    print("Survived Machine Learning")
    print("Logistic Regression on Titanic Data set")

    TitanicLogistic()

#===========================================================================================================================================================
# Application Starter
#===========================================================================================================================================================

if __name__ == "__main__":
    main()

#===========================================================================================================================================================

#------------***------------***-----------***------------***-----------***------------***-----------***------------***-----------***------------***-----------***

# ------------------------------------- END OF THE APPLICATION.

#------------***------------***-----------***------------***-----------***------------***-----------***------------***-----------***------------***-----------***
