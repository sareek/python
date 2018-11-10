tableData = [['apples', 'orangesdddd', 'cherries', 'banana'],
             ['Ali', 'Bobsbaby', 'Car','ddd'],
             ['dogs', 'cats', 'moose', 'goosesss']]
     
subList=len(tableData)

array=[]
for i  in range(subList):  
    for j in range(len(tableData[i])-1):
        for k in range(len(tableData[i])):
            if len(str(tableData[i][j]))<len(str(tableData[i][k])):
                longest=len(str(tableData[i][k])) 
                value=str(tableData[i][k])

    array.append(longest)
    # print(array)

#line of code for transpose of a matrix
rez = [[tableData[j][i] for j in range(len(tableData))] for i in range(len(tableData[0]))] 
print('\n')
print(rez)

for i in range(len(rez)):
    print('\n') 
    for j in range(len(rez[0])):  
        print(rez[i][j].rjust(array[j],' '),end='   ')
      

     

 
   