f = open('three_digit_numbers.txt')
sample = f.read()
cols = sample.split()
numlist = []

for col in cols:
    num = int(col)
    numlist.append(num)


start = 300
for count in range(start, 501):
    with open('sorted_numbers.txt','w') as sort_f_obj:
        sort_f_obj.writelines(str(a) + "\n" for a in numlist)      
        if count in numlist:
            numlist.sort()
        else:
            sort_f_obj.writelines(str(numlist.append(count)))
            numlist.sort()
            print(f"{count} is missing")
f.close()
sort_f_obj.close()