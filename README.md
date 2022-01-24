# kmy-beautify

```python
pip install kmy-beautify
```
[https://pypi.org/project/kmy-beautify/](https://pypi.org/project/kmy-beautify/)

``beautify`` allows us to add color to text, banners, menu options in the terminal application
<hr>

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

<hr>

```python
Python 3.9.2 (default, Feb 28 2021, 17:03:44) 
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from beautify import Beautify
>>> banner = Beautify().banner('wolf1')
>>> print(banner)

                                 ,ood8888booo,
                              ,od8           8bo,
                           ,od                   bo,
                         ,d8                       8b,
                        ,o                           o,    ,a8b
                       ,8                             8,,od8  8
                       8'                             d8'     8b
                       8                           d8'ba     aP'
                       Y,                       o8'         aP'
                        Y8,                      YaaaP'    ba
                         Y8o                   Y8'         88
                          `Y8               ,8"           `P
                            Y8o        ,d8P'              ba
                       ooood8888888P"""'                  P'
                    ,od                                  8
                 ,dP     o88o                           o'
                ,dP          8                          8
               ,d'   oo       8                       ,8
               $    d$"8      8           Y    Y  o   8
              d    d  d8    od  ""boooooooob   d"" 8   8
              $    8  d   ood' ,   8        b  8   '8  b
              $   $  8  8     d  d8        `b  d    '8  b
               $  $ 8   b    Y  d8          8 ,P     '8  b
               `$$  Yb  b     8b 8b         8 8,      '8  o,
                    `Y  b      8o  $$o      d  b        b   $o
                     8   '$     8$,,$"      $   $o      '$o$$
                      $o$$P"                 $$o$
```

<hr>

## Art Name for ```Beautify().banner(name,color,bg)```
```
eagle1
 
                               /T /I
                              / |/ | .-~/
                          T\ Y  I  |/  /  _
         /T               | \I  |  I  Y.-~/
        I l   /I       T\ |  |  l  |  T  /
     T\ |  \ Y l  /T   | \I  l   \ `  l Y
 __  | \l   \l  \I l __l  l   \   `  _. |
 \ ~-l  `\   `\  \  \\ ~\  \   `. .-~   |
  \   ~-. "-.  `  \  ^._ ^. "-.  /  \   |
.--~-._  ~-  `  _  ~-_.-"-." ._ /._ ." ./
 >--.  ~-.   ._  ~>-"    "\\   7   7   ]
^.___~"--._    ~-{  .-~ .  `\ Y . /    |
 <__ ~"-.  ~       /_/   \   \I  Y   : |
   ^-.__           ~(_/   \   >._:   | l______
       ^--.,___.-~"  /_/   !  `-.~"--l_ /     ~"-.
              (_/ .  ~(   /'     "~"--,Y   -=b-. _)
               (_/ .  \  :           / l      c"~o \
                \ /    `.    .     .^   \_.-~"~--.  )
                 (_/ .   `  /     /       !       )/
                  / / _.   '.   .':      /        '
                  ~(_/ .   /    _  `  .-<_
                    /_/ . ' .-~" `.  / \  \          ,z=.
                    ~( /   '  :   | K   "-.~-.______//
                      "-,.    l   I/ \_    __{--->._(==.
                       //(     \  <    ~"~"     //
                      /' /\     \  \     ,v=.  ((
                    .^. / /\     "  }__ //===-  `
                   / / ' '  "-.,__ {---(==-
                 .^ '       :  T  ~"   ll       
                / .  .  . : | :!        \\
               (_/  /   | | j-"          ~^
                 ~-<_(_.^-~"

                             
 


eagle2
                                                                __..-'
                                                         _.--''
                                               _...__..-'
                                             .'
                                           .'
                                         .'
                                       .'
            .------._                 ;
      .-"""`-.<')    `-._           .'
     (.--. _   `._       `'---.__.-'
      `   `;'-.-'         '-    ._
        .--'``  '._      - '   .
         `""'-.    `---'    ,
 ''--..__      `\
         ``''---'`\      .'
                  `'. '
                     `'.
 


eagle3
     ________________________
    `'-.,________,,..-  ___ \________
       > `'-.,_____,,.-`<_>\ )__     `\
         >            `'-._    _)____  \
          >          _.-'`  _______  `\ |
           >   _,,..--'''```       `'-.\|
          >-'``                        `'
 

wolf1
 
                                 ,ood8888booo,
                              ,od8           8bo,
                           ,od                   bo,
                         ,d8                       8b,
                        ,o                           o,    ,a8b
                       ,8                             8,,od8  8
                       8'                             d8'     8b
                       8                           d8'ba     aP'
                       Y,                       o8'         aP'
                        Y8,                      YaaaP'    ba
                         Y8o                   Y8'         88
                          `Y8               ,8"           `P
                            Y8o        ,d8P'              ba
                       ooood8888888P"""'                  P'
                    ,od                                  8
                 ,dP     o88o                           o'
                ,dP          8                          8
               ,d'   oo       8                       ,8
               $    d$"8      8           Y    Y  o   8
              d    d  d8    od  ""boooooooob   d"" 8   8
              $    8  d   ood' ,   8        b  8   '8  b
              $   $  8  8     d  d8        `b  d    '8  b
               $  $ 8   b    Y  d8          8 ,P     '8  b
               `$$  Yb  b     8b 8b         8 8,      '8  o,
                    `Y  b      8o  $$o      d  b        b   $o
                     8   '$     8$,,$"      $   $o      '$o$$
                      $o$$P"                 $$o$
 


wolf2
            _        _
          /\\     ,'/|
        _|  |\-'-'_/_/
   __--'/`           \
       /              \
      /        "o.  |o"|
      |              \/
       \_          ___\
         `--._`.   \;//
              ;-.___,'
             /
           ,'
        _-'
 


wolf3
                           ,     ,
                          |\---/|
                         /  , , |
                    __.-'|  / \ /
           __ ___.-'        ._O|
        .-'  '        :      _/
       / ,    .        .     |
      :  ;    :        :   _/
      |  |   .'     __:   /
      |  :   /'----'| \  |
      \  |\  |      | /| |
       '.'| /       || \ |
       | /|.'       '.l \\_
       || ||             '-'
       '-''-'
 


wolf4
                                __
                             .d$$b
                           .' TO$;\
                          /  : TP._;
                         / _.;  :Tb|
                        /   /   ;j$j
                    _.-"       d$$$$
                  .' ..       d$$$$;
                 /  /P'      d$$$$P. |\
                /   "      .d$$$P' |\^"l
              .'           `T$P^"""""  :
          ._.'      _.'                ;
       `-.-".-'-' ._.       _.-"    .-"
     `.-" _____  ._              .-"
    -(.g$$$$$$$b.              .'
      ""^^T$$$P^)            .(:
        _/  -"  /.'         /:/;
     ._.'-'`-'  ")/         /;/;
  `-.-"..--""   " /         /  ;
 .-" ..--""        -'          :
 ..--""--.-"         (\      .-(\
   ..--""              `-\(\/;`
     _.                      :
                             ;`-
                            :\
                            ;  
 


wolf5
       /^\      /^\
      |  \    /  |
      ||\ \../ /||
      )'        `(
     ,;`w,    ,w';,
     ;,  ) __ (  ,;
      ;  \(\/)/  ;;
     ;|  |vwwv|    ``-...
      ;  `lwwl'   ;      ```''-.
     ;| ; `""' ; ;              `.
      ;         ,   ,          , |
      '  ;      ;   l    .     | |
      ;    ,  ,    |,-,._|      \;
       ;  ; `' ;   '    \ `\     \;
       |  |    |  |     |   |    |;
       |  ;    ;  |      \   \   (;
       | |      | l       | | \  |
       | |      | |       | |  ) |
       | |      | ;       | |  | |
       ; ,      : ,      ,_.'  | |
      :__'      | |           ,_.'
               `--'


butterfly1
 
                                             _,.====.
                                          ,=". . . / /
                                       ,='. . . ..'.`
                           ==.      ,='. . . . ./ /
                     .       ,\.  ,'. . . . . ./ /
                     |       888,: . . . . . .| |
                     \       `88b . . . . . . | |
                      \.  ,"=,888._...........| |
                 .="""88b' ..,q88: . . . . :". `.
         __...-.-.-.-:Y88,/=="";L . . . . . . :. \
    ,-.": . ._,..-----d88.."'  ; . . . . . . . | |
   ( ( . .-': . . . .:q88=.` ' ;. . . . . . . .| |
    \_;-'. . . . ..'. .88J ` .; \. . . . . . ./ /
   ,: . . . . ..'. . . | ; ,  ;  \  . . . ._.'.'
 .:. . . . . .: . . . .| ;  . ;   \`------'_.'
/:. . . . . /. . . . . |; '  ;     `------'
\ `._,-. . /: . . . . .|;  . ;
 `-._,-.`-/: . . . . ._J; '  ;
        `-\ `-.__..--'_|;  ' ;
           `--.__..--'  ;l42 ; 


butterfly2
   _--_                                     _--_
/#()# #\         0             0         /# #()#\
|()##  \#\_       \           /       _/#/  ##()|
|#()##-=###\_      \         /      _/###=-##()#|
 \#()#-=##  #\_     \       /     _/#  ##=-#()#/
  |#()#--==### \_    \     /    _/ ###==--#()#|
  |#()##--=#    #\_   \!!!/   _/#    #=--##()#|
   \#()##---===####\   O|O   /####===---##()#/
    |#()#____==#####\ / Y \ /#####==____#()#|
     \###______######|\/#\/|######______###/
        ()#O#/      ##\_#_/##      \#O#()
       ()#O#(__-===###/ _ \###===-__)#O#()
      ()#O#(   #  ###_(_|_)_###  #   )#O#()
      ()#O(---#__###/ (_|_) \###__#---)O#()
      ()#O#( / / ##/  (_|_)  \## \ \ )#O#()
      ()##O#\_/  #/   (_|_)   \#  \_/#O##()
       \)##OO#\ -)    (_|_)    (- /#OO##(/
        )//##OOO*|    / | \    |*OOO##\\(
        |/_####_/    ( /X\ )    \_####_\|
       /X/ \__/       \___/       \__/ \X\
      (#/                               \#) 


butterfly3
      __....__                                           _..-'"`""+"'-.
   ."`.._____`"-._                                  _.-"__...-----\""'\
 ,'..._      '""-.`._                            _.'_."'       __..\---|
( :    "..__     _,'."-._                      ,'_.'__`.----""'     \ /
 . \        `",+'--.+`-..`.   o           o  .'-"   \  _.".-"''"""`"'/
  \"`.+"'----+----.'       `.  .        .' ,'       .'" ___"._____,'.
   \  .   __/......`.__      `. `.     ' ." __..--'"+'""     \    :-|
    \-:--"  :      /__ `'"-.._ \  \   / /.-'__..---""`."'----.\___; '
     .: _..+.--"'"/   `"--..__`_`. \ / /.-'"           `.     :   :7
     ':"  .'    .'--------""'   `.(_X_)'"'"'"`----""'`'--`-''".--.'
      \._.'-'""/    ______        / ^ \ _....--------...__`._'_."
       `.\_`."_..."",---. `""`'"": / \ :____    .""`"._   "-."
         `"",._...'"    '__..-''"`j   \'.   `"-;      ,`"""`.`.
          ,".'    :      \     .'.| " |\ `.   /       `      \ \
         '.'...--".       \  ,' / | - | .  "-/       ."`-.._  : .
        j":     _,'_       .'  /  | = | '   /       ,-\     `.:.|
        | .  _.'    ;      :  /   } = {  \ j       _\  `._    ' :
        | ',"     .'".      ./    `._,'   ':      :  \    "._: j
        '.':    ,"   ,".    .              \     ,-.  `._    '"|
         \ `  .'    /   :_  '               \   :   \    `._/ j
          . `'     /   /  \/                 ."".    \      : |
          ; :     /   /   /                  "   \    \     ; :
        ,'   \__.'___/__.'                    `.__\____\__.'   `.
      .'  .'".  _....-"                       mh "--...._  ,--.  `.
      `--'    `"                                         `"    `--" 


butterfly4
                                                                   _______
                                                                LLLLLLLLLLL
                                                            __LLLLLLLLLLLLLL
                                                           LLLLLLLLLLLLLLLLL
                                                         _LLLLLLLLLLLLLLLLLL
                                                        LLLLLLLLLLLLLLLLLLLL
                                                      _LLLLLLLLLLLLLLLLLLLLL
                                                      LLLLLLLLLLLLLLLLLLLLLL
                                              L     _LLLLLLLLLLLLLLLLLLLLLLL
                                             LL     LLLLLL~~~LLLLLLLLLLLLLL
                                            _L    _LLLLL      LLLLLLLLLLLLL
                                            L~    LLL~        LLLLLLLLLLLLL
                                           LL   _LLL        _LL   LLLLLLLL
                                          LL    LL~         ~~     ~LLLLLL
                                          L   _LLL_LLLL___         _LLLLLL
                                         LL  LLLLLLLLLLLLLL      LLLLLLLL
                                         L  LLLLLLLLLLLLLLL        LLLLLL
                                        LL LLLLLLLLLLLLLLLL        LLLLL~
                  LLLLLLLL_______       L _LLLLLLLLLLLLLLLL     LLLLLLLL
                         ~~~~~~~LLLLLLLLLLLLLLLLLLLLLLLLL~       LLLLLL
                       ______________LLL  LLLLLLLLLLLLLL ______LLLLLLLLL_
                   LLLLLLLLLLLLLLLLLLLL  LLLLLLLL~~LLLLLLL~~~~~~   ~LLLLLL
             ___LLLLLLLLLL __LLLLLLLLLLLLL LLLLLLLLLLLLL____       _LLLLLL_
          LLLLLLLLLLL~~   LLLLLLLLLLLLLLL   LLLLLLLLLLLLLLLLLL     ~~~LLLLL
      __LLLLLLLLLLL     _LLLLLLLLLLLLLLLLL_  LLLLLLLLLLLLLLLLLL_       LLLLL
     LLLLLLLLLLL~       LLLLLLLLLLLLLLLLLLL   ~L ~~LLLLLLLLLLLLL      LLLLLL
   _LLLLLLLLLLLL       LLLLLLLLLLLLLLLLLLLLL_  LL      LLLLLLLLL   LLLLLLLLL
  LLLLLLLLLLLLL        LLLLLLLLLLLLL~LLLLLL~L   LL       ~~~~~       ~LLLLLL
 LLLLLLLLLLLLLLL__L    LLLLLLLLLLLL_LLLLLLL LL_  LL_            _     LLLLLL
LLLLLLLLLLLLLLLLL~     ~LLLLLLLL~~LLLLLLLL   ~L  ~LLLL          ~L   LLLLLL~
LLLLLLLLLLLLLLLL               _LLLLLLLLLL    LL  LLLLLLL___     LLLLLLLLLL
LLLLLLLLLLLLLLLL              LL~LLLLLLLL~     LL  LLLLLLLLLLLL   LLLLLLL~
LLLLLLLLLLLLLLLL_  __L       _L  LLLLLLLL      LLL_ LLLLLLLLLLLLLLLLLLLLL
 LLLLLLLLLLLLLLLLLLLL        L~  LLLLLLLL      LLLLLLL~LLLLLLLLLLLLLLLL~
  LLLLLLLLLLLLLLLLLLLL___L_ LL   LLLLLLL       LLLL     LLLLLLLLLLLLLL
   ~~LLLLLLLLLLLLLLLLLLLLLLLL     LLLLL~      LLLLL        ~~~~~~~~~
           LLLLLLLLLLLLLLLLLL_ _   LLL       _LLLLL
               ~~~~~~LLLLLLLLLL~             LLLLLL
                         LLLLL              _LLLLLL
                         LLLLL    L     L   LLLLLLL
                          LLLLL__LL    _L__LLLLLLLL
                          LLLLLLLLLL  LLLLLLLLLLLL
                           LLLLLLLLLLLLLLLLLLLLLL
                            ~LLLLLLLLLLLLLLLLL~~
                               LLLLLLLLLLLLL
                                 ~~~~~~~~~ 


butterfly5
        899X7                                                X8997
     g999999Wm_                                         ,gm999999W.
   gW99*~~~~VM9Ws                                     ,m99*~~~~VM99m.
  g999`       '*99i                                  W9Af        Y99W.
  999[          '*9W_                             ,g9Af           999b
  999W            '*9W.                          g9Af            i9999
  9999W_            'V9W.       \.    ./       g9A~            ,g99999
  99999**Nm__          ~MW_.     N.  .N     _g9f`         ,_gm**M99999
  9999|   89999mms___    ~MWm.    [ ]`    gm9f`   ,___mmW9999|   8999P
  99999mmW99A***M9999999mms2M9s_,g+=Ye.,_W95_mmW9999999****999mmW9999[
  999999999`     '9999Af`  ~VM999P    9999*~`  ~*9999P      Y99999999[
  M9999AM99s.   ,g9999`       '99[    99P        Y999W_    _W99*99999!
  ]9999b'*999999999999b       _999.  d99b.      ,999999999999Af,99999
  'M9999i 'V*9999999999Wm__gmW9999[  99999mm__gm9999999999A*~  W9999f
    M9999s      ~~~~~~~~~~~~LmW99f   'M99ms7~~~~~~~~~~~`     ,W9999!
     V9999Ws_        ___mmW99999[      999999mms__.       ,_m9999A`
      '~*999999999999A**f~   ]9A[      A99   '~***999999999999Af~
          2999A*~~`          d9 9     ][]9.          ~~V*999K.
       ,gW9A~             ,_W9! 9[    9[ M9s_             'V99m_
      i999A            ,_W99f` i9[    9W  ~M99s_            !999W
      !9999ms_______mW99Af`   d99A.  /999.   ~*999ms_______mW999A
       Y9999f~~~~~~~~~`     gW9f~ +_z`'~M9m.     ~~~~~~~~~~M9999`
        V999            ,gm9Af`          ~*9Wm_            ]99A`
          ~*Nm______mmW99Af                 '*999mms_____gm*f`
             99999999                              99999999 


butterfly6
     .      .-~\
   / `-'\.'    `- :
   |    /          `._
   |   |   .-.        {
    \  |   `-'         `.
     \ |                /
~-.`. \|            .-~_
    .\-.\       .-~      \
     `-'/~~ -.~          /
   .-~/|`-._ /~~-.~ -- ~
  /  |  \    ~- . _\ 


butterfly7
                 .==-.                   .-==.
                 \()8`-._  `.   .'  _.-'8()/
                 (88"   ::.  \./  .::   "88)
                  \_.'`-::::.(#).::::-'`._/
                    `._... .q(_)p. ..._.'
                      ""-..-'|=|`-..-""
                      .""' .'|=|`. `"".
                    ,':8(o)./|=|\.(o)8:`.
                   (O :8 ::/ \_/ \:: 8: O)
                    \O `::/       \::' O/
                     ""--'         `--"" 


panda1
 
                              _,add8ba,
                            ,d888888888b,
                           d8888888888888b                        _,ad8ba,_
                          d888888888888888)                     ,d888888888b,
                          I8888888888888888 _________          ,8888888888888b
                __________`Y88888888888888P"""""""""""baaa,__ ,888888888888888,
            ,adP"""""""""""9888888888P""^                 ^""Y8888888888888888I
         ,a8"^           ,d888P"888P^                           ^"Y8888888888P'
       ,a8^            ,d8888'                                     ^Y8888888P'
      a88'           ,d8888P'                                        I88P"^
    ,d88'           d88888P'                                          "b,
   ,d88'           d888888'                                            `b,
  ,d88'           d888888I                                              `b,
  d88I           ,8888888'            ___                                `b,
 ,888'           d8888888          ,d88888b,              ____            `b,
 d888           ,8888888I         d88888888b,           ,d8888b,           `b
,8888           I8888888I        d8888888888I          ,88888888b           8,
I8888           88888888b       d88888888888'          8888888888b          8I
d8886           888888888       Y888888888P'           Y8888888888,        ,8b
88888b          I88888888b      `Y8888888^             `Y888888888I        d88,
Y88888b         `888888888b,      `""""^                `Y8888888P'       d888I
`888888b         88888888888b,                           `Y8888P^        d88888
 Y888888b       ,8888888888888ba,_          _______        `""^        ,d888888
 I8888888b,    ,888888888888888888ba,_     d88888888b               ,ad8888888I
 `888888888b,  I8888888888888888888888b,    ^"Y888P"^      ____.,ad88888888888I
  88888888888b,`888888888888888888888888b,     ""      ad888888888888888888888'
  8888888888888698888888888888888888888888b_,ad88ba,_,d88888888888888888888888
  88888888888888888888888888888888888888888b,`"""^ d8888888888888888888888888I
  8888888888888888888888888888888888888888888baaad888888888888888888888888888'
  Y8888888888888888888888888888888888888888888888888888888888888888888888888P
  I888888888888888888888888888888888888888888888P^  ^Y8888888888888888888888'
  `Y88888888888888888P88888888888888888888888888'     ^88888888888888888888I
   `Y8888888888888888 `8888888888888888888888888       8888888888888888888P'
    `Y888888888888888  `888888888888888888888888,     ,888888888888888888P'
     `Y88888888888888b  `88888888888888888888888I     I888888888888888888'
       "Y8888888888888b  `8888888888888888888888I     I88888888888888888'
         "Y88888888888P   `888888888888888888888b     d8888888888888888'
            ^""""""""^     `Y88888888888888888888,    888888888888888P'
                             "8888888888888888888b,   Y888888888888P^
                              `Y888888888888888888b   `Y8888888P"^
                                "Y8888888888888888P     `""""^
                                  `"YY88888888888P'
                                       ^""""""""'
 


panda2
                     ,mMm.,------.,mMm.
                    (GNP'        `?ND)
                     P  dMm.  ,mMb  ?
                     (  ?X_O  O_XP  )
                     (      qp      )   
                      \  `--'`--'  /

                   _____         ,__)
                  (--|__) _.._  _| _,
                    _|   (_|| |(_|(_|
                   (
 


panda3
             ,,,         ,,,
          ;"   ^;     ;'   ",
          ;    s$$$$$$$s     ;
          ,  ss$$$$$$$$$$s  ,'
          ;s$$$$$$$$$$$$$$$
          $$$$$$$$$$$$$$$$$$
         $$$$P""Y$$$Y""W$$$$$
         $$$$  p"$$$"q  $$$$$
         $$$$  .$$$$$.  $$$$
          $$DcaU$$$$$$$$$$
            "Y$$$"*"$$$Y"    
               "$b.$$"     
 


panda4
 $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$**$$$$$$$$$**$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$"   ^$$$$$$F    *$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$     z$$$$$$L    ^$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$    e$$$$$$$$$e  J$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$eee$$$$$$$$$$$$$e$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$b$$$$$$$$$$$$$$$$$$*$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$)$$$$P"e^$$$F$r*$$$$F"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$d$$$$  "z$$$$"  $$$$%  $3$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$*"""*$$$  .$$$$$$ z$$$*   ^$e*$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$"     *$$ee$$$$$$$$$$*"     $$$C$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$.      "***$$"*"$$""        $$$$e*$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$b          "$b.$$"          $$$$$b"$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$c.         """            $$$$$$$^$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$e..                     $$$$$$$$^$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$eeee..            J$$$$$$$$b"$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$r          z$$$$$$$$$$r$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"         z$$$$$**$$$$$^$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$*"          z$$$P"   ^*$$$ $$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$*"           .d$$$$       $$$ $$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$"           .e$$$$$F       3$$ $$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$.         .d$$$$$$$         $PJ$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$eeeeeeed$*""""**""         $\$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$                  $d$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$.                 $$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$e.              d$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$eeeeeee$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 


panda5
             __..                     ..__              
         .gd$$$$$b                 .$$$$$bp.           
        d$$$$$$$$$$               $$$$$$$$$$b          
       g$$$$$$$$$$$$     ___     $$$$$$$$$$$$p         
      !$$$$$$$$$$$$$.--''   ''--.$$$$$$$$$$$$$!        
      !$$$$$$$$$P^"               '-$$$$$$$$$$!        
       T$$$$$$P"                     '-$$$$$$P         
       !$$$$P"                          $$$$$!         
        T$$P                             $$$P          
         ^$        .             .        $^           
         :      .d$$             $$b.      :           
         :   .d$$$$$b           d$$$$$b.   :           
        :   g$$$$$$$$           $$$$$$$$p   :          
        :  d$$$$$$$$$b         d$$$$$$$$$b  :          
       :  !$$$$$$$$$$$         $$$$$$$$$$$!  :         
       :  $$$$$$$(O)$$b _..._ d$$(O)$$$$$$$  :         
       :  $$$$$$$$$$P^"       "^T$$$$$$$$$$  :         
        : T$$$$$$$P"     _._     "T$$$$$$$P :          
        : '$$$$$P       $$$$$       T$$$$$' :          
        :  "$$$P        "T$P"        T$$$"  :          
         :   T$           :           $P   :           
         :                :                :           
          :    "      _..' '.._      "    :            
           :   '.                   .'   :             
            '-.                       .-'              
               '-. '-._  __   _.-' .-'                 
                  '--.._ ___ _..--'                    
           ....eee$P"   """""    "T$aaa..._             
      _.ee$$$$$P""                  ""T$$$$$aa.
   .gd$$$$$$$P"                       "T$$$$$$bp.     



tiger1
                                  ___..........__
           _,...._           _."'_,.++8n.n8898n.`"._        _....._
         .'       `".     _.'_.'" _.98n.68n. `"88n. `'.   ,"       `.
        /        .   `. ,'. "  -'" __.68`""'""=._`+8.  `.'     .     `.
       .       `   .   `.   ,d86+889" 8"""+898n, j8 9 ,"    .          \
      :     '       .,   ,d"'"   _..d88b..__ `"868' .'  . '            :
      :     .      .    _    ,n8""88":8"888."8.  "               '     :
       \     , '  , . .88" ,8P'     ,d8. _   `"8n  `+.      `.   .     '
        `.  .. .     d89' "  _..n689+^'8n88n.._ `+  . `  .  , '      ,'
          `.  . , '  8'    .d88+"    j:""' `886n.    b`.  ' .' .   ."
           '       , .j            ,d'8.         `  ."8.`.   `.  ':
            .    .' n8    ,_      .f A 6.      ,..    `8b, '.   .'_
          .' _    ,88'   :8"8    6'.d`i.`b.   d8"8     688.  ".    `'
        ," .88  .d868  _         ,9:' `8.`8   "'  ` _  8+""      b   `,
      _.  d8P  d'  .d :88.     .8'`j   ;+. "     n888b 8  .     ,88.   .
     `   :68' ,8   88     `.   '   :   l `     .'   `" jb  .`   688b.   ',
    .'  .688  6P   98  =+""`.      `   '       ,-"`+"'+88b 'b.  8689  `   '
   ;  .'"888 .8;  ."+b. : `" ;               .: "' ; ,n  `8 q8, '88:       \
   .   . 898  8:  :    `.`--"8.              d8`--' '   .d'  ;8  898        '
  ,      689  9:  8._       ,68 .        .  :89    ..n88+'   89  689,' `     .
  :     ,88'  88  `+88n  -   . .           .        " _.     6:  `868     '   '
  , '  .68h.  68      `"    . . .        .  . .             ,8'   8P'      .   .
  .      '88  'q.    _.f       .          .  .    '  .._,. .8"   .889        ,
 .'     `898   _8hnd8p'  ,  . ..           . .    ._   `89,8P    j"'  _   `
  \  `   .88, `q9868' ,9      ..           . .  .   8n .8 d8'   +'   n8. ,  '
  ,'    ,+"88n  `"8 .8'     . ..           . .       `8688P"   9'  ,d868'   .  .
  .      . `86b.    " .       .            ..          68'      _.698689;      :
   . '     ,889_.n8. ,  ` .   .___      ___.     .n"  `86n8b._  `8988'b      .,6
    '       q8689'`68.   . `  `:. `.__,' .:'  ,   +   +88 `"688n  `q8 q8.     88
    , .   '  "     `+8 n    .   `:.    .;'   . '    . ,89           "  `q,    `8
   .   .   ,        .    + c  ,   `:.,:"        , "   d8'               d8.    :
    . '  8n           ` , .         ::    . ' "  .  .68h.             .8'`8`.  6
     ,    8b.__. ,  .n8688b., .    .;:._     .___nn898868n.         n868b "`   8
      `.  `6889868n8898886888688898"' "+89n88898868868889'         688898b    .8
       :    q68   `""+8688898P ` " ' . ` '  ' `+688988P"          d8+8P'  `. .d8
       ,     88b.       `+88.     `   ` '     .889"'           ,.88'        .,88
        :    '988b        "88b.._  ,_      . n8p'           .d8"'      '     689
        '.     "888n._,      `"8"+88888n.8,88:`8 .     _ .n88P'   .  `      ;88'
         :8.     "q888.  .            "+888P"  "+888n,8n8'"      .  .     ,d986
         :.`8:     `88986                          `q8"           ,      :688"
         ;.  '8,      "88b .d                        '                  ,889'
         :..   `6n      '8988                                         b.89p
         :. .    '8.      `88b                                        988'
         :. .      8b       `q8.        '                     . '   .d89      '
         . .        `8:       `86n,.       " . ,        , "        ,98P      ,
         .. .         '6n.       +86b.        .      .         _,.n88'     .
           .            `"8b.      'q98n.        ,     .  _..n868688'          .
          ' . .            `"98.     `8868.       .  _.n688868898p"            d
           . .                '88.      "688.       q89888688868"            ,86
         mh '. .                 88.     `8898        " .889"'              .988 


tiger2
    _
  ( \                ..-----..__
   \.'.        _.--'`  [   '  ' ```'-._
    `. `'-..-'' `    '  ' '   .  ;   ; `-'''-.,__/|/_
      `'-.;..-''`|'  `.  '.    ;     '  `    '   `'  `,
                 \ '   .    ' .     '   ;   .`   . ' 7 \
                  '.' . '- . \    .`   .`  .   .\     `Y
                    '-.' .   ].  '   ,    '    /'`""';:'
                      /Y   '.] '-._ /    ' _.-'
                      \'\_   ; (`'.'.'  ."/
                       ' )` /  `.'   .-'.'
                        '\  \).'  .-'--"
                          `. `,_'`
                            `.__)  
 


tiger3
                        ___......----:'"":--....(\
                .-':'"":   :  :  :   :  :  :.(1\.`-.
              .'`.  `.  :  :  :   :   : : : : : :  .';
             :-`. :   .  : :  `.  :   : :.   : :`.`. a;
             : ;-. `-.-._.  :  :   :  ::. .' `. `., =  ;
             :-:.` .-. _-.,  :  :  : ::,.'.-' ;-. ,'''"
           .'.' ;`. .-' `-.:  :  : : :;.-'.-.'   `-'
    :.   .'.'.-' .'`-.' -._;..:---'''"~;._.-;
    :`--'.'  : :'     ;`-.;            :.`.-'`.
     `'"`    : :      ;`.;             :=; `.-'`.
             : '.    :  ;              :-:   `._-`.
              `'"'    `. `.            `--'     `._;
                        `'"' 


tiger4
               (^\-==-/^)
              >\\ == //<
             :== q''p ==:      _,.---.._
              .__ qp __. ~.-'"'\   |   |''..
                 ^--^  | | \  \ |   , || /  '-. _______ .":
                  ;| | |    | |     |/   .^-./ _)_)__))_).'
                 / \ /      |       \ /  {/ \
             ..-'\_ \   \       ,.--'\ _ ) _/\
            |  ,_../ \- |'---"""      '-/ \  |
             --       | |            /_.   |-|
                  __' | |   ._ ___   \  )  | |__
          _,______'__ddd'_______._____""__ddd'___SK______
                  __________,______.   _._ 


tiger5
                          __,,,,_
          _ __..-;''`--/'/ /.',-`-.
      (`/' ` |  \ \ \\ / / / / .-'/`,_
     /'`\ \   |  \ | \| // // / -.,/_,'-,
    /<7' ;  \ \  | ; ||/ /| | \/    |`-/,/-.,_,/')
   /  _.-, `,-\,__|  _-| / \ \/|_/  |    '-/.;.\'
   `-`  f/ ;      / __/ \__ `/ |__/ |
        `-'      |  -| =|\_  \  |-' |
              __/   /_..-' `  ),'  //
             ((__.-'((___..-'' \__.' 


lion1
                  ,  ,, ,
           , ,; ; ;;  ; ;  ;
        , ; ';  ;  ;; .-''\ ; ;
     , ;  ;`  ; ,; . / /8b \ ; ;
     `; ; .;'         ;,\8 |  ;  ;
      ` ;/   / `_      ; ;;    ;  ; ;
         |/.'  /9)    ;  ; `    ;  ; ;
        ,/'          ; ; ;  ;   ; ; ; ;
       /_            ;    ;  `    ;  ;
      `?8P"  .      ;  ; ; ; ;     ;  ;;
      | ;  .:: `     ;; ; ;   `  ;  ;
      `' `--._      ;;  ;;  ; ;   ;   ;
       `-..__..--''   ; ;    ;;   ; ;   ;
                   ;    ; ; ;   ;     ;
 


lion2
 
    |\_                \|\||             
  -' | `.             -- ||||/
 /7      `-._        /7   |||||/
/            `-.____/    |||||||/`-.____________
\-'_                \-' |||||||||               `-._
 -- `-.              -/||||||||\                `` -`.
       |\              /||||||\             \_  |   `\\
       | \  \_______...-//|||\|________...---'\  \    \\
       |  \  \            ||  |  \ ``-.__--. | \  |    ``-.__--.
       |  |\  \          / |  |\  \   ``---'/ / | |       ``---'
     _/  / _|  )      __/_/  / _|  )     __/ / _| |
:   /,__/ /,__/      /,_/,__/_/,__/     /,__/ /,__/  


lion3
            ,aodObo,
        ,AMMMMP~~~~
     ,MMMMMMMMA.
   ,M;'     `YV'
  AM' ,OMA,
 AM|   `~VMM,.      .,ama,____,amma,..
 MML      )MMMD   .AMMMMMMMMMMMMMMMMMMD.
 VMMM    .AMMY'  ,AMMMMMMMMMMMMMMMMMMMMD
 `VMM, AMMMV'  ,AMMMMMMMMMMMMMMMMMMMMMMM,                ,
  VMMMmMMV'  ,AMY~~''  'MMMMMMMMMMMM' '~~             ,aMM
  `YMMMM'   AMM'        `VMMMMMMMMP'_              A,aMMMM
   AMMM'    VMMA. YVmmmMMMMMMMMMMML MmmmY          MMMMMMM
  ,AMMA   _,HMMMMmdMMMMMMMMMMMMMMMML`VMV'         ,MMMMMMM
  AMMMA _'MMMMMMMMMMMMMMMMMMMMMMMMMMA `'          MMMMMMMM
 ,AMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMa      ,,,   `MMMMMMM
 AMMMMMMMMM'~`YMMMMMMMMMMMMMMMMMMMMMMA    ,AMMV    MMMMMMM
 VMV MMMMMV   `YMMMMMMMMMMMMMMMMMMMMMY   `VMMY'  adMMMMMMM
 `V  MMMM'      `YMMMMMMMV.~~~~~~~~~,aado,`V''   MMMMMMMMM
    aMMMMmv       `YMMMMMMMm,    ,/AMMMMMA,      YMMMMMMMM
    VMMMMM,,v       YMMMMMMMMMo oMMMMMMMMM'    a, YMMMMMMM
    `YMMMMMY'       `YMMMMMMMY' `YMMMMMMMY     MMmMMMMMMMM
     AMMMMM  ,        ~~~~~,aooooa,~~~~~~      MMMMMMMMMMM
       YMMMb,d'         dMMMMMMMMMMMMMD,   a,, AMMMMMMMMMM
        YMMMMM, A       YMMMMMMMMMMMMMY   ,MMMMMMMMMMMMMMM
       AMMMMMMMMM        `~~~~'  `~~~~'   AMMMMMMMMMMMMMMM
       `VMMMMMM'  ,A,                  ,,AMMMMMMMMMMMMMMMM
     ,AMMMMMMMMMMMMMMA,       ,aAMMMMMMMMMMMMMMMMMMMMMMMMM
   ,AMMMMMMMMMMMMMMMMMMA,    AMMMMMMMMMMMMMMMMMMMMMMMMMMMM
 ,AMMMMMMMMMMMMMMMMMMMMMA   AMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
AMMMMMMMMMMMMMMMMMMMMMMMMAaAMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM 


lion4
                       ,.
                    ,_> `.   ,';
                ,-`'      `'   '`'._
             ,,-) ---._   |   .---''`-),.
           ,'      `.  \  ;  /   _,'     `,
        ,--' ____       \   '  ,'    ___  `-,
       _>   /--. `-.              .-'.--\   \__
      '-,  (    `.  `.,`~ \~'-. ,' ,'    )    _\
      _>    \     \ ,'  ') )   `. /     /    <,.
   ,-'   _,  \    ,'    ( /      `.    /        `-,
   `-.,-'     `.,'       `         `.,'  `\    ,-'
    ,'       _  /   ,,,      ,,,     \     `-. `-._
   /-,     ,'  ;   ' _ \    / _ `     ; `.     `(`-\
    /-,        ;    (o)      (o)      ;          `'`,
  ,~-'  ,-'    \     '        `      /     \      <_
  /-. ,'        \                   /       \     ,-'
    '`,     ,'   `-/             \-' `.      `-. <
     /_    /      /   (_     _)   \    \          `,
       `-._;  ,' |  .::.`-.-' :..  |       `-.    _\
         _/       \  `:: ,^. :.:' / `.        \,-'
       '`.   ,-'  /`-..-'-.-`-..-'\            `-.
         >_ /     ;  (\/( ' )\/)  ;     `-.    _<
         ,-'      `.  \`-^^^-'/  ,'        \ _<
          `-,  ,'   `. `"""""' ,'   `-.   <`'
            ')        `._.,,_.'        \ ,-'
             '._        '`'`'   \       <
                >   ,'       ,   `-.   <`'
                 `,/          \      ,-`
                  `,   ,' |   /     /
                   '; /   ;        (
                    _)|   `       (
                    `')         .-'
                      <_   \   /    
                        \   /\(
                         `;/  ` 


lion5
     .u:o. -c:o.  ex::u.    .czeez* .edB$ e@$$eu
  e$MMMMMNu^$MMMb.#BMMM$c $MMM8P.d$RM$F4RMMMMMMRb
A$MMMMMMMMRb^$MMMMb^$MMMP MMMMF4$MMM8"dRMMMMMMMMMN
zMM8M***M$8M$.#8MMM$.$8M&J$M$%$RMM8*.$R8$#"""""BMM
$$".e@Rmu. "*M"    '    ^^             .o$$RMM$c'$
$.$RMMMMMM$$$$ dRRRRRRRRRR$$MMMMMMRL'$$RMMMMMMMM$.
.$MMMMMMMMM$" $RMMMMMMMMMMMMMMMMMMMMb ^4$MMMMMMMM$
JMMMM$$**" ..$MMMMMMMMMMMMMMMMMMMMMMM$.:c  "***$MM
$M"..oenR$".$MMMMMMMMMMMMMMMMMMMMMMMMM$.*$$MMMRc.*
* d$MMMM$"u$MMMMMMMMMMMMMMMMMMMMMMMMM8MRc"$MMMMM$b
.$RMMM$# J$MF       "MMMMMMMMM   .....4M$b "$MMMM$
dMM8P"  dMMM$ $M8P4 4MMMMMMMMM 'L"$M$ JMMMF  "*88M
$$P\d$$ $MMMM$L..d$r4MMMMMMMMM <$$u.e$RMMMF $M$c"$
$ zRMM& ^8MMMMMMMMMF'MMMMMMMMM 4MMMMMMMMMG  $MMM$r
 $RMMMF$f)MMMMMMMMMF'MMMMMMMMM 4MMMMMMMMMF.$'$MMMM
'MMM$FJR$ $MMMMMMMMF4MMMMMMMMM 4MMMMMMMM$ $Rh^$MMM
AMM8\dRMMF RMMMMMMM 4MMMMMMMMM  MMMMMMM$".MMMRb$MM
AM$.$MMMMF.3MMMM$P*-'*********- "*NMMMM*..RMMMM$'$
AP.$RMMM$:$ $M$".oM$.'$RRRRR$".d$5u'*M$ $$?RMMMM$'
$ $MMMM$\$Rb'P eMMMMM$c"$M8# dRMMMMRc"F4MMb^$MMMMb
 $RMMMPzRMM!  eRMMMMMMR$c" dRMMMMMMMR  'MMMR.?$MM$
 $M8$ $MMMM"x $MMMMMMMMMM ?MMMMMMMMM$ 3'$MMM$b'$MM
ARM$.$RMMMP $$'BMMMMMMMMM 4MMMMMMMM8P4$$ $MMMM$.$M
A$F4RMMMMf $RM  *88MMM88M J8MM888$$\ @MMMr5MMMM$.$
 $ $RMM8P.$MMMF?b.                z$F$MMMMc3BMMM$'
  4MMMM$-$RMM8F4MM$ '8MMMMMMMM$ dRMM$#8MMM$r#8MMM.
  4MMM$.$MMMM$ RMMM$ 3MMMM$ 8MMM
   $MM$'MMMMP zRMMM$ .'**4P*".$ $MMMM$'$MMMM $MM$
   4MMC'MMMM$:$MMMMPoM$b   .@$M$$MMMMRL^$MMMF$M8
    "$$'MMM$\$MMMM$ MMMM$.4RMMM$r$MMMMRr*MMMN$$"
     'N'$MM$4$MMMMF$MMMMM$$RMMMM$4$MMMM$$MMM @
        #$MN4MMMMMF$MMMMM$#MMMMMM RMMMM$$M$F
         ?$$.$MMMMF$MMMMMF RMMMMM $MMMM\$MP
           *$'$MMMb3MMMMM  RMMMMNJRMMNFJ*
               #88$L#8MMMr RMMM$z$M8$"
                 ^*$P/*B8$$R8M"zP*" 


lion6
               _      _
             (c\-.--/a)
              |q: p   /\_            _____
            __\(_/  ).'  '---._.---'`     '---.__
           /  (Y_)_/             /        : \-._ \
   !!!!,,, \_))'-';             (       _/   \  '\\_
  !!II!!!!!IIII,, \_             \     /      \_  '.\
   !IIsndIIIII!!!!,,\     /_      \   |----.___ '-. \'.__
   !!!IIIIIIIIIIIIIIII\   | '--._.-'  _)       \  |  `'--'
       '''!!!!IIIIIII/   .',, ((___.-'         / /
             '''!!!!/  _/!!!!IIIIIII!!!!!,,,,,;,;,,,.....
                   | /IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
                   | \   ''IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
                   \_,)     '''''!!!!IIIIIIIIIIIIIIII!!!!!!!!
                                     ''''''''''!!!!!!!!!!!!!!! 


lion7
                                                 ,w.
                                              ,YWMMw  ,M  ,
                         _.---.._   __..---._.'MMMMMw,wMWmW,
                    _.-""        """           YP"WMMMMMMMMMb,
                 .-' __.'                   .'     MMMMW^WMMMM;
     _,        .'.-'"; `,       /`     .--""      :MMM[==MWMW^;
  ,mM^"     ,-'.'   /   ;      ;      /   ,       MMMMb_wMW"  @\
 ,MM:.    .'.-'   .'     ;     `\    ;     `,     MMMMMMMW `"=./`-,
 WMMm__,-'.'     /      _.\      F"""-+,,   ;_,_.dMMMMMMMM[,_ / `=_}
 "^MP__.-'    ,-' _.--""   `-,   ;       \  ; ;MMMMMMMMMMW^``; __|
            /   .'            ; ;         )  )`{  \ `"^W^`,   \  :
           /  .'             /  (       .'  /     Ww._     `.  `"
          /  Y,              `,  `-,=,_{   ;      MMMP`""-,  `-._.-,
         (--, )                `,_ / `) \/"")      ^"      `-, -;"\:
          `"""                    `"""   `"'                  `---"  


dragon1
                               __________________
                  __..---..-''_.............,_..`>
           _..-'':::_:-'_..-'_.-':::::::::,''//||                      _./
         ,':::::::,'_.-':','.-':.:.::::,','.//:||           _..---.._,','
       ,':::::::,',':'',',:':'`:.:::,',':`:/'.:::         ,'  ,'    _`/
      /::.::.::/,':'  ',':' . ' ::,',':'  '   `:\\       /     .,' _`:)
     /:.::.::://'   .          ',','         .   \\    ,/    .:;  (::. \
    :.::.::._//             .  /'   .     .       `:,./)    (:/ `. \`:)/
    |.:._.-'::     _..--.._                  __    (:.)      )    `'  `
    |.,'    ||  _.'     ,',`.  _.-''``.   ,''  )   /`'      :
    |/      ||,'    _.-','  |,'        ),'   ,:   (         ; __
            |/   _,':     / `         '      `:.            \',.\
              _,':'    : :.                     '    ,'     /'`''
            ,':'        \::  /:..        .        .:' (:   `.      _
          ,':'            \:::::.    .`.  )   _..:.:,::`.._  ``--'',`
         /:'      _..-''```::(:.      ::\/:::.::::.'_:::'  ``----''`'
        /:     ,-'          `\:.       `::_::-''
       ::'    ,               \:.        |::|
       |:    :          ,.     `:.       |::|
       ::.   :        ,'/        `.      ;::;
        \:.   `..__.-','           )  .:/:,'
         `.:.       ,'         _..' _.-::/
           ``-----''          `:. .'<:::<
                                `. `._>::`-..__
                                ,',`-._)_).---'`-._
                               ,`-`:::`'`\::'      \
                           ___/::::::::,' `:\      (_
                       __,'::::`--.._:/     \`._   (:::._
                     ,:`._`----..._:::`-._   \:::.  `-.SSt:. 


dragon2
 
                    ___'''''''''''\___
                 __'                  \___
               -/                         \_
             -/                             \_    
           -/                                 \   
          /                                    \
           '''''''''''_                         \
                     _-'_           __           \
                   _*    '_        (  '_         \ _
                 _*        '        \   '_        \ *_
               _*                         '_       \  *_
         /   _*         -----           ----'-      \  *_
        /  _*          -     \        /       ' \   \   *_
       / _*                   \    ---\           \  \    *_
      / *                 --   \---    \     \_--_ \       *_
     -        ----''''''''   \  \       \_   \_   -_  \      -
    - @     -'               \  \         \   /     -_        _
    /- _  )'                 __  \     ___/  /        -_       -
   |  /  /                  \  ___\  _ \\ __/           -
   /  | /                    \               \           -      '
  [o / /                                       \          -     _
   \/_/                        |                 -         -    -
                               |                   \       -    -
                               |                     \___ -    -
                               |                          \_______
 


dragon3
 
                               ,/     _,---._
                    ,       _,'/|  ,-'       `.
                     \.__,-' // `./   ____     \
                      \\    //   `. ,'\__/`.    \
                       \\  //      `.,'  `./`.   `.
                        ||//         `-.   `.'|    \
                        / ,`,===========:=- |-|     \
            __        ,' )\,_        ,-'    | |      `.__
          /))/)       \,/)/ \\\    /'      /`-|          `---.___
         ())'_)       / '   /,\\ ,/       |`-,'
         /)).\____,-_/  , ,'~  \\|        |--|          ,
        (()||_)~~~~|' ,','      )'        `._,\  `.     `.
         ((\\/      \/_/       (          / `.-\   \      )
           /\\                  `,       /    \-`-.,'   ,/
          / ')\                        ,'     /`-./   ,'---.____
         |     |                      /   ,--'   /   /---.______
         |  |  |            ,-.-. _,-'  ,-,-._  /  _/
         |_/|_,'           /\/ ) `  /|,/\/\_, `-  /\
          // ||_          //'|/\__,'\|(/'|/ \___,'`,)
          `-  ~~          `  `           `
 


dragon4
          _(.==.         .==.)_
          //`^\\(\_._/)//^`\\
         //^ ^ ^( 6 6 )^ ^ ^\\
        //^ ^ ^/\( " )/\^ ^ ^\\
       // ^ /\/_/ v"v \_\/\^  \\
       \\^ /  // /===\ \\  \ ^//
        \\/   \(((===)))/   \//
         ^   .-' /\__/\ `-.  ^
            (((-'      '-)))
 


dragon5
            ____ __
          { --.\  |          .)%%%)%%
           '-._\\ | (\___   %)%%(%%(%%%
               `\\|{/ ^ _)-%(%%%%)%%;%%%
           .'^^^^^^^  /`    %%)%%%%)%%%'
          //\   ) ,  /       '%%%%(%%'
    ,  _.'/  `\<-- \<
     `^^^`     ^^   ^^
 


