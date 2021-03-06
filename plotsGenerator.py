import csv
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
import math

#### Data Reading ####

with open("cookies_report.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    #### Pie chart clicked vs not ####
    cookiesClicked = 0
    cookiesNotClicked = 0
    totalDomains = -1
    
    # REMEMBER! Column 6 is clicked, if we add more columns remember to change this value
    for row in csv_reader:
        totalDomains += 1
        if row[6] == "True":
            cookiesClicked += 1
        elif row[6] == "False":
            cookiesNotClicked += 1

    print("cookiesClicked: ", cookiesClicked)
    print("cookiesNotClicked: ", cookiesNotClicked)
    print("totalDomains: ", totalDomains)

    cookies = [cookiesClicked, cookiesNotClicked]
    nombres = ["Accepted", "Not asked/Not accepted"]
    plt.pie(cookies, labels=nombres, autopct="%0.1f %%")
    plt.axis("equal")
    plt.title("Pages able to accept cookies")
    plt.show()
    
with open("cookies_report.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    #### Pie chart same vs more cookies ####
    moreCookies = 0
    sameCookies = 0

    # Column 2 is cookies_default, column 5 is cookies_accepted
    for row in csv_reader:
        if row[6] == "True":
            if row[2] == row[5] or row[5] < row[2]:
                sameCookies += 1
            elif row[5] > row[2]:
                moreCookies += 1

    print("moreCookies: ", moreCookies)
    print("sameCookies: ", sameCookies)

    cookies = [moreCookies, sameCookies]
    nombres = ["More cookies", "Same Cookies"]
    plt.pie(cookies, labels=nombres, autopct="%0.1f %%")
    plt.axis("equal")
    plt.title("Domains with the same cookies after accept")
    plt.show()

with open("cookies_report.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    #### How many cookies by saying yes ####
    accepting = 0
    notInteract = 0
    firstLine = 0

    # Column 2 is cookies_default, column 5 is cookies_accepted
    for row in csv_reader:
        if firstLine == 0:
            firstLine += 1
        else:
            accepting = accepting + int(row[5])
            notInteract = notInteract + int(row[2])

    print("Cookies accepting: ", accepting)
    print("Cookies not interacting: ", notInteract)

    objects = ('Accepting','Not interacting')
    y_pos = np.arange(len(objects))
    performance = [accepting,notInteract]

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Number of cookies')
    plt.xlabel('Action performed')
    plt.title('Total of cookies accepting or not interacting')

    plt.show()


with open("cookies_report.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    firstLine = 0
    mydict = {}
    allCountries = []
    myDictPercentage = {}

    #Colum 7 is location (countries) and column 6 is clicked
    for row in csv_reader:
        if firstLine == 0:
            firstLine += 1
        else:
            newStr = row[7].replace('[','')
            newStr2 = newStr.replace(']','')
            arrayCountry = eval('[' + newStr2 + ']')
            #print(arrayCountry)
            for country in arrayCountry:
                allCountries.append(country)
                numCountry = allCountries.count(country)
                #print("total numCountry: ", numCountry)
                if row[6] == "False":
                    mydict[country] = mydict.get(country,0) + 1
                else:
                    mydict[country] = mydict.get(country,0) 

                actualValDic = mydict.get(country)
                #print("actualValDic: ", actualValDic)
                percentFalse = (actualValDic/numCountry) * 100
                #print("percentatge: ", percentFalse)
                myDictPercentage.update({country:percentFalse})
                

    print(mydict)
    print(myDictPercentage)

    plt.bar(range(len(myDictPercentage)), list(myDictPercentage.values()), align='center')
    plt.xticks(range(len(myDictPercentage)), list(myDictPercentage.keys()))
    plt.ylabel('Percentatge of NOT accepted')
    plt.xlabel('Country')
    plt.title('Country vs acceptance')

    plt.show()

    csv_header = ["country","perNotAccept"]
    with open("countryCookiesNot.csv", 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(csv_header)
        
        for key in myDictPercentage.keys():
            csv_file.write("%s,%s\n"%(key,myDictPercentage[key]))


with open("cookies_report.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    #### Pie chart same vs more cookies ####
    moreCookies = 0
    sameCookies = 0
    lessCookies = 0

    # Column 2 is cookies_default, column 4 is cookies_ninja
    for row in csv_reader:
        if row[2] == row[4]:
            sameCookies += 1
        elif row[4] > row[2]:
            moreCookies += 1
        elif row[4] < row[2]:
            lessCookies += 1

    print("moreCookies: ", moreCookies)
    print("sameCookies: ", sameCookies)
    print("lessCookies: ", lessCookies)

    cookies = [moreCookies, sameCookies, lessCookies]
    nombres = ["More cookies", "Same Cookies", "Less Cookies"]
    plt.pie(cookies, labels=nombres, autopct="%0.1f %%")
    plt.axis("equal")
    plt.title("Domains with the same cookies case Ninja Cookie plugin")
    plt.show()


with open("cookies_report.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    #### How many cookies by saying yes ####
    ninja = 0
    notInteract = 0
    firstLine = 0

    # Column 2 is cookies_default, column 4 is cookies_ninja
    for row in csv_reader:
        if firstLine == 0:
            firstLine += 1
        else:
            ninja = ninja + int(row[4])
            notInteract = notInteract + int(row[2])

    print("Cookies ninja plugin: ", ninja)
    print("Cookies not interacting: ", notInteract)

    objects = ('Ninja Plugin','Not interacting')
    y_pos = np.arange(len(objects))
    performance = [ninja,notInteract]

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Number of cookies')
    plt.xlabel('Action performed')
    plt.title('Total of cookies with ninja plugin or not interacting')

    plt.show()


#CDF accept cookies vs default
def cdf(data, data2):

    data_size=len(data)
    data_size2=len(data2)

    # Set bins edges
    data_set=sorted(set(data))
    data_set2=sorted(set(data2))
    bins=np.append(data_set, data_set[-1]+1)
    bins2=np.append(data_set2, data_set2[-1]+1)

    # Use the histogram function to bin the data
    counts, bin_edges = np.histogram(data, bins=bins, density=False)
    counts2, bin_edges2 = np.histogram(data2, bins=bins2, density=False)

    counts=counts.astype(float)/data_size
    counts2=counts2.astype(float)/data_size2

    # Find the cdf
    cdf = np.cumsum(counts)
    cdf2 = np.cumsum(counts2)

    # Plot the cdf
    blueLine, = plt.plot(bin_edges[0:-1], cdf,linestyle='--', marker="o", color='b')
    redLine, = plt.plot(bin_edges2[0:-1], cdf2,linestyle='--', marker="o", color='r')
    plt.legend([blueLine,redLine],['cookies Accepted', 'cookies Default'])
    plt.ylim((0,1))
    plt.xlabel('Number of cookies')
    plt.title("CDF cookies accepted vs default")
    plt.grid(True)

    plt.show()

print("resource_id,num_fonts")
data = []
data2 = []

with open('cookies_report.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    first = True
    for row in spamreader:
        if not first:
            data.append(row[5]) #Cookies accepted column
            data2.append(row[2]) #Default cookies column
        first = False

data_array = np.asarray(data).astype(int)
data_array2 = np.asarray(data2).astype(int)

cdf(data_array, data_array2)


#CDF ninja cookies vs default
def cdf(data, data2):

    data_size=len(data)
    data_size2=len(data2)

    # Set bins edges
    data_set=sorted(set(data))
    data_set2=sorted(set(data2))
    bins=np.append(data_set, data_set[-1]+1)
    bins2=np.append(data_set2, data_set2[-1]+1)

    # Use the histogram function to bin the data
    counts, bin_edges = np.histogram(data, bins=bins, density=False)
    counts2, bin_edges2 = np.histogram(data2, bins=bins2, density=False)

    counts=counts.astype(float)/data_size
    counts2=counts2.astype(float)/data_size2

    # Find the cdf
    cdf = np.cumsum(counts)
    cdf2 = np.cumsum(counts2)

    # Plot the cdf
    blueLine, = plt.plot(bin_edges[0:-1], cdf,linestyle='--', marker="o", color='b')
    redLine, = plt.plot(bin_edges2[0:-1], cdf2,linestyle='--', marker="o", color='r')
    plt.legend([blueLine,redLine],['cookies Ninja', 'cookies Default'])
    plt.ylim((0,1))
    plt.xlabel('Number of cookies')
    plt.title("CDF cookies Ninja Plugin vs Default")
    plt.grid(True)

    plt.show()

print("resource_id,num_fonts")
data = []
data2 = []

with open('cookies_report.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    first = True
    for row in spamreader:
        if not first:
            data.append(row[4]) #Ninja cookies column
            data2.append(row[2]) #Default cookies column
        first = False

data_array = np.asarray(data).astype(int)
data_array2 = np.asarray(data2).astype(int)

cdf(data_array, data_array2)


#Plot known 10 domains vs number of cookies
with open("cookies_report.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    #### How many cookies by saying yes ####
    firstLine = 0
    dictDomainCookies = {}

    # Column 2 is cookies_default, column 1 is domain names
    for row in csv_reader:
        if firstLine == 0:
            firstLine += 1
        else:
            if row[1] == "ups.com":
                dictDomainCookies["ups.com"] = int(row[2])
            elif row[1] == "bing.com":
                dictDomainCookies["bing.com"] = int(row[2])
            elif row[1] == "oracle.com":
                dictDomainCookies["oracle.com"] = int(row[2])
            elif row[1] == "cnn.com":
                dictDomainCookies["cnn.com"] = int(row[2])
            elif row[1] == "orange.fr":
                dictDomainCookies["orange.fr"] = int(row[2])
            elif row[1] == "dell.com":
                dictDomainCookies["dell.com"] = int(row[2])
            elif row[1] == "booking.com":
                dictDomainCookies["booking.com"] = int(row[2])
            elif row[1] == "grammarly.com":
                dictDomainCookies["grammarly.com"] = int(row[2])
            elif row[1] == "google.com":
                dictDomainCookies["google.com"] = int(row[2])
            elif row[1] == "amazon.com":
                dictDomainCookies["amazon.com"] = int(row[2])

    print("Dictionari cookies domains: ", dictDomainCookies)

    plt.bar(range(len(dictDomainCookies)),dictDomainCookies.values(), align='center')
    plt.xticks(range(len(dictDomainCookies)), list(dictDomainCookies.keys()))
    
    plt.ylabel('Number of cookies')
    plt.xlabel('Domains names')
    plt.title('Number cookies vs domains')

    plt.show()



with open("cookies_report.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    firstLine = 0
    mydict = {}
    myDictPercentage = {}
    myDictPercentageThird = {}
    mydictThird = {}
    mydictTotal = {}
    isEU = ['AT','BE','BG','HR','CY','CZ','DK','EE','FI','FR','DE','GR','HU','IE','IT','LV','LT','LU','MT','NL','PL','PT','RO','SK','SI','ES','SE']

    #Colum 7 is location (countries) and column 6 is clicked and column 8 is first parties
    for row in csv_reader:
        if firstLine == 0:
            firstLine += 1
        else:
            newStr = row[7].replace('[','')
            newStr2 = newStr.replace(']','')
            arrayCountry = eval('[' + newStr2 + ']')
            newStrPart = row[8].replace('[','')
            newStr2Part = newStrPart.replace(']','')
            arrayPart = eval('[' + newStr2Part + ']')
            #print(arrayCountry)
            #print(row[8])
            for i in range(len(arrayCountry)):
                if row[6] == "False" and arrayPart[i] == True:
                    mydict[arrayCountry[i]] = mydict.get(arrayCountry[i],0) + 1
                    mydictTotal[arrayCountry[i]] = mydictTotal.get(arrayCountry[i],0) + 1
                elif row[6] == "True" and arrayPart[i] == True:
                    mydict[arrayCountry[i]] = mydict.get(arrayCountry[i],0) 
                    mydictTotal[arrayCountry[i]] = mydictTotal.get(arrayCountry[i],0) + 1
                elif row[6] == "False" and arrayPart[i] == False:
                    mydictThird[arrayCountry[i]] = mydictThird.get(arrayCountry[i],0) + 1
                    mydictTotal[arrayCountry[i]] = mydictTotal.get(arrayCountry[i],0) + 1
                elif row[6] == "True" and arrayPart[i] == False:
                    mydictThird[arrayCountry[i]] = mydictThird.get(arrayCountry[i],0)
                    mydictTotal[arrayCountry[i]] = mydictTotal.get(arrayCountry[i],0) + 1
                            
    print(mydict)
    print(mydictTotal)
    print(mydictThird)

    for x in mydictTotal.keys():
        myDictPercentage.update({x:0})
        myDictPercentageThird.update({x:0})

    print(myDictPercentage)
    print(myDictPercentageThird)

    for x, y in mydict.items():
        yTotal = mydictTotal[x]
        percentFalse = (y/yTotal) * 100
        myDictPercentage.update({x:percentFalse})

    print(myDictPercentage)

    for x, y in mydictThird.items():
        yTotal = mydictTotal[x]
        percentFalse = (y/yTotal) * 100
        myDictPercentageThird.update({x:percentFalse})

    print(myDictPercentageThird)

    X_axis = np.arange(len(mydictTotal))

    plt.bar(X_axis - 0.2, myDictPercentage.values(), 0.4, label = 'First parties')
    plt.bar(X_axis + 0.2, myDictPercentageThird.values(), 0.4, label = 'Third parties')
    
    plt.xticks(X_axis, mydictTotal.keys())
    plt.xlabel("Country")
    plt.ylabel("Percentatge of NOT accepted")
    plt.title("Country vs acceptance")
    plt.legend()
    plt.show()

    csv_header = ["country","perNotAccept"]
    with open("countryCookiesNotFirst.csv", 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(csv_header)
        
        for key in myDictPercentage.keys():
            csv_file.write("%s,%s\n"%(key,myDictPercentage[key]))

    csv_header = ["country","perNotAccept"]
    with open("countryCookiesNotThird.csv", 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(csv_header)
        
        for key in myDictPercentageThird.keys():
            csv_file.write("%s,%s\n"%(key,myDictPercentageThird[key]))



with open("cookies_report.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    #### Pie chart clicked vs not ####
    cookiesClicked = 0
    cookiesNotClicked = 0
    totalDomains = -1
    
    # REMEMBER! Column 10 is accepted_pablo, if we add more columns remember to change this value
    for row in csv_reader:
        totalDomains += 1
        if row[10] == "True":
            cookiesClicked += 1
        elif row[10] == "False":
            cookiesNotClicked += 1

    print("cookiesClicked: ", cookiesClicked)
    print("cookiesNotClicked: ", cookiesNotClicked)
    print("totalDomains: ", totalDomains)

    cookies = [cookiesClicked, cookiesNotClicked]
    nombres = ["Accepted", "Not asked/Not accepted"]
    plt.pie(cookies, labels=nombres, autopct="%0.1f %%")
    plt.axis("equal")
    plt.title("Pages able to accept cookies Computer Vision")
    plt.show()



with open("cookies_report.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    #### Pie chart same vs more cookies ####
    moreCookies = 0
    sameCookies = 0

    # Column 2 is cookies_default, column 9 is cookies_pablo
    for row in csv_reader:
        if row[10] == "True":
            if row[2] == row[9] or row[9] < row[2]:
                sameCookies += 1
            elif row[9] > row[2]:
                moreCookies += 1

    print("moreCookies: ", moreCookies)
    print("sameCookies: ", sameCookies)

    cookies = [moreCookies, sameCookies]
    nombres = ["More cookies", "Same Cookies"]
    plt.pie(cookies, labels=nombres, autopct="%0.1f %%")
    plt.axis("equal")
    plt.title("Domains with the same cookies after accept Computer Vision")
    plt.show()



#CDF Computer Vision accept cookies vs default
def cdf(data, data2):

    data_size=len(data)
    data_size2=len(data2)

    # Set bins edges
    data_set=sorted(set(data))
    data_set2=sorted(set(data2))
    bins=np.append(data_set, data_set[-1]+1)
    bins2=np.append(data_set2, data_set2[-1]+1)

    # Use the histogram function to bin the data
    counts, bin_edges = np.histogram(data, bins=bins, density=False)
    counts2, bin_edges2 = np.histogram(data2, bins=bins2, density=False)

    counts=counts.astype(float)/data_size
    counts2=counts2.astype(float)/data_size2

    # Find the cdf
    cdf = np.cumsum(counts)
    cdf2 = np.cumsum(counts2)

    # Plot the cdf
    blueLine, = plt.plot(bin_edges[0:-1], cdf,linestyle='--', marker="o", color='b')
    redLine, = plt.plot(bin_edges2[0:-1], cdf2,linestyle='--', marker="o", color='r')
    plt.legend([blueLine,redLine],['cookies Computer Vision', 'cookies Default'])
    plt.ylim((0,1))
    plt.xlabel('Number of cookies')
    plt.title("CDF cookies Computer Vision vs Default")
    plt.grid(True)

    plt.show()

print("resource_id,num_fonts")
data = []
data2 = []

with open('cookies_report.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    first = True
    for row in spamreader:
        if not first:
            data.append(row[9]) #Cookies Pablo column
            data2.append(row[2]) #Default cookies column
        first = False

data_array = np.asarray(data).astype(int)
data_array2 = np.asarray(data2).astype(int)

cdf(data_array, data_array2)



#CDF all
def cdf(data, data2, data3, data4):

    data_size=len(data)
    data_size2=len(data2)
    data_size3=len(data3)
    data_size4=len(data4)

    # Set bins edges
    data_set=sorted(set(data))
    data_set2=sorted(set(data2))
    data_set3=sorted(set(data3))
    data_set4=sorted(set(data4))
    bins=np.append(data_set, data_set[-1]+1)
    bins2=np.append(data_set2, data_set2[-1]+1)
    bins3=np.append(data_set3, data_set3[-1]+1)
    bins4=np.append(data_set4, data_set4[-1]+1)

    # Use the histogram function to bin the data
    counts, bin_edges = np.histogram(data, bins=bins, density=False)
    counts2, bin_edges2 = np.histogram(data2, bins=bins2, density=False)
    counts3, bin_edges3 = np.histogram(data3, bins=bins3, density=False)
    counts4, bin_edges4 = np.histogram(data4, bins=bins4, density=False)

    counts=counts.astype(float)/data_size
    counts2=counts2.astype(float)/data_size2
    counts3=counts3.astype(float)/data_size3
    counts4=counts4.astype(float)/data_size4

    # Find the cdf
    cdf = np.cumsum(counts)
    cdf2 = np.cumsum(counts2)
    cdf3 = np.cumsum(counts3)
    cdf4 = np.cumsum(counts4)

    # Plot the cdf
    blueLine, = plt.plot(bin_edges[0:-1], cdf,linestyle='--', marker="o", color='b')
    redLine, = plt.plot(bin_edges2[0:-1], cdf2,linestyle='--', marker="o", color='r')
    greenLine, = plt.plot(bin_edges3[0:-1], cdf3,linestyle='--', marker="o", color='g')
    orangeLine, = plt.plot(bin_edges4[0:-1], cdf4,linestyle='--', marker="o", color='y')
    plt.legend([blueLine,redLine,greenLine,orangeLine],['cookies Ninja', 'cookies Default','cookies Computer Vision','Cookies Selenium'])
    plt.ylim((0,1))
    plt.xlabel('Number of cookies')
    plt.title("CDF cookies of all different methods")
    plt.grid(True)

    plt.show()

print("resource_id,num_fonts")
data = []
data2 = []
data3 = []
data4 = []

with open('cookies_report.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    first = True
    for row in spamreader:
        if not first:
            data.append(row[4]) #Ninja cookies column
            data2.append(row[2]) #Default cookies column
            data3.append(row[9]) #Cookies Pablo column
            data4.append(row[5]) #Cookies accepted column
        first = False

data_array = np.asarray(data).astype(int)
data_array2 = np.asarray(data2).astype(int)
data_array3 = np.asarray(data3).astype(int)
data_array4 = np.asarray(data4).astype(int)

cdf(data_array, data_array2, data_array3, data_array4)



with open("cookies_report.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    #### Pie chart same vs more cookies ####
    moreCookies = 0
    sameCookies = 0
    firstLine = 0

    # Column 2 is cookies_default, we inspect the percentage of domains that add cookies by default
    for row in csv_reader:
        if firstLine == 0:
            firstLine += 1
        else:
            if int(row[2]) != 0:
                sameCookies += 1
            elif int(row[2]) == 0:
                moreCookies += 1

    print("moreCookies: ", moreCookies)
    print("sameCookies: ", sameCookies)

    cookies = [moreCookies, sameCookies]
    nombres = ["Not adding cookies", "Adding cookies"]
    plt.pie(cookies, labels=nombres, autopct="%0.1f %%")
    plt.axis("equal")
    plt.title("Domains that add cookies by default")
    plt.show()