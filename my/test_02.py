from functools import reduce

number_list = [3, 4, 6, 9, 34, 12]
my_sum = 0
for number in number_list:
    my_sum += number
    print(my_sum)




date_info = {"year": "2020", "month": "01", "day": "15"}
track_info = {"artist": "beethowen", "title": "song 5"}
all_info = {**date_info, **track_info}

assert all_info == {}
print(all_info)