dragon6
             _.===._      ,"^^^^",
           /_\^^^/_\    /  ^ ,^  \     ,
           (0\ ^ /0)\  / ^  /  ^  \    /\
            \     /  ^^   ^ \ ^ \  ",." /
             )   (  ^  ^   ^ \   \    ,'
             (o_o)^    \ ^   ,)  /`^^`
              ^V^\ ^ \  \_,-"((((
              /  /`""/  /
             (((`   '(((
 


dragon7
                      ,     _,
                    #\`-"-'/
                   #/   o (o
                  #/ \__   '._
  ,_#_#          #/  /=/`-. _")
   '-.`\#       #/  /=(_.. `-`.
      \ `\#    #/  -.'`_\\\`_\\\
       ;  \#  #/ '.__.'=\_.'
       |   '-#;    _|====\_
       ;      '  /`  `\==| \
        \     .        \=| /
         '-.._         // /__
              `)-.    `----._\
                <_________\_\_\
 


dragon8
                                         ,   ,
                                        $,  $,     ,
                                        "ss.$ss. .s'
                                ,     .ss$$$$$$$$$$s,
                                $. s$$$$$$$$$$$$$$`$$Ss
                                "$$$$$$$$$$$$$$$$$$o$$$       ,
                               s$$$$$$$$$$$$$$$$$$$$$$$$s,  ,s
                              s$$$$$$$$$"$$$$$$""""$$$$$$"$$$$$,
                              s$$$$$$$$$$s""$$$$ssssss"$$$$$$$$"
                             s$$$$$$$$$$'         `"""ss"$"$s""
                             s$$$$$$$$$$,              `"""""$  .s$$s
                             s$$$$$$$$$$$$s,...               `s$$'  `
                         `ssss$$$$$$$$$$$$$$$$$$$$####s.     .$$"$.   , s-
                           `""""$$$$$$$$$$$$$$$$$$$$#####$$$$$$"     $.$'
                                 "$$$$$$$$$$$$$$$$$$$$$####s""     .$$$|
                                  "$$$$$$$$$$$$$$$$$$$$$$$$##s    .$$" $
                                   $$""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"   `
                                  $$"  "$"$$$$$$$$$$$$$$$$$$$$S""""'
                             ,   ,"     '  $$$$$$$$$$$$$$$$####s
                             $.          .s$$$$$$$$$$$$$$$$$####"
                 ,           "$s.   ..ssS$$$$$$$$$$$$$$$$$$$####"
                 $           .$$$S$$$$$$$$$$$$$$$$$$$$$$$$#####"
                 Ss     ..sS$$$$$$$$$$$$$$$$$$$$$$$$$$$######""
                  "$$sS$$$$$$$$$$$$$$$$$$$$$$$$$$$########"
           ,      s$$$$$$$$$$$$$$$$$$$$$$$$#########""'
           $    s$$$$$$$$$$$$$$$$$$$$$#######""'      s'         ,
           $$..$$$$$$$$$$$$$$$$$$######"'       ....,$$....    ,$
            "$$$$$$$$$$$$$$$######"' ,     .sS$$$$$$$$$$$$$$$$s$$
              $$$$$$$$$$$$#####"     $, .s$$$$$$$$$$$$$$$$$$$$$$$$s.
   )          $$$$$$$$$$$#####'      `$$$$$$$$$###########$$$$$$$$$$$.
  ((          $$$$$$$$$$$#####       $$$$$$$$###"       "####$$$$$$$$$$
  ) \         $$$$$$$$$$$$####.     $$$$$$###"             "###$$$$$$$$$   s'
 (   )        $$$$$$$$$$$$$####.   $$$$$###"                ####$$$$$$$$s$$'
 )  ( (       $$"$$$$$$$$$$$#####.$$$$$###'                .###$$$$$$$$$$"
 (  )  )   _,$"   $$$$$$$$$$$$######.$$##'                .###$$$$$$$$$$
 ) (  ( \.         "$$$$$$$$$$$$$#######,,,.          ..####$$$$$$$$$$$"
(   )$ )  )        ,$$$$$$$$$$$$$$$$$$####################$$$$$$$$$$$"
(   ($$  ( \     _sS"  `"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$S$$,
 )  )$$$s ) )  .      .   `$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"'  `$$
  (   $$$Ss/  .$,    .$,,s$$$$$$##S$$$$$$$$$$$$$$$$$$$$$$$$S""        '
    \)_$$$$$$$$$$$$$$$$$$$$$$$##"  $$        `$$.        `$$.
        `"S$$$$$$$$$$$$$$$$$#"      $          `$          `$
            `"""""""""""""'         '           '           '
 


