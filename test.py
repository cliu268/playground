# print("Hello World!")
# print("         /|")
# print("        / |")
# print("       /  |")
# print("      /   |")
# print("     /____|")

# name = "WHATTTT"
# print(" My name is " + name + "!!!!")

# num1 = input("Enter number1:")
# num2 = input("Enter number2:")
# result = float(num1) + float(num2)
# print(result)



import pandas as pd 
from urllib.request import urlretrieve
urlretrieve('https://hub.jovian.ml/wp-content/uploads/2020/09/italy-covid-daywise.csv', 'italy-covid-daywise.csv')
covid_df = pd.read_csv('italy-covid-daywise.csv')
type(covid_df)
covid_df

