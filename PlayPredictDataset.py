#-------------------------------------------------------------------------------------

import numpy as np 
import pandas as pd 
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier

#-------------------------------------------------------------------------------------

# Sunny = 2, OverCast = 0, Rainy = 1
# Hot = 1, Mild = 2, Cool = 0
# yes = 1, no = 0

#-------------------------------------------------------------------------------------

def Play_Predictor_KNN(data_path,Data_test1, Data_test2):
    data = pd.read_csv(data_path,index_col = 0)
    print("Size of Actual Dataset", len(data))

    feautures_names = ["Whether", "Temperature"]

    whether = data.Whether
    Temp = data.Temperature
    Labels = data.Play 

    le = preprocessing.LabelEncoder()

    weather_encoded = le.fit_transform(whether)
    print("Whether : ")
    print(weather_encoded)

    temp_encoded = le.fit_transform(Temp)
    label = le.fit_transform(Labels)

    print("Temperature : ")
    print(temp_encoded)

    print("Lables : ")
    print(label)

    feautures = list(zip(weather_encoded,temp_encoded))

    model = KNeighborsClassifier(n_neighbors = 3)

    model.fit(feautures, label)

    predicted = model.predict([[Data_test1,Data_test2]])

    print(predicted)
    if(predicted == 1):
        print("Your are able to Play Outside")
    elif(predicted == 0):
        print("Your are not able to Play Outside")

#-------------------------------------------------------------------------------------

def main():
    print("-----Python Machine Learning Application-----")
    print(" Play Predictor application using K-Nearest Neighbors Classifier")

    print("Enter the Whether : ")
    Whether = input()
    print("Enter the Temperature : ")
    Temperature = input()

    if Whether.lower() == "sunny":
        Whether = 2
    elif Whether.lower() == "overcast":
        Whether = 0
    elif Whether.lower() == "rainy":
        Whether = 1

    if Temperature.lower() == "hot":
        Temperature = 1
    elif Temperature.lower() == "mild":
        Temperature = 2
    elif Temperature.lower() == "cool":
        Temperature = 0

    Play_Predictor_KNN("PlayPredictor.csv",Whether,Temperature)

if __name__ =="__main__":
    main()

#-------------------------------------------------------------------------------------