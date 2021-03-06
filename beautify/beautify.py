import os
from random import choice
from time import sleep
from timeit import default_timer
from art import *
from shell import shell
from stringcolor import cs
from bs4 import BeautifulSoup
from requests import get
from zipfile import ZipFile
from shutil import move

def download_banner():
    req = get('https://github.com/ExsoKamabay/kmy-beautify/blob/main/beautify/banner.zip')
    if req.status_code == 200:
        soup = BeautifulSoup(req.content,'html.parser')
        link = soup.find('a',id='raw-url')['data-permalink-href']
        req1 = get(f'https://github.com{link}')
        try:
            open('banner.zip','wb').write(req1.content)
            zp = ZipFile(f'banner.zip')
            zp.extractall()
            zp.close()
            os.remove(f'banner.zip')
        except:pass
        if os.name == 'nt':
            print(cs('memindahkan banner ke -> C:/user','blue'))
            move('banner','C:/user')
        else:
            print(cs('memindahkan banner ke -> /usr','blue'))
            try:
                move('banner', '/usr')
            except:
                os.system('sudo mv banner /usr')
    else:
        print(f'Error response {req.status_code}')

def path_banner():
    if os.name == 'nt':
        if 'banner' in shell('dir C:/user').output():pass
        else:
            print(cs('download banner..','blue'))
            download_banner()
            print(cs('selesai..','blue'))
        return 'C:/user/banner/'
    else:
        if 'banner' in shell('ls /usr').output():pass
        else:
            print(cs('download banner..','blue'))
            download_banner()
            print(cs('selesai..','blue'))
        return '/usr/banner/'

def clear():
    if os.name == 'nt':os.system('cls')
    else:os.system('clear')

class Loading:
    def __init__(self):
        global color,bg_color;
        color = None;
        bg_color = None;

    def loading(self,timeout:int or float=0.5,clor:str='blue',bg:str=None):
        '''
        timeout -> int/float -> default 0.5
        clor -> str -> default blue
        bg -> str -> default None
        '''
        global color,bg_color;
        color = clor;
        bg_color = bg;
        def distv(c,b):
            for i in range(5):
                clear()
                dsview = f"{text2art(f'{i+1*5}0%','fancy5')} {art(f'loading{i+1}')} {text2art('loading...','fancy90')}"
                print(cs(dsview, c,b))
                sleep(timeout)
        distv(color, bg_color)

    def show(self,callback):
        '''
        return callback
        '''
        self.strt = default_timer()
        self.callback = callback
        self.stop = default_timer()
        clear()
        dsview = f"{text2art('100%','fancy5')} {art('loading6')} {text2art('complete!','fancy90')}"
        print(cs(dsview, color,bg_color))
        sleep(float(f'{self.strt - self.stop}'.strip('-')))
        clear()
        return self.callback;


class Beautify:
    
    def colors(self,random:bool=False) -> bool:
        '''
        random -> type boolean
        True -> return random color
        False -> return list color
        '''
        if random == True:
            return choice((
                'blue', 'blueviolet', 'lightblue', 'lightseagreen', 'limegreen', 
                'magenta', 'maroon', 'mediumseagreen', 'mediumslateblue', 'orange', 
                'orangered', 'olivedrab', 'cyan', 'crimson', 'saddlebrown', 'darkcyan', 
                'darkgreen', 'darkolivegreen', 'darkslategrey', 'darkturquoise', 
                'darkviolet', 'darkgrey', 'darkorchid'))
        else:
            return (
                'blue', 'blueviolet', 'lightblue', 'lightseagreen', 'limegreen', 
                'magenta', 'maroon', 'mediumseagreen', 'mediumslateblue', 'orange', 
                'orangered', 'olivedrab', 'cyan', 'crimson', 'saddlebrown', 'darkcyan', 
                'darkgreen', 'darkolivegreen', 'darkslategrey', 'darkturquoise', 
                'darkviolet', 'darkgrey', 'darkorchid')

    def txtclr(self,text:str='hello worlds!',color='#00e6e6',bg=None,**kwargs):
        '''
        text color params:
        text -> type str -> default "hello worlds!"
        color -> type str 
        bg -> type str 
        font -> type str -> view font list https://github.com/sepandhaghighi/art/blob/master/FontList.ipynb - https://www.4r7.ir/FontList.html
        chr_ignore -> boolean
        sep -> type str -> separator
        decoration -> view decoration list https://github.com/sepandhaghighi/art/blob/master/DecorList.ipynb - https://www.4r7.ir/DecorList.html
        '''
        if not kwargs.keys():
            return cs(text2art(text,'fancy90'), color,bg)
        else:
            if 'font' in kwargs.keys():
                return cs(text2art(text,**kwargs), color,bg)
            else:
                return cs(text2art(text,'fancy90',**kwargs), color,bg)

    def banner(self,name:str='eagle2',color:str='blue',bg:str=None) -> str:
        try:
            with open(f'{path_banner()}{name}.txt','r') as f:
                return cs(f.read(), color,bg)
        except:
            return NameError(f'Invalid {name}!')

    def menu(self,add_menu:list[str]=None,separator='*',rw_num=True,color:str='white',bg:str=None,font=None):
        '''
        Params:
        add_menu -> type list -> default None
        separator -> type str -> default *
        rw_num -> type boolean -> default True
        color -> type str -> default white,available hex/rgb/name color
        bg -> type str -> default None,available hex/rgb/name color
        '''
        self.line = [];
        if add_menu == None:print(cs('please add menu!','red'))
        else:
            self.result = {}
            for i in add_menu:self.line.append(len(i))
            self.separator = f'{separator*sorted(self.line)[-1]*2}';
            print(cs(f'\n{self.separator}',color,bg))
            for (i,d) in enumerate(add_menu):
                if rw_num == True:
                    abstr = f'0{i+1} - {d}'.title()
                    absbr = f'{i+1} - {d}'.title()
                    if i+1 < 10:
                        self.result[f'0{i+1}'] = d
                        rst = int(len(self.separator)) - int(len(abstr)) - 1
                        try:
                            if font == None:
                                print(cs(f'{abstr}'+' '*rst+'|', color,bg))
                            else:
                                print(cs(text2art(f'{abstr}'+' '*rst+'|',font), color,bg))
                        except:
                            print(f'Invalid font {font}')
                    else:
                        self.result[f'{i+1}'] = d
                        rst = int(len(self.separator)) - int(len(absbr)) - 1
                        if font == None:
                            print(cs(f'{absbr}'+' '*rst+'|', color,bg))
                        else:
                            print(cs(text2art(f'{absbr}'+' '*rst+'|',font), color,bg))
                else:
                    try:
                        if font == None:
                            print(cs(d, color,bg))
                        else:
                            print(cs(text2art(d,font),color,bg))
                    except:
                        print(f'Invalid font {font}')
                print(cs(self.separator,color,bg))
            return self.result;

