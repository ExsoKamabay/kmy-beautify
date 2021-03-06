# kmy-beautify

``beautify`` allows us to add color to text, banners, menu options in the terminal application

```python
pip install kmy-beautify
```
[https://pypi.org/project/kmy-beautify/](https://pypi.org/project/kmy-beautify/)

## 👉  [Tutorial!](https://www.youtube.com/watch?v=2pkcNTJrpNQ) 👈

[font](https://www.4r7.ir/FontList.html) - [decoration](https://www.4r7.ir/DecorList.html) - [list banner name](https://github.com/ExsoKamabay/kmy-beautify/blob/main/list_banners_name)

## Example

```python
from beautify import Beautify,Loading
from time import sleep as timeout

Bf = Beautify()
Ld = Loading()

menu_options = (
    'home',
    'about',
    'contact',
    'check for update'
)

# loading menu_options
Ld.loading(0.2)
timeout(3)
Bf.menu(Ld.show(menu_options),color='cyan',font='fancy102')

# banner menu_options
print(Bf.banner('wolf1',color=Bf.colors(random=True)))

# text color
print(Bf.txtclr(str(menu_options),color=Bf.colors(random=True)))

```

# ``parameters``

```python
ld = Loading()
ld.loading(timeout:int or float) # time load
ld.show('hello world') # loaded value

bf = Beautify()
bf.txtclr(
    text:str,
    color:str,
    bg:str,
    font:str,
    chr_ignore:boolean,
    sep:str,
    decoration:str)
bf.colors(random:bool)
bf.banner(name,color,bg) --> str
# list banner name https://github.com/ExsoKamabay/kmy-beautify/blob/main/list_banners_name
bf.menu(
    add_menu:list,
    separator:str,
    rw_num:bool,
    color:str,
    bg:str,
    font:str)
```
