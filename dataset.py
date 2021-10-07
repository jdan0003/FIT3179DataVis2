import csv

f = open('The Worlds 50 Best Restaurants 2018.csv', 'r')
nineteen = f.read()

o = open('one-star-michelin-restaurants.csv','r')
one = o.read() 

t = open('two-stars-michelin-restaurants.csv', 'r')
two = t.read()

e = open('three-stars-michelin-restaurants.csv', 'r')
three = e.read()

print('---------------- one star ------------------')
one = one.split('\n')
for i in range(len(one)):
    one[i] = one[i].split(',')
#print(one)

print('---------------- two star ------------------')
two = two.split('\n')
for i in range(len(two)):
    two[i] = two[i].split(',')
#print(two)

print('---------------- three star ------------------')
three = three.split('\n')
for i in range(len(three)):
    three[i] = three[i].split(',')
print(three)

print('---------------- 2019 ------------------')
nineteen = nineteen.split('\n')
for i in range(len(nineteen)):
    nineteen[i] = nineteen[i].split(',')
    # duplicates in one-star
    for j in range(len(one)-1):
        # check year
        if nineteen[i][0] == one[j][1]:
            if len(nineteen[i]) > 1:
                if nineteen[i][2] == one[j][0]:
                    print(True)
                    print('--------')
        else:
            if len(nineteen[i]) > 1:
                if nineteen[i][2] == one[j][0]:
                    print('no-star')
                    print('one-sheet')
                    print(nineteen[i][0])
                    print(nineteen[i][2])
                    print('awarded:'+ str(one[j][1]))
                    print('--------')
    # duplicates in two-star
    for j in range(len(two)-1):
        # check year
        if nineteen[i][0] == two[j][1]:
            if len(nineteen[i]) > 1:
                if nineteen[i][2] == two[j][0]:
                    print(True)
                    print(nineteen[i][0])
                    print(nineteen[i][2])
                    print('--------')
        else:
            if len(nineteen[i]) > 1:
                if nineteen[i][2] == two[j][0]:
                    print('no-star')
                    print('two-sheet')
                    print(nineteen[i][0])
                    print(nineteen[i][2])
                    print('awarded:'+ str(two[j][1]))
                    print('--------')
    # duplciates in three-star
    for j in range(len(three)-1):
        # check year
        if nineteen[i][0] == three[j][1]:
            if len(nineteen[i]) > 1:
                if nineteen[i][2] == three[j][0]:
                    print(True)
                    print(nineteen[i][2])
        else:
            if len(nineteen[i]) > 1:
                if nineteen[i][2] == three[j][0]:
                    print('no-star')
                    print('three-sheet')
                    print(nineteen[i][0])
                    print(nineteen[i][2])
                    print('awarded:' + str(three[j][1]))
                    print('--------')
duplicate = []

