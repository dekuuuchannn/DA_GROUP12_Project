import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("Coding By Wenjie")

File = 'Project_File.xlsx'

# Check all the Asia Country
Asia = [" Brunei Darussalam ", " Indonesia ", " Malaysia ", " Philippines ", " Thailand ", " Viet Nam ", " Myanmar ", " Japan ", " Hong Kong ", " China ", " Taiwan ", " Korea, Republic Of ", " India ", " Pakistan ", " Sri Lanka "]
Top = []
# Read Project_Files and search for Asia Columns
df = pd.read_excel(File, usecols=Asia)
# Sum of All Asia Country
valued = df.iloc[240:360].sum()
print("1998 - 2007")
# Sorted the Values from Highest to Lowest
TopList = valued.sort_values(ascending=False).index
TopListNum = valued.sort_values(ascending=False)
#print(TopListNum)

# Append the Top 3 Country to the List
x = 0
while (x < 3):
    Top.append(TopList[x])
    x += 1
print(TopListNum.head(3))

# Read Project Files Again But Only the Top 3 Columns
top3 = pd.read_excel(File, usecols=Top)
country0 = []
country1 = []
country2 = []
year = 0
startnum = 240
endnum = 252
# Check 10 years span of data
while (year < 10):
    year += 1
    # Get the Sum of that year
    valueofyear = top3.iloc[startnum:endnum].sum()
    # Append the Country Value for each year
    country0.append(int(valueofyear[Top[0]]))
    country1.append(int(valueofyear[Top[1]]))
    country2.append(int(valueofyear[Top[2]]))
    # Change to the Next Year
    startnum += 12
    endnum += 12

# X-axis of the Year
year10 = [1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007]
index = 0
range = [0, 10000]

while (index < 10):
    # Divide by thousand(Too Large to display)
    country0[index] = country0[index]/1000
    country1[index] = country1[index]/1000
    country2[index] = country2[index]/1000
    # Do for all data in Array
    index += 1

# Set Y-axis to be Max of 10000 and Min of 0, Change default Tick to 200
plt.yticks(np.arange(min(range), max(range), 200.0))
# Set x-axis to be Max of year10(2007) and Min of year10(1998), Change default Tick to 1
plt.xticks(np.arange(min(year10), max(year10)+1, 1.0))

plt.plot(year10, country0, label=TopList[0], marker=".")
plt.plot(year10, country1, label=TopList[1], marker="8")
plt.plot(year10, country2, label=TopList[2], marker="s")
plt.title("Asia Region to Singapore")
plt.legend()
plt.ylabel("Visitors ( Thousand )")
plt.xlabel("Year")
plt.grid(True)
plt.show()