import csv

with open("height-weight.csv",newline="")as f:
    reader   = csv.reader(f)
    filedata = list(reader)
filedata.pop(0)
# print(filedata)
# sorting data  to get the height of people.
new_data=[]
for i in range(len(filedata)):
	n_num = filedata[i][1]
	new_data.append(float(n_num))

##getting the mean
n = len(new_data)
total =0
for x in new_data:
    total += x

mean = total / n
print("Mean / Average is: " + str(mean))





#MOde
with open('height-weight.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)
# removing the list of titles using pop
file_data.pop(0)

new_data=[]
for i in range(len(file_data)):
	n_num = file_data[i][1]
	new_data.append(n_num)

n = len(new_data)
new_data.sort()
#using floor division to get the nearest number whole number
# floor division is shown by //
if n % 2 == 0:
    #getting the first number
	median1 = float(new_data[n//2])
    #getting the second number
	median2 = float(new_data[n//2 - 1])
    #getting mean of those numbers
	median = (median1 + median2)/2
else:
	median = new_data[n//2]

print("Median is: " + str(median))





# Python program to print
# mode of elements
from collections import Counter
import csv

with open('height-weight.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data=[]
for i in range(len(file_data)):
	n_num = file_data[i][1]
	new_data.append(n_num)



#Calculating Mode
data = Counter(new_data)
mode_data_for_range = {
                        "50-60": 0,
                        "60-70": 0,
                        "70-80": 0
                    }
for height, occurence in data.items():
    if 50 < float(height) < 60:
        mode_data_for_range["50-60"] += occurence
    elif 60 < float(height) < 70:
        mode_data_for_range["60-70"] += occurence
    elif 70 < float(height) < 80:
        mode_data_for_range["70-80"] += occurence

mode_range, mode_occurence = 0, 0
for range, occurence in mode_data_for_range.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
mode = float((mode_range[0] + mode_range[1]) / 2)
print(f"Mode is -> {mode:2f}")




# Python program to print
# mode of elements
from collections import Counter
import csv

with open('height-weight.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data=[]
for i in range(len(file_data)):
	n_num = file_data[i][1]
	new_data.append(n_num)


n = len(new_data)
#using counter function to get the occurences of numbers
data = Counter(new_data)
# # print(data)
get_mode = dict(data)
#
mode = []
mode1 = []
mode2 = []

#taking a,v for key and value
for a,v in get_mode.items():
    #changing type of a from string to float
    a= float(a)
    if 50< a <60:
        #checking if v is equal to the maximum of values in data
        if v == max(list(data.values())):
            mode.append(a)
    elif 60< a <70:
        if v == max(list(data.values())):
            mode1.append(a)
    elif 70< a <75:
        if v == max(list(data.values())):
            mode2.append(a)



if len(mode)>len(mode1) and len(mode2):
    print("Mode is /are "+ ', '.join(map(str, mode)))
elif len(mode1)>len(mode) and len(mode2):
    print("Mode is /are "+ ', '.join(map(str, mode1)))
elif len(mode2)>len(mode) and len(mode1):
    print("Mode is /are "+ ', '.join(map(str, mode2)))