dragon10
                                  _
                              ==(W{==========-      /===-
                                ||  (.--.)         /===-_---~~~~~~~----__
                                | \_,|**|,__      |===-~___            _,-'`
                   -==\\        `\ ' `--'   ),    `//~\\   ~~~~`--._.-~
               ______-==|        /`\_. .__/\ \    | |  \\          _-~`
         __--~~~  ,-/-==\\      (   | .  |~~~~|   | |   `\       ,'
      _-~       /'    |  \\     )__/==0==-\<>/   / /      \     /
    .'        /       |   \\      /~\___/~~\/  /' /        \   /
   /  ____  /         |    \`\.__/-~~   \  |_/'  /          \/'
  /-'~    ~~~~~---__  |     ~-/~         ( )   /'        _--~`
                    \_|      /        _) | ;  ),   __--~~
                      '~~--_/      _-~/- |/ \   '-~ \
                     {\__--_/}    / \\_>-|)<__\      \
                     /'   (_/  _-~  | |__>--<__|      |
                    |   _/) )-~     | |__>--<__|      |
                    / /~ ,_/       / /__>---<__/      |
                   o-o _//        /-~_>---<__-~      /
                   (^(~          /~_>---<__-      _-~
                  ,/|           /__>--<__/     _-~
               ,//('(          |__>--<__|     /                  .--_
              ( ( '))          |__>--<__|    |                 /' _-_~\
           `-)) )) (           |__>--<__|    |               /'  /   ~\`\
          ,/,'//( (             \__>--<__\    \            /'  //      ||
        ,( ( ((, ))              ~-__>--<_~-_  ~--__---~'/'/  /'       VV
      `~/  )` ) ,/|                 ~-_~>--<_/-__      __-~ _/
    ._-~//( )/ )) `                    ~~-'_/_/ /~~~~~__--~
     ;'( ')/ ,)(                              ~~~~~~~~
    ' ') '( (/
 


dragon11
 
                                               _   __,----'~~~~~~~~~`-----.__
                                        .  .    `//====-              ____,-'~`
                        -.            \_|// .   /||\\  `~~~~`---.___./
                  ______-==.       _-~o  `\/    |||  \\           _,'`
            __,--'   ,=='||\=_    ;_,_,/ _-'|-   |`\   \\        ,'
         _-'      ,='    | \\`.    '',/~7  /-   /  ||   `\.     /
       .'       ,'       |  \\  \_  "  /  /-   /   ||      \   /
      / _____  /         |     \\.`-_/  /|- _/   ,||       \ /
     ,-'     `-|--'~~`--_ \     `==-/  `| \'--===-'       _/`
               '         `-|      /|    )-'\~'      _,--"'
                           '-~^\_/ |    |   `\_   ,^             /\
                                /  \     \__   \/~               `\__
                            _,-' _/'\ ,-'~____-'`-/                 ``===\
                           ((->/'    \|||' `.     `\.  ,                _||
             ./                       \_     `\      `~---|__i__i__\--~'_/
            <_n_                     __-^-_    `)  \-.______________,-~'
             `B'\)                  ///,-'~`__--^-  |-------~~~~^'
             /^>                           ///,--~`-\
            `  `                                       
 


