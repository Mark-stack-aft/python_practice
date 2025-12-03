import json
from dict_mod import *
from traceback import format_exc
import keyboard
from orign_dic import orign_dic
import colorama
from colorama import Fore, Back, Style
import socket
import googletrans
import langid
from termcolor import colored
import argostranslate.package
import argostranslate.translate
from tkinter import *
import time
import threading

tk = Tk()
# tk.attributes('-fullscreen', True)
tk.title('사전')
icon_path = '06.딕셔너리/dic_gui/dict.png'
icon_image = PhotoImage(file = icon_path)
tk.iconphoto(True, icon_image)
tk.iconbitmap('06.딕셔너리/dic_gui/dict.ico')
tk.state('zoomed')
tk.resizable(False, False)

def find():
    global dic
    
    find_wd = str(search_input.get())

    if bool(find_wd):
        found['text'] = f'\'{find_wd}\' 단어를 찾는 중입니다...'

        def finding(): 
            found_now = find_mod(find_wd, dic)

            found['text'] = f'<\'{find_wd}\' 단어>'

            text_widget.config(state = 'normal')

            text_widget.delete('1.0', 'end')

            text_widget.insert('end', found_now)

            lenth1 = max([len(lenth) for lenth in found_now.split('\n')])
            lenth2 = found_now.count('\n') + 1

            text_widget.configure(width = lenth1, height = lenth2)

            # lines = text_widget.count("1.0", "end", "displaylines")[0]
            
            # text_widget.configure(height = lines if lines > 0 else 1, width = lenth1)

            text_widget.config(state = 'disabled')

        thread = threading.Thread(target=finding, daemon=True)
        thread.start()

    else:
        found['text'] = '단어 대기 중...'
        text_widget.config(state = 'normal')
        text_widget.delete('1.0', 'end')
        text_widget.configure(width = 5, height = 1)
        text_widget.config(state = 'disabled')

def find_kw():
    global dic
    
    find_kw_wd = str(search_kw_input.get())

    if bool(find_kw_wd):
        found_kw['text'] = f'\'{find_kw_wd}\' 키워드가 들어간 단어를 찾는 중입니다...'

        def finding_kw():
            
            text_widget_kw.config(state = 'normal')

            text_widget_kw.delete('1.0', 'end')

            found_now = find_kw_mod(find_kw_wd, dic)

            found_kw['text'] = f'<\'{find_kw_wd}\' 키워드가 들어간 단어>'

            lenth1 = max([len(lenth) for lenth in found_now.split('\n')]) + 20
            lenth2 = found_now.count('\n') + 1

            text_widget_kw.configure(width = lenth1, height = lenth2)

            for ind1 in found_now.split('\n'):
                for ind2 in range(len(ind1.split(find_kw_wd))):
                    text_widget_kw.insert('end', ind1.split(find_kw_wd)[ind2])
                    if not ind2 == len(ind1.split(find_kw_wd)) - 1:
                        text_widget_kw.insert('end', find_kw_wd, 'colored_tag')

                text_widget_kw.insert('end', '\n')
                    
            text_widget_kw.tag_configure('colored_tag', foreground = 'red')

            lines = text_widget_kw.count("1.0", "end", "displaylines")[0]
            
            text_widget_kw.configure(height = lines if lines > 0 else 1, width = lenth1)

            text_widget_kw.config(state = 'disabled')

        thread = threading.Thread(target=finding_kw, daemon=True)
        thread.start()

    else:
        found_kw['text'] = '단어 대기 중...'
        text_widget.config(state = 'normal')
        text_widget_kw.delete('1.0', 'end')
        text_widget_kw.configure(width = 5, height = 1)
        text_widget_kw.config(state = 'disabled')
    

with open(r'06.딕셔너리/dic_gui/dic.json', 'r') as file_dic:
    dic_ = json.load(file_dic)
    dic = dic_['']

Label(tk, text = '사전', bg = 'green', fg = 'white', font = (100)).pack(expand = True)
Label(tk, text = '-' * 40).pack(side = 'top', expand = True)

found = Label(tk, text = '단어 대기 중...', bg = 'cyan', fg = 'black')
text_widget = Text(tk, height = 1, width = 5, wrap = "word", bg = 'black', fg = 'white', relief = "flat", highlightthickness = 0)

search_label = Label(tk,text = '검색', bg = 'cyan', fg = 'black')
search_label.pack(expand = True)
search_input = Entry(tk)
search_input.pack(expand = True)
search_button = Button(tk, text = '🔍', command = find)
search_button.pack(expand = True)

found.pack(expand = True)
text_widget.pack(expand = True, padx = 20, pady = 20)

found_kw = Label(tk, text = '단어 대기 중...', bg = 'black', fg = 'white')
text_widget_kw = Text(tk, height = 1, width = 5, wrap = "word", bg = 'black', fg = 'white', relief = "flat", highlightthickness = 0)

search_kw_label = Label(tk,text = '키위드 검색', bg = 'black', fg = 'white')
search_kw_label.pack(expand = True)
search_kw_input = Entry(tk)
search_kw_input.pack(expand = True)
search_kw_button = Button(tk, text = '🔍', command = find_kw)
search_kw_button.pack(expand = True)

found_kw.pack(expand = True)
text_widget_kw.pack(expand = True, padx = 20, pady = 20)

