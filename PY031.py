# print character from string that are present at an even index number

text = 'Center for geoinformatice Technlogy'
length = len(text)
print(length)

for index_pos in range(length):
    if index_pos % 2 == 0:
        print(text[index_pos])



