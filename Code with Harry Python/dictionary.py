dic = {"key1":"value1","key2":"value2"}

# print(dic['key1'])

# dictionaries where unordered before py 3.7


# for key in dic.keys():
#     print(key)


print(dic.items())

for key , value in dic.items():
    print(f"The Value Corresponding to the key {key} is {value}")