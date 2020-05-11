from django.test import TestCase

# Create your tests here.

def paixu(list1):
    for i in range(len(list1)):
        for j in range(i+1,len(list1)):
            if list1[i]>list1[j]:
                temp=list1[j]
                list1[j]=list1[i]
                list1[i]=temp
    return list1


a=paixu([5,2,4,6,1])
print(a)
