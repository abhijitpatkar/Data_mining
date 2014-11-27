from math import sqrt,modf
import re

def standard_deviation(mean,totalrows,*args):
    """
    This function calculate standard deviation of the parameters passed in argument
    """
    mean=mean
    n=totalrows
    argList=args
    sumOfAll=0
    for i in argList:
        """
        """
        calEachVal=0
        calEachVal=(float(i)-mean)**2
        sumOfAll=sumOfAll+calEachVal
    standard_deviation=sumOfAll/n-1 #According to formula
    squareroot=sqrt(standard_deviation)
    return squareroot
        


def distribution_calc(*args):
    """
    This function calculate the distribution accord to names in column 5 of csv
    """
    irisfirst=0
    irisecond=0
    iristhird=0
    allargs=[i for i in args]
    count=0
    irisfirst= allargs[0].count('Iris_First\n')
    irisecond= allargs[0].count('Iris_second\n')
    iristhird= allargs[0].count('Iris_Third\n')
    distribution_A=((irisfirst//100)*150)
    distribution_B=((irisecond//100)*150)
    distribution_C=((iristhird//100)*150)
    print distribution_A
    print distribution_B
    print distribution_C


    
if __name__=="__main__":
    fp=open('Iris.csv','r')
    INP=[]
    UNP=[]
    first_row=[]
    second_row=[]
    third_row=[]
    fourth_row=[]
    total=0
    row=1
    #loop to iterate over file pointer
    for i in fp:
        first_row.append(i.split(',')[0])
        second_row.append(i.split(',')[0])
        third_row.append(i.split(',')[0])
        fourth_row.append(i.split(',')[0])
        UNP.append(i.split(',')[4])
    INP=[first_row,second_row,third_row,fourth_row]
    
    for i in INP:
        n=0
        for k in i:
            total=total+float(k)
            n=n+1
        print "The standard Deviation for %d row is %f "%(row,(standard_deviation(total/n,n,*i)))# Call the standard deviation function        
        row=row+1

    distribution_calc(UNP)
     
