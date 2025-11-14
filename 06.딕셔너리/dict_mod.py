import langid
import keyboard
from password import get_password
import os
from termcolor import colored

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    
    else:
        os.system('clear')

def plus(dic):
    key = input('추가할 단어를 입력하세요 : ')

    if not key in dic.keys() and not key in dic.values():
        value = input('뜻 : ')
                
        if langid.classify(key)[0] == 'en' and langid.classify(value)[0] == 'ko':
                dic[key] = value

        elif langid.classify(key)[0] == 'ko' and langid.classify(value)[0] == 'en':
            dic[value] = key

        else:
            print('영/한 구조가 아닙니다!')
    else:
        print('단어가 이미 있습니다!')

    return dic

def delete(dic):
    key = input('삭제할 단어를 입력하세요 : ')

    if langid.classify(key)[0] == 'en':
        if key in dic:
            dic.pop(key)

    elif langid.classify(key)[0] == 'ko':
        if key in dic.values():
            dic.pop(list(dic.keys())[list(dic.values()).index(key)])

    else:
        print('오류! 삭제할 단어가 없습니다!')

    return dic

def correct(dic):
    key = input('수정할 단어를 입력하세요 : ')

    if langid.classify(key)[0] == 'en':
        if key in dic:
            re_key = input('수정할 단어의 수정된 단어를 입력하세요 : ')
            re_value = input('수정할 단어의 수정된 뜻을 입력하세요 : ')

            dic.delete(key)

            if langid.classify(re_key)[0] == 'en' and langid.classify(re_value)[0] == 'ko':
                dic[re_key] = re_value

            elif langid.classify(re_key)[0] == 'ko' and langid.classify(re_value)[0] == 'en':
                dic[re_value] = re_key

            else:
                print('영/한 구조가 아닙니다!')

    elif langid.classify(key)[0] == 'ko':
        if key in dic.values():
            re_key = input('수정할 단어의 수정된 단어를 입력하세요 : ')
            re_value = input('수정할 단어의 수정된 뜻을 입력하세요 : ')

            dic.pop(list(dic.keys())[list(dic.values()).index(key)])

            if langid.classify(re_key)[0] == 'en' and langid.classify(re_value)[0] == 'ko':
                dic[re_key] = re_value

            elif langid.classify(re_key)[0] == 'ko' and langid.classify(re_value)[0] == 'en':
                dic[re_value] = re_key

            else:
                print('영/한 구조가 아닙니다!')

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

def find(find_wd, dic):

    key_value = find_wd

    if langid.classify(key_value)[0] == 'en':
        if key_value in dic.keys():
            print(f'단어 : {key_value}, 뜻 : {dic[key_value]}')

        else:
            print('단어가 없습니다!')

    elif langid.classify(key_value)[0] == 'ko':
        if key_value in dic.values():
            print(f'단어 : {list(dic.keys())[list(dic.values()).index(key_value)]}, 뜻 : {key_value}')

        else:
            print('단어가 없습니다!')

    return find_wd, dic

def find_kw(key_word, dic):
    key_value = key_word

    found_list = []

    attrs = ['bold']

    if langid.classify(key_value)[0] == 'en':
        for key in list(dic.keys()):
            if key_value in key:
                found_list.append(key.replace(key_value, '⬛'))

        if bool(found_list) == True:
            for printing in found_list:
                print('단어 : ', end = '')
                
                for ind in printing:
                    print(colored(key_value, 'red', attrs=['bold']) if ind == '⬛' else ind, end = '')

                print(f', 뜻 : {dic[printing.replace('⬛', key_value)]}')

        else:
            print('단어가 없습니다!')

    elif langid.classify(key_value)[0] == 'ko':
        for value in list(dic.values()):
            if key_value in value:
                found_list.append(value.replace(key_value, '⬛'))

        if bool(found_list) == True:
            for printing in found_list:
                print(f'단어 : {list(dic.keys())[list(dic.values()).index(printing.replace('⬛', key_value))]}, 뜻 : ', end = '')
                
                for ind in printing:
                    print(colored(key_value, 'red', attrs=['bold']) if ind == '⬛' else ind, end = '')

                print()

        else:
            print('단어가 없습니다!')

    return key_value, dic