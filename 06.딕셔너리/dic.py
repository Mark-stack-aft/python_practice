import json
from dict_mod import *
from traceback import format_exc
import keyboard
from orign_dic import orign_dic
import colorama
from colorama import Fore, Back, Style

def make():
    with open(r'06.딕셔너리/person.json', 'r') as file:
        persons = json.load(file)

    print()
    print('---회원가입---')
    
    try:
        et = True

        while et:
            new_id = input('아이디 : ')
            
            if len(new_id) >= 10:
                et = False
            else:
                print('아이디의 길이는 10자 이상이여야 합니다.')
                et = True
            
            if new_id in persons.keys():
                print('이미 있는 아이디 입니다.')
                et = True
            else:
                et = False

        et = True

        while et:
            new_password = input('비밀번호 : ')
            
            if len(new_id) >= 10:
                et = False
            else:
                print('비밀번호의 길이는 10자 이상이여야 합니다.')
                et = True

        persons[new_id] = new_password

        with open(r'06.딕셔너리/person.json', 'w') as file:
            persons = json.dump(persons, file, indent = 2)

        with open(r'06.딕셔너리/dic.json', 'w') as file:
            dic_ = json.load(file)
            dic_[persons] = orign_dic
            json.dump(dic_, file, indent = 2)

    except KeyboardInterrupt:
        print('\n회원가입이 취소되었습니다.')

def login():
    with open(r'06.딕셔너리/person.json', 'r') as file:
        persons = json.load(file)

    person = ''

    print()

    id = input('아이디 입력 : ')
    password = input('비밀번호 입력 : ')

    if id in persons.keys():
        if password == persons[id]:
            print('로그인 성공!')
            person = id

        else:
            print('아이디나 비밀번호가 틀렸습니다.')

    else:
        print('회원가입을 하시겠습니까?')
        print('   네    ⚪ 아니오', end = '', flush = True)

        click = False

        while True:
        
            event = False

            keyboard.read_key(suppress=True)

            event = keyboard.read_event(suppress=True)

            if event.name == 'enter' or event.name == 'return':
                if click == True:
                    make()
                            
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

    return person

def diction(person, color):
    with open(r'06.딕셔너리/dic.json', 'r') as file:
            dic_ = json.load(file)
            dic = dic_[person]
    try:
        if color == True:
            # dic = {}

            clear_screen()

            try:
                while True:
                    func = input(Back.WHITE + Style.DIM + '기능을 선택하세요 (0 : 종료, 1 : 추가, 2 : 삭제, 3 : 수정, 4 : 검색, 5 : 키워드 검색, 6 : 번역, 000 : 전부 삭제) : ' + Style.RESET_ALL)

                    if func == '0':
                        break

                    elif func == '1':
                        dic = plus(dic, color)

                    elif func == '2':
                        dic = delete(dic, color)

                    elif func == '3':
                        dic = correct(dic, color)

                    elif func == '000':
                        dic = dic_clear(dic, color)
                                
                    elif func == '4':

                        find_wd = input(Back.CYAN + '단어나 뜻을 입력하세요 : ' + Style.RESET_ALL)

                        func, dic = find(find_wd, dic, color)

                    elif func == '5':

                        key_word = input(Back.BLACK + Fore.WHITE + '키워드를 입력하세요 : ' + Style.RESET_ALL)

                        func, dic = find_kw(key_word, dic, color)

                    elif func == '6':

                        tr_str = input(Back.LIGHTBLACK_EX + Fore.LIGHTWHITE_EX + '번역할 것을 입력하세요 : ' + Style.RESET_ALL)
                        trans(tr_str, color)


                    else:
                        print(Back.LIGHTYELLOW_EX + '잘못 입력하였습니다.' + Style.RESET_ALL)

            except KeyboardInterrupt:
                print(Back.WHITE + Style.DIM + '\n종료합니다.' + Style.RESET_ALL)

            except:
                print(Back.LIGHTYELLOW_EX + '\n오류가 발생했습니다. | 오류 : %s' % format_exc().split('\n')[-2] + Style.RESET_ALL)

        else:
            # dic = {}

            clear_screen()

            try:
                while True:
                    func = input('기능을 선택하세요 (0 : 종료, 1 : 추가, 2 : 삭제, 3 : 수정, 4 : 검색, 5 : 키워드 검색, 6 : 번역, 000 : 전부 삭제) : ')

                    if func == '0':
                        break

                    elif func == '1':
                        dic = plus(dic, color)

                    elif func == '2':
                        dic = delete(dic, color)

                    elif func == '3':
                        dic = correct(dic, color)

                    elif func == '000':
                        dic = dic_clear(dic, color)
                                
                    elif func == '4':

                        find_wd = input('단어나 뜻을 입력하세요 : ')

                        func, dic = find(find_wd, dic, color)

                    elif func == '5':

                        key_word = input('키워드를 입력하세요 : ')

                        func, dic = find_kw(key_word, dic, color)

                    elif func == '6':

                        tr_str = input('번역할 것을 입력하세요 : ')
                        trans(tr_str, color)


                    else:
                        print('잘못 입력하였습니다.')

            except KeyboardInterrupt:
                print('\n종료합니다.')

            except:
                print('\n오류가 발생했습니다. | 오류 : %s' % format_exc().split('\n')[-2])

    finally:
        if not person == '':
            dic_[person] = dic

            with open(r'06.딕셔너리/dic.json', 'w') as file:
                json.dump(dic_, file, indent = 2)

def dictionary(bool, person, color):
    if bool:
        diction(person, color)

    else:
        diction('', color)

def main():

    person = ''
    color = False

    print(
'''
-----------------------------------------
|                  사전                 |
-----------------------------------------
''')
    
    print('   로그인    ⚪ 비회원', end = '', flush = True)

    click = False

    while True:
        
        event = False

        keyboard.read_key(suppress=True)

        event = keyboard.read_event(suppress=True)

        if event.name == 'enter' or event.name == 'return':
            if click == True:
                person = login()

                if person == '':
                    continue

                else:
                    break

        elif event.name == 'left' or event.name == 'right':
            if click == True:
                click = False
                print('\r   로그인    ⚪ 비회원', end = '')

            else:
                click = True
                print('\r⚪ 로그인       비회원', end = '')

    print(
'''
-----------------------------------------
|                  설정                 |
-----------------------------------------
''')
    
    print('   색 있음    ⚪ 색 없음', end = '', flush = True)

    click = False

    while True:
        
        event = False

        keyboard.read_key(suppress=True)

        event = keyboard.read_event(suppress=True)

        if event.name == 'enter' or event.name == 'return':
            if click == True:
                color = True

            else:
                color = False

            break

        elif event.name == 'left' or event.name == 'right':
            if click == True:
                click = False
                print('\r   색 있음    ⚪ 색 없음', end = '')

            else:
                click = True
                print('\r⚪ 색 있음       색 없음', end = '')

    if person == '':
        dictionary(False, '', color)

    else:
        dictionary(True, person, color)
    
main()