my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while index < len(my_list):
    number_list = my_list[index]
    if number_list < 0:
       break
    if number_list == 0:
        index +=1
        continue
    print(number_list)
    index +=1





