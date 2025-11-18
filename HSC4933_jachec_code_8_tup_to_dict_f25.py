data_list = [('apple', 5), ('banana', 2), ('orange', 8), ('grapes', 3), ('pineapple', 1)]

dictionary = []

def convert_to_dictionary(data_list):
    for key, value in data_list:
        dictionary[key] = value

    return dictionary

data_dict = {}
for key,value in data_list:
    data_dict[key] = value

print (data_dict)
converted_data_dict = convert_to_dictionary(data_list)
print ("Original list of tuples:", data_list)
print ("Converted dictionary:", converted_data_dict)