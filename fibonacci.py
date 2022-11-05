
def fibonacci():
    k = int(input("basamak sayısı giriniz: "))
    num1 = 0
    num2 = 1
    count = 0
    while (k>=count):
        if (k==1):
            print(num1, num2, end=" ")
        count = 0
        num2 = num1 + num2
        num1 = num2 - num1
        a = num2
        while a>0:
            a = a//10
            count += 1
        if (k==count):
            print(num2, end=" ")

fibonacci()        

