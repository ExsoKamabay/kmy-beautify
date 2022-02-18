# kmy-beautify

``beautify`` allows us to add color to text, banners, menu options in the terminal application

```python
pip install kmy-beautify
```
[https://pypi.org/project/kmy-beautify/](https://pypi.org/project/kmy-beautify/)

## [how to use!](https://www.youtube.com/watch?v=vmDmQvQ00D4)

[font](https://www.4r7.ir/FontList.html) - [decoration](https://www.4r7.ir/DecorList.html) - [list banner name](https://github.com/ExsoKamabay/kmy-beautify/blob/main/list_banners_name)

## Example

```python
from beautify import Beautify,Loading

Bf = Beautify()
Ld = Loading()

menu = (
    'home',
    'about',
    'contact',
    'check for update'
)

# loading
Ld.loading(0.2)
Bf.menu(Ld.show(menu),color='cyan',font='fancy102')

# banner menu
print(Bf.banner('wolf1',color=Bf.colors(random=True)))

# text color
print(Bf.txtclr(str(menu),color=Bf.colors(random=True)))

```

# ``parameters``

```python
ld = Loading()
ld.loading(timeout:int or float)
ld.show('hello world')

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
bf.banner(name:color,bg) --> str
# list banner name https://github.com/ExsoKamabay/kmy-beautify/blob/main/list_banners_name
bf.menu(
    add_menu:list,
    separator:str,
    rw_num:bool,
    color:str,
    bg:str,
    font:str)
```
