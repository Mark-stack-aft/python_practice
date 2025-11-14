import json
from dict_mod import *
from traceback import format_exc

with open(r'06.딕셔너리/dic.json', 'r') as file:
    dic = json.load(file)


# dic = {}

clear_screen()

try:
    while True:
        func = input('기능을 선택하세요 (0 : 종료, 1 : 추가, 2 : 삭제, 3 : 수정, 4 : 검색, 5 : 키워드 검색, 000 : 전부 삭제) : ')

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
                    
        elif func == '4':

            find_wd = input('단어나 뜻을 입력하세요 : ')

            func, dic = find(find_wd, dic)

        elif func == '5':

            key_word = input('키워드를 입력하세요 : ')

            func, dic = find_kw(key_word, dic)

        else:
            print('잘못 입력하였습니다.')

except KeyboardInterrupt:
    print('\n종료합니다.')

except:
    print('\n오류가 발생했습니다. | 오류 : %s' % format_exc().split('\n')[-2])

finally:
    with open(r'06.딕셔너리/dic.json', 'w') as file:
        json.dump(dic, file, indent = 2)