tk.mainloop()

argostranslate.package.update_package_index()
available_packages = argostranslate.package.get_available_packages()
package_to_install = next(
    filter(
        lambda x: x.from_code == 'ko' and x.to_code == 'en',
        available_packages
    )
)
argostranslate.package.install_from_path(package_to_install.download())

def has_modul():
    modul = True
    try:
        keyboard.is_pressed('a')
        colorama.init()
        langid.classify('모듈이 있는가')
        print(colored('모듈 설치 여부를 확인 중입니다...', 'red', attrs = ['bold']))
        tran = googletrans.Translator().translate(text = '모듈 설치 여부를 확인 중입니다...', dest = 'en', src = 'auto')
        print(tran.text)
        translatedText = argostranslate.translate.translate(q = "모듈 설치 여부를 확인 중입니다...", from_code = 'ko', to_code = 'en')
        print(translatedText)
        check_internet()

    except ImportError:
        modul = False

    return modul

def make():
    with open(r'06.딕셔너리/person.json', 'r') as file:
        persons = json.load(file)

    print()
    print('---회원가입---')
    
    try:
        while True:
            new_id = input('아이디 : ')
            
            if len(new_id) >= 10:
                break
            else:
                print('아이디의 길이는 10자 이상이여야 합니다.')
                continue
            
            if new_id in persons.keys():
                print('이미 있는 아이디 입니다.')
                continue
            else:
                break

        while True:
            new_password = input('비밀번호 : ')
            
            if len(new_id) >= 10:
                break
            else:
                print('비밀번호의 길이는 10자 이상이여야 합니다.')
                continue

        persons[new_id] = new_password

        with open(r'06.딕셔너리/person.json', 'w') as file:
            json.dump(persons, file, indent = 2)

        with open(r'06.딕셔너리/dic.json', 'r') as file1:
            dic_ = json.load(file1)

        person = new_id
        dic_[person] = orign_dic

        with open(r'06.딕셔너리/dic.json', 'w') as file2:
            json.dump(dic_, file2, indent = 2)

    except KeyboardInterrupt:
        print('\n회원가입이 취소되었습니다.')

    return person

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
                if click :
                    person = make()
                            
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
    with open(r'06.딕셔너리/dic.json', 'r') as file_dic:
            dic_ = json.load(file_dic)
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
                        dic = plus_mod(dic, color)

                    elif func == '2':
                        dic = delete_mod(dic, color)

                    elif func == '3':
                        dic = correct_mod(dic, color)

                    elif func == '000':
                        dic = dic_clear_mod(dic, color)
                                
                    elif func == '4':

                        find_wd = input(Back.CYAN + '단어나 뜻을 입력하세요 : ' + Style.RESET_ALL)

                        func, dic = find(find_wd, dic, color)

                    elif func == '5':

                        key_word = input(Back.BLACK + Fore.WHITE + '키워드를 입력하세요 : ' + Style.RESET_ALL)

                        func, dic = find_kw_mod(key_word, dic, color)

                    elif func == '6':

                        tr_str = input(Back.LIGHTBLACK_EX + Fore.LIGHTWHITE_EX + '번역할 것을 입력하세요 : ' + Style.RESET_ALL)
                        trans_mod(tr_str, color)


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
                        dic = plus_mod(dic, color)

                    elif func == '2':
                        dic = delete_mod(dic, color)

                    elif func == '3':
                        dic = correct_mod(dic, color)

                    elif func == '000':
                        dic = dic_clear_mod(dic, color)
                                
                    elif func == '4':

                        find_wd = input('단어나 뜻을 입력하세요 : ')

                        func, dic = find(find_wd, dic, color)

                    elif func == '5':

                        key_word = input('키워드를 입력하세요 : ')

                        func, dic = find_kw_mod(key_word, dic, color)

                    elif func == '6':

                        tr_str = input('번역할 것을 입력하세요 : ')
                        trans_mod(tr_str, color)


                    else:
                        print('잘못 입력하였습니다.')

            except KeyboardInterrupt:
                print('\n종료합니다.')

            except:
                print('\n오류가 발생했습니다. | 오류 : %s' % format_exc().split('\n')[-2])

    finally:
        if not person == '':
            dic_[person] = dic

            with open(r'06.딕셔너리/dic.json', 'w') as file_dict:
                json.dump(dic_, file_dict, indent = 2)

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
            if click:
                person = login()

                if person == '':
                    print('   로그인    ⚪ 비회원', end = '', flush = True)
                    continue

                else:
                    break

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
    
def main_page():
    try:
        clear_screen()
        if has_modul():
            main()

        else:
            print('모듈이 설치되어 있지 않습니다. 모듈을 설치하시겠습니까? (1 : 네, 2 : 아니오) : ')
            answer = input()
            
            if answer == '1':
                print('모듈을 설치합니다.')
                os.system('pip install keyboard')
                os.system('pip install colorma')
                os.system('pip install langid')
                os.system('pip install termcolor')
                os.system('pip install googletrans==4.0.0-rc1')
                os.system('pip install socket')

            elif answer == '2':
                raise KeyboardInterrupt
            
            else:
                print('잘못 입력하셨습니다.')
                main_page()

    except KeyboardInterrupt:
        print('\n종료합니다.')

    except:
        print()