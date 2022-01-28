# kmy-beautify

``beautify`` allows us to add color to text, banners, menu options in the terminal application

```python
# install requirements
pip3 install art==4.8 string-color==1.2.1
```

## [how to use!](https://www.youtube.com/watch?v=vmDmQvQ00D4)

```python
'''
 create a working directory & move the beautify package to your working directory!
 
working directory |
      | -> beautify     |> directory package 
      | -> testing.py   |> create your working file outside the `beautify` package directory
'''
```
<hr>

# Parameters
``ld = Loading()``

``ld.loading(timeout:int or float)``

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
 
