import langid
import keyboard
from password import get_password
import os
from termcolor import colored
import googletrans
import socket
import colorama
from colorama import Fore, Back, Style
import re

colorama.init()

no_blank = re.compile('\S+')

def check_internet(host="8.8.8.8", port=53, timeout=5):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error as ex:
        return False

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    
    else:
        os.system('clear')

def auto_find_mod(dic, auto_wd):
    if check_internet():
        plus_wd = trans_mod(auto_wd)

        if not (langid.classify(auto_wd)[0] == 'ko' and langid.classify(plus_wd)[0] == 'ko') or not (langid.classify(auto_wd)[0] == 'en' and langid.classify(plus_wd)[0] == 'en'):
            if langid.classify(auto_wd)[0] == 'en' and langid.classify(plus_wd)[0] == 'ko':
                dic[auto_wd] = plus_wd

            elif langid.classify(auto_wd)[0] == 'ko' and langid.classify(plus_wd)[0] == 'en':
                dic[plus_wd] = auto_wd

    else:
        print(Back.LIGHTRED_EX + '인터넷이 연결 되어 있지 않음 -> 오토 추가 기능 사용 불가' + Style.RESET_ALL)

def plus_mod(dic):
    key = input(Back.LIGHTGREEN_EX + '추가할 단어를 입력하세요 : ' + Style.RESET_ALL)

    if not key in dic.keys() and bool(key == no_blank.search(key)):
        value = input(Back.LIGHTGREEN_EX + '뜻 : ' + Style.RESET_ALL)
        
        if not value in dic.keys() and bool(value == no_blank.search(value)):
            if langid.classify(key)[0] == 'en' and langid.classify(value)[0] == 'ko':
                dic[key] = value
                print(Back.LIGHTGREEN_EX + '추가되었습니다.', f': {key}, {value}' + Style.RESET_ALL)


            elif langid.classify(key)[0] == 'ko' and langid.classify(value)[0] == 'en':
                dic[value] = key
                print(Back.LIGHTGREEN_EX + '추가되었습니다.', f': {key}, {value}' + Style.RESET_ALL)

            else:
                print(Back.LIGHTYELLOW_EX + '영/한 구조가 아닙니다!' + Style.RESET_ALL)

        else:
            print(Back.LIGHTYELLOW_EX + '단어가 이미 있거나 공백이 있습니다!' + Style.RESET_ALL)
    
    else:
        print(Back.LIGHTYELLOW_EX + '단어가 이미 있거나 공백이 있습니다!' + Style.RESET_ALL)

    return dic

def delete_mod(dic):
    key = input(Back.MAGENTA + '삭제할 단어를 입력하세요 : ' + Style.RESET_ALL)

    if langid.classify(key)[0] == 'en':
        if key in dic:
            dic.pop(key)
            print(Back.MAGENTA + '삭제되었습니다.', f': {key}' + Style.RESET_ALL)

        else:
            print(Back.LIGHTYELLOW_EX + '오류! 삭제할 단어가 없습니다!' + Style.RESET_ALL)

    elif langid.classify(key)[0] == 'ko':
        if key in dic.values():
            dic.pop(list(dic.keys())[list(dic.values()).index(key)])
            print(Back.MAGENTA + '삭제되었습니다.', f': {key}' + Style.RESET_ALL)

        else:
            print(Back.LIGHTYELLOW_EX + '오류! 삭제할 단어가 없습니다!' + Style.RESET_ALL)

    else:
        print(Back.LIGHTYELLOW_EX + '오류! 삭제할 단어가 없습니다!' + Style.RESET_ALL)

    return dic

def correct_mod(dic):
    key = input(Back.LIGHTBLUE_EX + '수정할 단어를 입력하세요 : ' + Style.RESET_ALL)

    key_value = key
    found_list_wd, found_list_def = [], []
    attrs = ['bold']
    num = 0

    if langid.classify(key_value)[0] == 'en':
        for indx in range(len(dic)):
            if key_value == list(dic.keys())[indx]:
                found_list_wd.append(list(dic.keys())[indx])
                found_list_def.append(list(dic.values())[indx])
                num = num + 1

        if num > 0:
            for printing in range(num):
                print(Back.LIGHTBLUE_EX + f'{printing}. 단어 : {found_list_wd[printing]}, 뜻 : {found_list_def[printing]}'  + Style.RESET_ALL)

        else:
            print(Back.LIGHTYELLOW_EX + '오류! 수정할 단어가 없습니다!' + Style.RESET_ALL)

    elif langid.classify(key_value)[0] == 'ko':
        for indx in range(len(dic)):
            if key_value == list(dic.values())[indx]:
                found_list_def.append(list(dic.values())[indx])
                found_list_wd.append(list(dic.keys())[indx])
                num = num + 1

        if num > 0:
            for printing in range(num):
                print(Back.LIGHTBLUE_EX + f'{printing}. 단어 : {found_list_wd[printing]}, 뜻 : {found_list_def[printing]}' + Style.RESET_ALL)

        else:
            print(Back.LIGHTYELLOW_EX + '오류! 수정할 단어가 없습니다!' + Style.RESET_ALL)

    if num > 0:
        try:
            select = int(input(Back.LIGHTBLUE_EX + '수정하고자 하는 단어의 번호를 입력하세요 : ' + Style.RESET_ALL))

        except:
            print(Back.LIGHTYELLOW_EX + '잘못 입력되었습니다.' + Style.RESET_ALL)
            pass
            
        else:
            if num >= select >= 0:
                re_key = input(Back.LIGHTBLUE_EX + '수정할 단어의 수정된 단어를 입력하세요 : ' + Style.RESET_ALL)
                re_value = input(Back.LIGHTBLUE_EX + '수정할 단어의 수정된 뜻을 입력하세요 : ' + Style.RESET_ALL)

                if langid.classify(re_key)[0] == 'en' and langid.classify(re_value)[0] == 'ko':
                    dic.pop(found_list_wd[select])
                    dic[re_key] = re_value
                    print(Back.LIGHTBLUE_EX + f'수정되었습니다. {key} => {re_key}, {re_value}' + Style.RESET_ALL)

                elif langid.classify(re_key)[0] == 'ko' and langid.classify(re_value)[0] == 'en':
                    dic.pop(found_list_wd[select])
                    dic[re_value] = re_key
                    print(Back.LIGHTBLUE_EX + f'수정되었습니다. {key} => {re_key}, {re_value}' + Style.RESET_ALL)

                else:
                    print(Back.LIGHTYELLOW_EX + '영/한 구조가 아닙니다!' + Style.RESET_ALL)

    return dic

