from statistics import * #Imports everything that is needed
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

restart = True #Creates a variable that is true

def rangefunction(datalist): #Makes a function that finds the range of the data.
  datalist.sort()
  first = datalist[0]
  last = datalist[-1]
  return last - first

def mode(datalist): #Makes a function that finds the mode of the data (becuase multimode doesn't work on Grok
    counter = Counter(datalist)
    answer = [item for item, variable in counter.items() if variable == counter.most_common(1)[0][1]]
    return answer

def isnumber(datalist): #Makes a function that finds out whether or not the input was a number
    for i in datalist:
        try:
            float(i)
            return True
        except ValueError:
            return False

def continuation(): #Function that asks user if they want to analyse another data set
    global restart
    continuee = input("Would you like to analyse another data set? (yes/no) ")
    if continuee == "yes":
        restart = True
    elif continuee == "no":
        print("Goodbye")
        restart = False
    else:
        print("I'll take that as a no.")
        restart = False
    return restart

while restart == True: #While the variable above is true, the indented code will continue to run
    dataname = input("What is the name of this data set? ") #Asks user to input the name of the data set
    restart_number = True #Creates another variable that is true
    while restart_number == True: #While the above variable is true, the indented code will continue to run
        d = input("Enter data: ") #Asks user to input data
        if isnumber(d): #Using the function that was created above, if the input is a number, the indented code wll run
            data = d.split() #Turns the data into a list.
            datalist = [] #Creates an empty list
            for e in data: #For each item in the list of data
                datas = float(e) #Makes all the data in the list into a float, one by one.
                datalist.append(datas) #Appends the data to the emptpy list
            restart_number = False #Makes the restart_number variable false, so it doesn't run again
        else: #If the data inputed isn't a number
            print("I don't believe you inputed a number. ") #Prints "I don't believe you inputed a number"
            restart = continuation() #Asks the user if they want to analyse another set of data
        if restart == False: #If restart is false, it breaks away from the while loop
            break
    if restart == False: #If restart is false, it breaks away from the while loop
        break
    Mean = mean(datalist) #Finds the mean of the data set
    Median = median(datalist) #Finds the median of the data set
    Mode = mode(datalist) #Finds the Mode of the data set
    LMedian = median_low(datalist) #Finds the low median of the data set
    HMedian = median_high(datalist) #Finds the high median of the data set
    Range = rangefunction(datalist) #Finds the range of the data set
    datalistwithoutduplicates = [*set(datalist)] #Changes the datalist to a set, then back to a list, which removes any duplicates
    datalistwithoutduplicates.sort() #Sorts the data list without duplicates
    Mode.sort() #Sorts the list of modes
    print(f"The mean of your data is {Mean}") #Prints the mean
    print(f"The median of your data is {Median}") #Prints the median
    print(f"The low median of your data is {LMedian}") #Prints the low median
    print(f"The high median of your data is {HMedian}") #Prints the high median
    print(f"The range of your data is {Range}") #Prints the range
    dataset = np.array([Mean,Median,LMedian,HMedian, Range]) #Creates a NumPy array with the mean, median, low median, hight median and range values
    Modes = {} #Creates a dictionary
    if datalistwithoutduplicates == Mode: #If the data list without duplicates is the same as the list of modes
        print("There is no mode") #Prints "There is no mode"
        Labels = ['Mean', 'Median', 'Low Median','High Median','Range'] #Creates labels for the x axis of the bar graph
        plt.subplot(2,1,1) #Subplot to prevent overlapping of 2 different graphs
        plt.title = "Title" #Titles the graph
        plt.xlabel = "Xlabel" #Labels the x axis
        plt.ylabel = "Ylabel" #Labels the y axis
        plt.bar(Labels, dataset) #Creates the bar graph
        plt.show() #Shows the bar graph
    else: #Otherwise, if the data list without duplicates is not the same as the list of modes
        StrMode = str(Mode) #Changes the list of modes into a string
        StrMode = StrMode.replace("[","") #Replaces "[" with nothing
        StrMode = StrMode.replace("]","") #Replaces "]" with nothing
        print(f"The mode(s) of your data is/are {StrMode}.") #Prints the mode
        counter = 1 #Creates a variable that is equal to 1
        for e in Mode: #For each item in the list of modes
            Modes['Mode'+" "+str(counter)] = float(e) #Creates a new item in the dictionary that is called "Mode(whatever number item it is in the list)" and changes it to a float
            counter = counter + 1 #Adds one to the counter
        Modelist = np.array([list(Modes.values())]) #Creates a NumPy array with the value of each mode in the dictionary
        everything = np.concatenate((dataset, Modelist), axis=None) #Combines the 2 NumPy arrays
        plt.subplot(2,1,1) #Subplot to prevent overlapping of 2 different graphs
        plt.title = "Title" #Labels the title
        plt.xlabel = "Xlabel" #Labels the x axis
        plt.ylabel = "Ylabel" #Labels the y axis
        Labels = ['Mean','Median','Low Median','High Median','Range'] + list(Modes.keys()) #Creates the list of labels for the x axis
        plt.bar(Labels, everything) #Creates the bar graph
        plt.show() #Shows the bar graph
    datalist = np.array(datalist) #Creates a NumPy array with the data set
    plt.subplot(2,1,2) #Subplot to prevent overlapping of 2 different graphs
    plt.hist(datalist) #Creates a histogram that shows the occurences of each value in the data set
    plt.xlabel = "Number" #Labels the x axis
    plt.ylabel = "Occurences" #Labels the y axis
    plt.show() #Shows the histogram
    continuation() #Asks if the user wants to analyse another data set
