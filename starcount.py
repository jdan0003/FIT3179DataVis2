import csv

f = open('all-michelin.csv', 'r')
michelinFile = f.read()

#[name, year, stars, latitude, longitude, city, region, zipCode, cuisine, price, url, country]

file = michelinFile.split('\n')

countries =[]


for i in range(len(file)):
    file[i] = file[i].split(',')
    if i!= 0:
        if len(file[i])>1:
            if i == 1: #[country, one star, two star, three star, total stars, average]
                if file[i][2] == 1:
                        countries.append([file[i][11],1,0,0,1,0])
                if file[i][2] == 2:
                    countries.append([file[i][11],0,1,0,2,0])
                if file[i][2] == 3:
                    countries.append([file[i][11],0,0,1,3,0])
            else:
                file[i][2] = int(file[i][2])
                found = False
                for j in range(len(countries)):
                    if countries[j][0] == file[i][11]:
                        found = True
                        if file[i][2] == 1:
                            countries[j][1] += 1
                            countries[j][4] += 1
                        if file[i][2] == 2:
                            countries[j][2] += 1
                            countries[j][4] += 2
                        if file[i][2] == 3:
                            countries[j][3] += 1
                            countries[j][4] += 3

                if found == False:
                    print('--------')
                    print(file[i][11])
                    print(file[i])
                    if file[i][2] == 1:
                        countries.append([file[i][11],1,0,0,1,0])
                    if file[i][2] == 2:
                        countries.append([file[i][11],0,1,0,2,0])
                    if file[i][2] == 3:
                        countries.append([file[i][11],0,0,1,3,0])
                
for i in range(len(countries)):
    sum = countries[i][1] + countries[i][2] + countries[i][3]
    countries[i][5] = countries[i][4] / sum 


print(countries)
            