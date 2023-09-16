import matplotlib.pyplot as plt
import sqlite3

years = []
co2 = []
temp = []

#Connect to SQLite database
connect = sqlite3.connect('climate.db')

#create a cursor object to interact with the database 
cursor = connect.cursor()

#A query to fetch data from the database 
cursor.execute('SELECT year, co2, temperature FROM ClimateData ORDER BY year')

#Fetch rows from query
data = cursor.fetchall()

# Populate the lists with the retrieved data
for row in data:
    years.append(row[0])
    co2.append(row[1])
    temp.append(row[2])

connect.close()

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_1.png") 
