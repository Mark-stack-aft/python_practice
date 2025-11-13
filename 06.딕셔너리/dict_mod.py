import json
import langid
import keyboard
import time
from password import get_password

def plus(dic):
    key = input('추가할 단어를 입력하세요 : ')

    if not key in dic.keys() and not key in dic.values():
        value = input('뜻 : ')
                
        if langid.classify(key)[0] == 'en':
            dic[key] = value

        if langid.classify(key)[0] == 'ko':
            dic[value] = key

    else:
        print('단어가 이미 있습니다!')

    return dic

def delete(dic):
    key = input('삭제할 단어를 입력하세요 : ')

    if key in dic:
        dic.pop(key)

    else:
        print('오류! 삭제할 단어가 없습니다!')

    return dic

def correct(dic):
    key = input('수정할 단어를 입력하세요 : ')

    if key in dic:
        re_key = input('수정할 단어의 수정된 단어를 입력하세요 : ')
        re_value = input('수정할 단어의 수정된 뜻을 입력하세요 : ')

        dic.pop(key)

        if langid.classify(key)[0] == 'en':
            dic[re_key] = re_value

        if langid.classify(key)[0] == 'ko':
            dic[re_value] = re_key

    else:
        print('오류! 수정할 단어가 없습니다!')

    return dic

def dic_clear(dic):
    print('정말로 삭제하시겠습니까? : ')
    print(' 네    ⚪ 아니오', end = '', flush = True)

    click = False

    while True:
        
        event = False

        keyboard.read_key(suppress=True)

        event = keyboard.read_event(suppress=True)

        if event.name == 'enter' or event.name == 'return':
            if click == True:

                password = input('\n비밀번호 : ')

                if password == get_password:
                    dic.clear()
                    print('\n완료되었습니다.')

                else:
                    print('\n비밀번호가 틀렸습니다.')
                        
            else:
                print('\n취소되었습니다.')

            break

        elif event.name == 'left' or event.name == 'right':
            if click == True:
                click = False
                print('\r   네  ⚪ 아니오', end = '')

            else:
                click = True
                print('\r⚪ 네     아니오', end = '')

        keyboard.read_key(suppress=True)

    return dic

def find(func, dic):
    key_value = func
    if langid.classify(key_value)[0] == 'en':
        if key_value in dic.keys():
            print(f'단어 : {key_value}, 뜻 : {dic[key_value]}')

    if langid.classify(key_value)[0] == 'ko':
        if key_value in dic.values():
            print(f'단어 : {list(dic.keys())[list(dic.values()).index(key_value)]}, 뜻 : {key_value}')

    return func, dic