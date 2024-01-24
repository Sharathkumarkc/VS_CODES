# Create a list based on the sum of two consecutive pairs

num1 = [1,2,3,4,5,6,7,8,9]

output =[]

if len(num1) % 2 == 0:
    for i in range(0,len(num1)):
        sum =  num1[i] + num1[i+1]
        
        output.append(sum)
        print(f'{i+1} consecutive sum is {sum}')
print(output)


