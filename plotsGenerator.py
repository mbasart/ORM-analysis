import csv
import matplotlib.pyplot as plt
import numpy as np

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