dragon12
 WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWP'dP'dWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWW"VWWWb """'.o.. .dWWWWWWWWWWWWP~~""_{WWWWWWWWWWWWWWWWWWWWWW
WWWWWWb  """""""w.     jWWWWWWWP"  ,.--"'    .wWWWWWWWWWWWWWWWWWW
WWWWWWWbWWWWF"""""`    WWWWWWP" .-"          {WWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWLLWP      jWWWWP"               .wwWWWWWWWWW WWWWWWWW
WWWWW`W`W`WWWW'      jWWW'                 {WWWWWWWWWWP  `VWWWWWW
WWWWWW, dWWWW'      jWWWW                 .wwWWP".w."WWP.WWWWWWWW
WWWWWW' VWWWW        VWW'               _{WWWW( WWWW. P.WWWWWWWWW
::::::':  :::         "                {  `:::::. '' ,.::::::::::
:::::,:::  ::                                `''''  .::::::::::::
::::::::::                                       ..,:::::::::::::
:::::::::::   .                  ..:.      `:::::::::::::::::::::
:::::::::::: ::   .: ::::::::   :::::::.          `::::::::::::::
::::::::::::::' .::::::::::::.    .::::::::::::::  ::::::::::::::
:::::::::::::'.:::::::::::::::::  ::::::::::::::'  ::::::::::::::
:::::::'.....:.. ::::::::'......:. :::::::::'....::.`::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
 


dragon13
               __                  __
             ( _)                ( _)
            / / \\              / /\_\_
           / /   \\            / / | \ \
          / /     \\          / /  |\ \ \
         /  /   ,  \ ,       / /   /|  \ \
        /  /    |\_ /|      / /   / \   \_\
       /  /  |\/ _ '_|\    / /   /   \    \\
      |  /   |/  0 \0\ \  / |    |    \    \\
      |    |\|      \_\_ /  /    |     \    \\
      |  | |/    \.\ o\o)  /      \     |    \\
      \    |     /\\`v-v  /        |    |     \\
       | \/    /_| \\_|  /         |    | \    \\
       | |    /__/_     /   _____  |    |  \    \\
       \|    [__]  \_/  |_________  \   |   \    ()
        /    [___] (    \         \  |\ |   |   //
       |    [___]                  |\| \|   /  |/
      /|    [____]                  \  |/\ / / ||
     (  \   [____ /     ) _\      \  \    \| | ||
      \  \  [_____|    / /     __/    \   / / //
      |   \ [_____/   / /        \    |   \/ //
      |   /  '----|   /=\____   _/    |   / //
   __ /  /        |  /   ___/  _/\    \  | ||
  (/-(/-\)       /   \  (/\/\)/  |    /  | /
                (/\/\)           /   /   //
                       _________/   /    /
                      \____________/    (
 


dragon14
                                                    _
                       /                            )
                      (                             |\
                     /|                              \\
                    //                                \\
                   ///                                 \|
                  /( \                                  )\
                  \\  \_                               //)
                   \\  :\__                           ///
                    \\     )                         // \
                     \\:  /                         // |/
                      \\ / \                       //  \
                       /)   \     ___..-'         ((  \_|
                      //     /  .'  _.'           \ \  \
                     /|       \(  _\_____          \ | /
                    (| _ _  __/          '-.       ) /.'
                     \\ .  '-.__ \          \_    / / \
                      \\_'.     > '-._   '.   \  / / /
                       \ \      \     \    \   .' /.'
                        \ \  '._ /     \  /   / .' |
                         \ \_     \_   |    .'_/ __/
                          \  \      \_ |   / /  _/ \_
                           \  \       / _.' /  /     \
                           \   |     /.'   / .'       '-,_
                            \   \  .'   _.'_/             \
               /\    /\      ) ___(    /_.'           \    |
              | _\__// \    (.'      _/               |    |
              \/_  __  /--'`    ,                   __/    /
              (_ ) /b)  \  '.   :            \___.-:_/ \__/
              /:/:  ,     ) :        (      /_.'_/-' |_ _ /
             /:/: __/\ >  __,_.----.__\    /        (/(/(/
            (_(,_/V .'/--'    _/  __/ |   /
             VvvV  //`    _.-' _.'     \   \
               n_n//     (((/->/        |   /
               '--'         ~='          \  |
                                          | |_,,,
                                          \  \  /
                                           '.__)
 


dragon15
                          __
                     _.-'.-'-.__
                  .-'.       '-.'-._ __.--._
           -..'\,-,/..-  _         .'   \   '----._
            ). /_ _\' ( ' '.         '-  '/'-----._'-.__
            '..'     '-r   _      .-.       '-._ \
            '.\. Y .).'       ( .'  .      .\          '\'.
            .-')'|'/'-.        \)    )      '',_      _.c_.\
              .<, ,>.          |   _/\        . ',   :   : \\
             .' \_/ '.        /  .'   |          '.     .'  \)
                             / .-'    '-.        : \   _;   ||
                            / /    _     \_      '.'\ ' /   ||
                           /.'   .'        \_      .|   \   \|
                          / /   /      __.---'      '._  ;  ||
                         /.'  _:-.____< ,_           '.\ \  ||
                        // .-'     '-.__  '-'-\_      '.\/_ \|
                       ( };====.===-==='        '.    .  \\: \
                        \\ '._        /          :   ,'   )\_ \
                         \\   '------/            \ .    /   )/
                          \|        _|             )Y    |   /
                           \\      \             .','   /  ,/
                            \\    _/            /     _/
                             \\   \           .'    .'
                              '| '1          /    .'
                                '. \        |:    /
                                  \ |       /', .'
                                   \(      ( ;z'
                                    \:      \ '(_
                                     \_,     '._ '-.___
                                                 '-' -.\

 


dragon16
             <>=======()
           (/\___   /|\\          ()==========<>_
                 \_/ | \\        //|\   ______/ \)
                   \_|  \\      // | \_/
                     \|\/|\_   //  /\/
                      (oo)\ \_//  /
                     //_/\_\/ /  |
                    @@/  |=\  \  |
                         \_=\_ \ |
                           \==\ \|\_ 
                        __(\===\(  )\
                       (((~) __(_/   |
                            (((~) \  /
                            ______/ /
                            '------'
 


dragon17
              /"\
            (/'\'-._        /"\
             `  \'-._`-.__.'~'\)                              ____
                 ) \  `-.   | '                              / (__\
              _,'   `.   `. |                               / .'  \)
          _.-'        \    | :                             / /`-...--.
       .-'             `.   ||                           .'.'   _.-""))
     .'__...__           \   ::                        _/.'   .' /   '
    /,--.     ``'--._     \   ||                   _.-" /   .'  :
   `\\_) )           `'._  \  | \                 (    (_ .'    :
     `" /                `-.`/'  '-./"\         __,      "(""\   \_
      .'         _ _ _ _ _  \`    ./`'\)  ,    _\/(       /"")) .--"--.
     /    __.- '           '''\ .'      /(\   _\/ |    )     '    .-""))
    /_.- '                     .`.     '%@\`._\/  |  //|         '    '
   /,--\                       | |    :%%@@\ |'    \//@|   `.   :
  (__,' |                       \ \   :%%@@) ' _    `|%/     :   ;
         ;                       | \.  ';/'__    \ : \\       ;  ;
         :                      .'  )  .'/###|    V  |#\   .-''-.\
          ;                    /   /   ||#####\   | /###| '    ._/
          :                  .'   /    ||######|  | |###|
          :                .'    |   .-\`.#####|  ( |###'
           :             .'  __  |  .-\|`\`.###; , \\#'
  _.-.      :          .' _-"  `. \.-\/ ) `-._")/ \|\ \_
<" .._)      :       .'_-'       \ \.' (            \   )
 ".__```-.    :    .'.'           \ `-  `-._   .     \ (
        `.`.  :  .'/ _..--.._      )        `-_|AA-.._\.
          : : : //.-'       _`)              / \\A(   ))
           : ///    /""-._-'                |  /`.\\, '
           ,// -_.-'      """--._        -__|_|             
          //~\_ (    _           `.    -._  /_|
         (/    ""\  ( "_          /  `._  "/".'
          `       \  \                  ""/"/\  _.-.
                  _\  \_/"\            _.'.\  \/ /`\)
                /"_"--"  (\)"\      _-"_.'  )   '-"""\
                \\ "-, ___.-"))___-'-""   /"_..__ <""\)
                 `  (/"      '            `      "\)
                     `                            '
 


dragon18
         _ _
      _(9(9)__        __/^\/^\__
     /o o   \/_     __\_\_/\_/_/_
     \___,   \/_   _\.'       './_      _/\_
      `---`\  \/_ _\/           \/_   _|.'_/
            \  \/_\/      /      \/_  |/ /
             \  `-'      |        ';_:' /
             /|          \      \     .'
            /_/   |,___.-`',    /`'---`
             /___/`       /____/
 


dragon19
               _,-'/-'/
  .      __,-; ,'( '/
   \.    `-.__`-._`:_,-._       _ , . ``
    `:-._,------' ` _,`--` -: `_ , ` ,' :
       `---..__,,--'            ` -'. -'
 