def dic_clear_mod(dic):
    print(Back.RED + '정말로 삭제하시겠습니까? : ' + Style.RESET_ALL)
    print(Back.RED + '   네    ⚪ 아니오'  + Style.RESET_ALL, end = '', flush = True)

    click = False

    while True:
        
        event = False

        keyboard.read_key(suppress=True)

        event = keyboard.read_event(suppress=True)

        if event.name == 'enter' or event.name == 'return':
            if click == True:

                password = input(Back.RED + '\n비밀번호 : ' + Style.RESET_ALL)

                if password == get_password:
                    dic.clear()
                    print(Back.RED + '\n완료되었습니다.' + Style.RESET_ALL)

                else:
                    print(Back.RED + '\n비밀번호가 틀렸습니다.' + Style.RESET_ALL)
                        
            else:
                print(Back.RED + '\n취소되었습니다.' + Style.RESET_ALL)

            break

        elif event.name == 'left' or event.name == 'right':
            if click == True:
                click = False
                print(Back.RED + '\r   네  ⚪ 아니오      ' + Style.RESET_ALL, end = '')

            else:
                click = True
                print(Back.RED + '\r⚪ 네     아니오      ' + Style.RESET_ALL, end = '')

    return dic

def find_mod(find_wd, dic):
    key_value = find_wd
    found_list = []

    if langid.classify(key_value)[0] == 'en':
        if key_value in dic.keys():
            found_list.append(f'단어 : {key_value}, 뜻 : {dic[key_value]}')

        else:
            found_list = ['단어가 없습니다!']
            # auto_find_mod(dic, key_value)

    elif langid.classify(key_value)[0] == 'ko':

        found_list_wd, found_list_def = [], []
        num = 0

        if key_value in dic.values():
            
            for indx in range(len(dic)):
                if key_value in list(dic.values())[indx].split(','):
                    found_list_def.append(list(dic.values())[indx])
                    found_list_wd.append(list(dic.keys())[indx])
                    num = num + 1

            if num > 0:
                for printing in range(num):
                    found_list.append(f'단어 : {found_list_wd[printing]}, 뜻 : {found_list_def[printing]}')
            
        else:
            found_list = ['단어가 없습니다!']
            # auto_find_mod(dic, key_value)

    found = '\n'.join(found_list)

    return found

def find_kw_mod(key_word, dic):
    key_value = key_word
    found_list_wd, found_list_def, found_list = [], [], []
    num = 0

    if langid.classify(key_value)[0] == 'en':
        for indx in range(len(dic)):
            if key_value in list(dic.keys())[indx]:
                found_list_wd.append(list(dic.keys())[indx])
                found_list_def.append(list(dic.values())[indx])
                num = num + 1

        if num > 0:
            for printing in range(num):
                found_list.append(f'단어 : {found_list_wd[printing]}, 뜻 : {found_list_def[printing]}')

        else:
            found_list.append('단어가 없습니다!')

    elif langid.classify(key_value)[0] == 'ko':
        for indx in range(len(dic)):
            if key_value in list(dic.values())[indx]:
                found_list_def.append(list(dic.values())[indx])
                found_list_wd.append(list(dic.keys())[indx])
                num = num + 1

        if num > 0:
            for printing in range(num):
                found_list.append(f'단어 : {found_list_wd[printing]}, 뜻 : {found_list_def[printing]}')

        else:
            found_list.append('단어가 없습니다!')

    found = '\n'.join(found_list)

    return found

def trans_mod(in_str):
    if check_internet():
        if langid.classify(in_str)[0] == 'ko':
            out_str = googletrans.Translator().translate(in_str, dest = 'en', src = 'auto')

        elif langid.classify(in_str)[0] == 'en':
            out_str = googletrans.Translator().translate(in_str, dest = 'ko', src = 'auto')

        print(Back.LIGHTBLACK_EX + Fore.LIGHTWHITE_EX + f'{in_str} : 번역됨 -> {out_str.text}' + Style.RESET_ALL)

        return out_str.text
    
    else:
        print(Back.LIGHTRED_EX + '인터넷 연결이 되어있지 않아서, 번역이 불가능 합니다.' + Style.RESET_ALL)

        

# cm2ft = entry2.get()
# entry1.delete(0,"end")
# entry1.insert(0,round(float(cm2ft)/30.48,4))