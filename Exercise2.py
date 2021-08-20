def meas(j, k):
    count = 0

    for i in range(len(j)):
        if (j[i] == k):
            count = count + 1
    return count 

str =(input("Paragraph: "))
c =(input("Enter a character: "))
print(meas(str, c))



    