dragon20
                         \`-\`-._
                         \` )`. `-.__      ,
      '' , . _       _,-._;'_,-`__,-'    ,/
     : `. ` , _' :- '--'._ ' `------._,-;'
      `- ,`- '            `--..__,,---'   
 


dragon21
                               ___, ____--'
                         _,-.'_,-'      (
                      ,-' _.-''....____(
            ,))_     /  ,'\ `'-.     (          /\
    __ ,+..a`  \(_   ) /   \    `'-..(         /  \
    )`-;...,_   \(_ ) /     \  ('''    ;'^^`\ <./\.>
        ,_   )   |( )/   ,./^``_..._  < /^^\ \_.))
       `=;; (    (/_')-- -'^^`      ^^-.`_.-` >-'
       `=\\ (                             _,./
         ,\`(                         )^^^
           ``;         __-'^^\       /
             / _>emj^^^   `\..`-.    ``'.
            / /               / /``'`; /
           / /          ,-=='-`=-'  / /
     ,-=='-`=-.               ,-=='-`=-.
   *******************************************
 


dragon22
                                                        ____________
                                 (`-..________....---''  ____..._.-`
                                  \\`._______.._,.---'''     ,'
                                  ; )`.      __..-'`-.      /
                                 / /     _.-' _,.;;._ `-._,'
                                / /   ,-' _.-'  //   ``--._``._
                              ,','_.-' ,-' _.- (( =-    -. `-._`-._____
                            ,;.''__..-'   _..--.\\.--'````--.._``-.`-._`.
             _          |\,' .-''        ```-'`---'`-...__,._  ``-.`-.`-.`.
  _     _.-,'(__)\__)\-'' `     ___  .          `     \      `--._
,',)---' /|)          `     `      ``-.   `     /     /     `     `-.
\_____--.  '`  `               __..-.  \     . (   < _...-----..._   `.
 \_,--..__. \\ .-`.\----'';``,..-.__ \  \      ,`_. `.,-'`--'`---''`.  )
           `.\`.\  `_.-..' ,'   _,-..'  /..,-''(, ,' ; ( _______`___..'__
                   ((,(,__(    ((,(,__,'  ``'-- `'`.(\  `.,..______   
                                                      ``--------..._``--.__
 


dragon23
 
                ,'\   |\
               / /.:  ;;
              / :'|| //
             (| | ||;'
             / ||,;'-.._
            : ,;,`';:.--`
            |:|'`-(\\
            ::: \-'\`'
             \\\ \,-`.
              `'\ `.,-`-._      ,-._
       ,-.       \  `.,-' `-.  / ,..`.
      / ,.`.      `.  \ _.-' \',: ``\ \
     / / :..`-'''``-)  `.   _.:''  ''\ \
    : :  '' `-..''`/    |-''  |''  '' \ \
    | |  ''   ''  :     |__..-;''  ''  : :
    | |  ''   ''  |     ;    / ''  ''  | |
    | |  ''   ''  ;    /--../_ ''_ '' _| |
    | |  ''  _;:_/    :._  /-.'',-.'',-. |
    : :  '',;'`;/     |_ ,(   `'   `'   \|
     \ \  \(   /\     :,'  \
      \ \.'/  : /    ,)    /
       \ ':   ':    / \   :
        `.\    :   :\  \  |
                \  | `. \ |..-_
                 ) |.  `/___-.-`
               ,'  -.'.  `. `'        _,)
               \'\(`.\ `._ `-..___..-','
                  `'      ``-..___..-'
 


dragon24
  ,,
`""*$b..
     ""*$o.
         "$$o.
           "*$$o.
              "$$$o.
                "$$$$bo...       ..o:
                  "$$$$$$$$booocS$$$    ..    ,.
               ".    "*$$$$SP     V$o..o$$. .$$$b
                "$$o. .$$$$$o. ...A$$$$$$$$$$$$$$b
          ""bo.   "*$$$$$$$$$$$$$$$$$$$$P*$$$$$$$$:
             "$$.    V$$$$$$$$$P"**""*"'   VP  * "l
               "$$$o.4$$$$$$$$X
                "*$$$$$$$$$$$$$AoA$o..oooooo..           .b
                       .X$$$$$$$$$$$P""     ""*oo,,     ,$P
                      $$P""V$$$$$$$:    .        ""*****"
                    .*"    A$$$$$$$$o.4;      .
                         .oP""   "$$$$$$b.  .$;
                                  A$$$$$$$$$$P
                                  "  "$$$$$P"
                                      $$P*"
                                     .$"
                                     "
 


