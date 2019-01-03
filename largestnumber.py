Write a program to find the largest number in the list.

list1 = [20,31,22,24,18,15,3,2,14,42,92,12,1]

def largest_no_of_list(lis):

    maxx =0
    for i in lis:
        if(i > maxx):
            maxx = i
    print(maxx)
largest_no_of_list(list1)
