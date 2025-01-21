#----------***-----------***----------***-----------***----------***-----------***----------***-----------***----------***
# - MACHINE LEARNING ON DATASET [WINE DATASET] USING LINEAR REGRESSION
#----------***-----------***----------***-----------***----------***-----------***----------***-----------***----------***

#==================================================================================================================
# Importing All Required Libraries
#==================================================================================================================

from sklearn import metrics
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

#==================================================================================================================
# FUNCTION NAME : WinePredictor(), Function Performing Accuracy to Wine Datasets
#==================================================================================================================

def WinePredictor():

    #Loading wine data into program
    wine = datasets.load_wine()

    #Printing all Independent variables
    print(wine.feature_names)

    #Printing all Dependent variables
    print(wine.target_names)

    #Printing the Wine data (top 5 records)
    print(wine.data[0:5])

    #Printing the wine labels (0:Class_0, 1:Class_1, 2:Class_3)
    print(wine.target)

    #Performs data splitting into training and testing
    X_train, X_test, Y_train, Y_test = train_test_split(wine.data, wine.target, test_size = 0.3)

    #Creating Object of KNN with neighbors Highperparameter : as 3
    knn = KNeighborsClassifier(n_neighbors = 3)

    #Training the model using fit method
    knn.fit(X_train, Y_train)

    #Testing the model using predict method
    y_pred =  knn.predict(X_test)

    #Printing Accuracy of the algorithm using accuracy_score method
    print("Accuracy : ",metrics.accuracy_score(Y_test,y_pred))

#==================================================================================================================
# FUNCTION NAME : main(), Execution starts from main function
#==================================================================================================================

def main():
    print("-----** Python Machine Learning Algorithm **-----")
    print("Wine Dataset using K-Nearest Neighbors classifier")

    #Calling Function to Calculate Accuracy
    WinePredictor()

#==================================================================================================================
# Application Starter
#==================================================================================================================

if __name__ == "__main__":
    main()

#==================================================================================================================

#------------***------------***-----------***------------***-----------***------------***-----------***------------***-----------***------------***-----------***

# ------------------------------------- END OF THE APPLICATION.

#------------***------------***-----------***------------***-----------***------------***-----------***------------***-----------***------------***-----------***
