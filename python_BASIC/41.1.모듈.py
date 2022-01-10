import Theater_Module
Theater_Module.price(3)
Theater_Module.price_soldier(3)

#그런데 이름이 너무 길어 호출이 불편하다면?

import Theater_Module as mv

mv.price_soldier(3)
mv.price_morning(4)
mv.price(5)

#이것마저 귀찮다? ★
from Theater_Module import *

price(5)
price_morning(5)

#일부만 가져오겠다?
from Theater_Module import price, price_morning