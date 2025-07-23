def swap_case(s):
    string_list = []
    for element in s:
        if element.islower():
            string_list.append(element.upper())
        elif element.isupper():
            string_list.append(element.lower())
        else:
            string_list.append(element)
        

    
    string_result = "".join(string_list)
    return string_result


s = input()
result = swap_case(s)
print(result)