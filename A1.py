# FernandoSenukiA2Q2.py
#
# Course: COMP 1012
# Instructor: Abolfazl Babaei
# Assignment: 2 Question 2
# Author: Senuki Fernando
# Version: 2023/07/08
#
# Purpose: get the standaard deviation of a list of numbers
#list1=original list
#list2=list with the square of the difference
#sd=standard deviation
#sd2=standard deviation squared


def grabList():
    list1 = []
    n = 0
    length = int(input("Enter the length of the list: "))
    while n < length:
        a = int(input("Enter element %d: " % (n+1)))
        list1.append(a)
        n += 1

    return list1


def avg_calc(list1):  
    total = 0
    for i in range(len(list1)):
        total += list1[i]

    average = total/len(list1)

    return average


def sd_calc(average, list1):
    from math import sqrt

    list2 = []  # sd^2 list
    total2 = 0

    for i in range(len(list1)):
        x = (list1[i]-average)**2
        list2.append(x)
        total2 += x

    sd2 = total2/len(list1)
    sd = sqrt(sd2)

    return sd


def main():
    list1 = grabList()
    average = avg_calc(list1)
    sd = sd_calc(average, list1)

    print('Sample data: ', list1)
    print('Standard deviation: %.2f' % sd)


main()
