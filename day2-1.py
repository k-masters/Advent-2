import collections

# initialize variables
input_ids_list = []
ids_2peat_dict = {}
ids_3peat_dict = {}
triple_count = 0
double_count = 0
default_dict = collections.defaultdict(int)

# create id list
with open("Files/test_input_day2-1.txt") as input_file:
    for line in input_file:
        if line.endswith("\n"):
            input_ids_list.append(line.rstrip("\n"))
        else:
            input_ids_list.append(line)

# fill each dictionary with key:value pairs using id list. Set all values to False initially. They will be changed to
# true later if the key contains repeated letters.
for id in input_ids_list:
    ids_2peat_dict.update({id: False})
    ids_3peat_dict.update({id: False})

# print(ids_2peat_dict)
# print(ids_3peat_dict)

for id in input_ids_list:
    default_dict.clear()  # clear dict each pass through
    print(id)

    for letter in id:  # get recurrence count of each letter
        default_dict[letter] += 1

    # loop through the default dict and count values that are 2 or greater
    # and set associated dict value to True
    for value in sorted(default_dict, key=default_dict.get, reverse=True):
        print(default_dict[value])
        if default_dict[value] >= 3:
            ids_3peat_dict[id] = True
        elif default_dict[value] == 2:
            ids_2peat_dict[id] = True
        else:
            pass

# count the amount of times that True appears in each dict
triple_count = sum(value == True for value in ids_3peat_dict.values())
double_count = sum(value == True for value in ids_2peat_dict.values())

# multiply the two sums together for the checksum value and print
print("The checksum value is: {}".format(str(triple_count * double_count)))