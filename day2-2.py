# initialize variables
input_ids_list = []
input_id_length = 0
output_string = ""

# create id list
with open("Files/input.txt") as input_file:
    for line in input_file:
        if line.endswith("\n"):
            input_ids_list.append(line.rstrip("\n"))
        else:
            input_ids_list.append(line)

# reverse list of ids
reverse_input_ids_list = list(input_ids_list)
reverse_input_ids_list.reverse()

# get length of the input ids; this only accounts for lists in which all elements are the same length
input_id_length = len(input_ids_list[0])

# choose original input id for comparision with an index value
for index, item in enumerate(input_ids_list):
    item_set = set(item)

    # from the reversed list choose an id to compare to and find the common/different characters.
    for compared_item in reverse_input_ids_list:
        common = item_set.intersection(compared_item)
        difference = item_set.difference(compared_item)


        # we are only looking for strings with one letter difference
        if len(difference) == 1:

            # create temp lists so that we can delete the character in the position that is different.
            list_a = list(item)
            list_b = list(compared_item)

            del list_a[item.find(list(difference)[0])]
            del list_b[item.find(list(difference)[0])]

            # compare the two strings. If they match it is your answer.
            if list_a == list_b:
                print("After much ado, here's your match")

                # convert the list to a string so we can print it legibly.
                for character in list_a:
                    output_string += character
                print(output_string)
                break

        else:
            pass

    # once we have found our match there is no need to continue the outer loop.
    if output_string is not "" or None:
        break
    else:
        pass