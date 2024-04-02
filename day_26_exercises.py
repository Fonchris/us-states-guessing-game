# list comprehension can work with integers and strings too
""" the syntax is
new_list = [new_item for item in list]"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # list

# here the new_list is 'add_1_to_num' new_item is num+1 and item is num
add_1_to_num = [num + 1 for num in numbers]

# name = "chris"
# new_name = [letter + "c" for letter in name]
# print(new_name)
# squared_number =[number ** 2 for number in numbers]
# print(squared_number)
"""theres also a conditional list comprehension having the syntax :
new_list = [new_item for item in list if test]"""
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# long_names = [name.upper() for name in names if len(name) > 5]
# print(long_names)
# result = [num for num in numbers if num % 2 == 0]


"""dictionary comprehension
new_dict = {new_key: new_value for (key, value) in dict.items() 'if test' """
# 'if test' is only when there is a  condition
sentence = "what is the airspeed velocity of an unladen swallow?"
# new_dict = {word:len(word)for word in sentence.split()}
# print(new_dict)
weather_C = {
    "monday": 12,
    "tuesday": 14,
    "wednesday": 15,
    "thursday": 14,
    "friday": 21,
    "saturday": 22,
    "sunday": 24

}
weather_f = {day: temperature * 9 / 5 + 32 for (day, temperature) in weather_C.items()}
print(weather_f)
"""when dealing with dataframes we can use the .itterows that is using the syntax as shown below
for (index, row in dataframe.iterrows()) if condition"""
