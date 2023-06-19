def create_dict(**kwargs):
    result_dict = {}
    for key, value in kwargs.items():
        try:
            hash(key)
            result_dict[value] = key
        except:
            print("error")
            string = to_str(value)
            result_dict[string] = key
    return result_dict


def to_str(array):
    string = ""
    for i in range(len(array)):
        string += str(array[i])
    return string


result = create_dict(a=2, b=3, c='string', d=[1, 2, 3], e=(4, 5, 6))
print(result)
