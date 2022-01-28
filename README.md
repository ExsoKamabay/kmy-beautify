# kmy-beautify

``beautify`` allows us to add color to text, banners, menu options in the terminal application
## ``start work with beautify!``
download the package in repository, before use we need to download the requirements in ``beautify/requirements.txt`` with command ``'pip install -r beautify/requirements.txt'`` ``adjust pip command which is in python3.x.x`` if you are in ``kmy-beautify`` directory

## [how to use!](https://www.youtube.com/watch?v=vmDmQvQ00D4)

```python
'''
 create a working directory & move the beautify package to your working directory!
 
working directory |
      | -> beautify     |> directory package 
      | -> testing.py   |> create your working file outside the `beautify` package directory
      
      
      
in the testing.py file import the class from the beautify package.
'''
from beautify import Beautify,Loading
```
<hr>

# Parameters
``ld = Loading()``

``ld.loading(timeout)``

``ld.show(callback)``return callback

<hr>

``bf = Beautify()``

``bf.txtclr(
 text:str,
 color:str,
 bg:str,
 font:str,
 chr_ignore:boolean,
 sep:str,
 decoration:str)``
 [font](https://www.4r7.ir/FontList.html) - [decoration](https://www.4r7.ir/DecorList.html)
 
 ``bf.colors(random:boolean)``
 
 ``bf.banner(name,color,bg)`` [banner name](list_banners_name)
 
 ``bf.print_menu(add_menu:list,separator:str,rw_num:boolean,color:str,bg:str)``
 