dragon25
                                 ,- 
                               //        
                              /:      ,
                             ;.(     //
                   |   ,     /`|    //
                   |\  |\    |,|   //
                |  (\  (\    |`|   |(
                (\  \\  \\   |,|   ;|
            .   ||   \\  \\  |`(   ;( 
            \\   \\  \\  \\  |.\\  ((                              
             \\   \\  \\  \\  \\ \;/:\                 
               \\  \\  \'. \\_,\\ /\""-._                
                \\  \\  \ \-"   \/ `;._ ".
               ___\\-\\-" \ \_  /,  |_ "._\
         _,--""___ \ \,_   "-_"- |".|(._ ".".-.
     _,-"_,--"""__ ) "."-_    "--\ \"("o\_\ "- ".
   ,",-""" _.-'''_-"   "-_"-.__   \ \_\_//\)__"\_)
 ,"    ',-'  ,-""   7"  _ "-.._""_>\__`""'"__ ""``-._
        ;  ," ,-",'/` ,":\.    `   `  `"""___`""-._  ".   )
        ;,"_," ,' /`,"}}::\\         `... \____''' "\  '.|\
       ,","   :  /`/{{)/:::"\__,---._    \  \_____'''\    \
      , ,"_  ;  /`/ ///::::::::' ,-"-\    \__   \____''\ \ \
     ,,"   `;| ";; /}}/::'``':::(._``."-.__  """--    '_\ \ \
    ('       ;// / {;;:'`````':; /`._."""  ""-.._ `"-. " (   )
    /         )(/ <";"'``   ``/ /_.(             "_  "-_"\`);
              (/ <";"``     `/ /`,(                "._ _".\; 
               |<";"`   ``  / /"-"                    "  
               <";"` ``    / /__,;   
 

parrot1
                                                       ,--,
                                              __,--'~~__  `-,
                                         ___,'   _,--'0 )  /
                      _____________,----'{__    `-.   _/ /~(
  ____,--------------' { {     ,----        )     '-,   )   \
 {_----__,-- `--------{ {~~~~___________,---(__     `. (\    )
  ~~~`---------.__,__{_{___-/~~~~~~~~~~~       \      (  `. /
          ___,-{~~~~~{_ ~~~{_                  ;`.    /`-';/
         {____  `---   ;     `----.___         ; ,`--'    `
  _____,-'--`.______,  `-._           `-------' /
 { -----------  `--.____,  `-.___      _,-'----'
  `----------._---____         __`-,--'_/           (\
              ~~;~~~~~`-------'~~~~_,-\ \ _________/  |
               / / ;  / /______,--'  /   ~~~\       " /
              ; ; /  ; ;        \ \_( (~~~~| |__"____/
             | / /  / /        / __~~~~\ ,'\/ ~~~~~~~
             ;~ ;`'/ /        ( (~~~~~: :
            |: ;  ; ;          \/"    \/
            ;`'  / /           /  "  "|
           |    / /          _/ "  "  /
           |   ;;'          /    "  _/
           |  ;|           /  "  " /
           | ; |         _/  "  "  /
           |;  |        /   "  "  /
           :   |       /  "   "   ~/
           `---'      / "   "  "" / 


parrot2
                             .
                           | \/|
   (\   _                  ) )|/|
       (/            _----. /.'.'
 .-._________..      .' @ _\  .'
 '.._______.   '.   /    (_| .')
   '._____.  /   '-/      | _.'
    '.______ (         ) ) \
      '..____ '._       )  )
         .' __.--\  , ,  // ((
         '.'     |  \/   (_.'(
                 '   \ .'
                  \   (
                   \   '.
                    \ \ '.)
                     '-'-' 


parrot3
 ______________________________________________________
__________|___________,_______________________________
__________|__________//,______________________________
__________|__________\|/;..___________________________
__________|___________\\//\,._________________________
__________|___________/   '\/_________________________
__________|__________/,* _  |_________________________
__________|_________( ) ( ) (_________________________
__________|__________\(  "   \________________________
__________|____________)      \\______________________
__________|___________(         \\\___________________
__________|____________\  (  \\   \\\_________________
__________|____________(\  \\  \\   \\\_______________
__________|_____________\\   \\  \\   \\\_____________
__________|______________\\   \\   \\   \\____________
__________|_______________\\    \\   \\  \\___________
__________|________________\-\    \\\  \\\\___________
__________|_________________\ /\_    \\\ \\___________
__________|__________________(( \-___-   \\\__________
__________|___________________\  \_______ \\\_________
__________|____________________\  \_______ \\\________
__________|_____________________\  \________\\\_______
__________|______________________\  \________\\\______
__________|_______________________\  \________\\______
__________|________________________(--)_______________
__________|___________________________________________
__________|___________________________________________ 

```
