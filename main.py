#opening file
f_obj = open('three_digit_numbers.txt', mode='r')
num_list = f_obj.read()

for f_obj in range(300, 501):
    if f_obj != num_list:
        print(f"{line} is missing")
    else:
        pass

f_obj.close()
            
            
    