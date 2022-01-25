# kmy-beautify

``beautify`` allows us to add color to text, banners, menu options in the terminal application
## ``start work with beautify!``
download the package in repository, before use we need to download the requirements in ``beautify/requirements.txt`` with command ``'pip install -r beautify/requirements.txt'`` ``adjust pip command which is in python3.x.x`` if you are in ``kmy-beautify`` directory

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

## ```Help```

```python
class Beautify(builtins.object)
 |  Methods defined here:
 |  
 |  banner(self, name: str = 'eagle2', color: str = 'blue', bg: str = None) -> str
 |  
 |  colors(self, random: bool = False) -> bool
 |      random -> type boolean
 |      True -> return random color
 |      False -> return list color
 |  
 |  print_menu(self, add_menu: list = None, separator='*', rw_num=True, color: str = 'white', bg: str = None)
 |      Params:
 |      add_menu -> type list -> default None
 |      separator -> type str -> default *
 |      rw_num -> type boolean -> default True
 |      color -> type str -> default white,available hex/rgb/name color
 |      bg -> type str -> default None,available hex/rgb/name color
 |  
 |  txtclr(self, text: str = 'hello worlds!', color='#00e6e6', bg=None, **kwargs)
 |      text color params:
 |      text -> type str -> default "hello worlds!"
 |      color -> type str 
 |      bg -> type str 
 |      font -> type str -> view font list https://github.com/sepandhaghighi/art/blob/master/FontList.ipynb - https://www.4r7.ir/FontList.html
 |      chr_ignore -> boolean
 |      sep -> type str -> separator
 |      decoration -> view decoration list https://github.com/sepandhaghighi/art/blob/master/DecorList.ipynb - https://www.4r7.ir/DecorList.html
 |  
 |  ----------------------------------------------------------------------


class Loading(builtins.object):
 |  loading(self, timeout: int = 0.5, clor: str = 'blue', bg: str = None)
 |      timeout -> int/float -> default 0.5
 |      clor -> str -> default blue
 |      bg -> str -> default None
 |  
 |  show(self, callback)
 |      callback value to be loaded, returns callback

```
