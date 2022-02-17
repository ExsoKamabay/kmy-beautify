# kmy-beautify

```python
pip install kmy-beautify
```
[https://pypi.org/project/kmy-beautify/](https://pypi.org/project/kmy-beautify/)

## [how to use!](https://www.youtube.com/watch?v=vmDmQvQ00D4)

[font](https://www.4r7.ir/FontList.html) - [decoration](https://www.4r7.ir/DecorList.html) - [banner](list_banners_name)


```python
ld = Loading()#class
ld.loading(timeout:int or float)
ld.show('hello world')

bf = Beautify()#class
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
