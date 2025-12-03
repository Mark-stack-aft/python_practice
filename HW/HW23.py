def make_reverse(string):

    reversing_list = []
    
    for char in string:
        reversing_list.append(char)
    
    reversing_list.reverse()

    print(reversing_list)

    result = ''.join(reversing_list)
    return result

string = input('문자열을 입력하세요 : ')
print(make_reverse(string))