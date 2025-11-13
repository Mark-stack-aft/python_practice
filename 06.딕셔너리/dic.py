import json
import langid
import keyboard
import time
from dict_mod import *

with open(r'06.딕셔너리/dic.json', 'r') as file:
    dic = json.load(file)


# dic = {}

try:
    while True:
        func = input('기능을 선택하세요 (0 : 종료, 1 : 추가, 2 : 삭제, 3 : 수정, 000 : 전부 삭제) : ')

        if func == '0':
            break

        elif func == '1':
            dic = plus(dic)

        elif func == '2':
            dic = delete(dic)

        elif func == '3':
            dic = correct(dic)

        elif func == '000':
            dic = dic_clear(dic)
                    
        else:
            func, dic = find(func, dic)


except:
    print('\n오류가 발생했습니다.')

finally:
    with open(r'06.딕셔너리/dic.json', 'w') as file:
        json.dump(dic, file, indent = 2)