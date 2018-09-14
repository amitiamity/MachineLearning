#Predicting diabetes
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('C:/Users/amitpatel/PycharmProjects/MachineLearning_Project1/data/pima-data.csv')
desired_width = 3200
pd.set_option("display.width",desired_width)
#print(data.shape)
# print(data.head(5))
#print(data.tail(5))
#check if any of the cell is null
#print(data.isnull().values.any())
#check if any of the column is duplicate or irrelevant, check for correlation
data.corr();
#print(data.corr())
#thickness and skin are correlated, removing the column
del data['skin']

#modelling the data
#check data types, if there is any string or boleean
print(data.head())
#it has true and false value, we need to change to 0 or 1
#mappinng dic
diabetes_map = {True:1,False:0}
data['diabetes'] = data['diabetes'].map(diabetes_map)
print(data.head())

#check how many time people hace diabetes
dia_true = len(data.loc[data['diabetes'] == True])
#lambda way
dia_false = len(data.loc[lambda data:data['diabetes'] == False])
print(dia_true)
print(dia_false)
#print the percentage of people who were daibetic
print("Percent of diabetic people : {}".format(dia_true/(dia_true+dia_false) * 100))
print("Percent of not diabetic people : {}".format(dia_false/(dia_true+dia_false) * 100))










#dummy
#plt.matshow(data.corr())
#plt.show()
x= [1,2,3,4]
y = [100,200,300,400]
#plt.plot(x,y)
#plt.show();