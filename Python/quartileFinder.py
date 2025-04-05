'''

1. prompt for list or just manually add T T
2. sort the list (dont you dare use sort module, manually sort, do itttt)
3. check for the size (even or odd)

4. if size is even, find the left median (size/2) , right median(left + 1)
    4.1 median Q2 = ( list[rightM] + list[leftM] )/ 2
    4.2 first half of list for q1 = list[:rightM], second half for q3 = list[rightM:]
    4.3 for each half, step 3 - 5

5. if size is odd, median = list[(size/2)]
    5.1 first half for q1 = list[:median]
    5.2 second half for qq3 = list[:(median+1)]
    5.3 for each half, step 3 - 5




'''


# i dont know how to prompt for list T T, sorry Sir

quartileList = [1,1,3,5,7,8,10,11,11,15]

listSize = len(quartileList)
print("list size: ",listSize)

Q1 = 0
Q2 = 0
Q3 = 0



# kinda bubble sort
for i in range(listSize - 1):
    for j in range(i,listSize):
        if quartileList[i] > quartileList[j]:

            print(f"i : {quartileList[i]}, j: {quartileList[j]}")

            temp = quartileList[i]
            quartileList[i] = quartileList[j]
            quartileList[j] = temp

print(f"After sort: {quartileList}")


# to find median for each even quarter , return value of element
def evenListSize(list_size, quartile_list):

    right_median = int(list_size / 2)
    left_median = right_median - 1

    return ((quartile_list[left_median] + quartile_list[right_median]) / 2)



# to find median for each odd quarter, return "index"  of element

def oddListSize(list_size): return list_size//2


def q1_q3_finder(q1_list,q3_list,listSize):

    global Q1
    global Q3

    if listSize % 2 == 0:
        Q1 = evenListSize(listSize,q1_list)
        Q3 = evenListSize(listSize,q3_list)
    else:
        Q1 = q1_list[oddListSize(q1_list_size)]
        Q3 = q3_list[oddListSize(q1_list_size)]




# finding the true median (Q2)
if listSize % 2 == 0:     # for even



    Q2 = evenListSize(listSize, quartileList)

    # finding Q1 & Q3
    rightMedian = int(listSize/2)

    q1_list = quartileList[:rightMedian]
    q3_list = quartileList[rightMedian:]

    q1_list_size = len(q1_list)

    q1_q3_finder(q1_list,q3_list,q1_list_size)

    print("Q1 : ",Q1)
    print("Q2 : ",Q2)
    print("Q3 : ",Q3)


else:     # for odd

    q2_index = oddListSize(listSize)

    Q2 = quartileList[q2_index]

    q1_list = quartileList[:q2_index]

    q3_list = quartileList[(q2_index + 1):]


    q1_list_size = len(q1_list)

    q1_q3_finder(q1_list, q3_list, q1_list_size)

    print("Q1 : ", Q1)
    print("Q2 : ", Q2)
    print("Q3 : ", Q3)



