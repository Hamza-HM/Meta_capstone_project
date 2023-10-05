# Meta-backend!
NOTE:
YOU HAVE TO BE AUTHENTICATED WITH TOKEN
ALSO USING PIPENV CUZ VENV TAKES A LOT OF TIME TO UPLOAD AND DOWNLOAD

if you have no menu items on your mysql database please create a superuser 
and connect to the django admin panel and create some bookings and menu items


static html is in 

http://127.0.0.1:8000/hello

**********************************************************************************
auth urls to test from djoser:

use GET method

DISPLAY USERS: http://127.0.0.1:8000/auth/users/

----------------------------------------------------------

use POST method

REGISTER : http://127.0.0.1:8000/auth/users/ 

-------------------------------------------------------

use POST method
CREATEA TOKEN: http://127.0.0.1:8000/auth/token/login/

**********************************************************************************
models to test in api:

use GET method
DISPLAY MENU ITEMS : http://127.0.0.1:8000/api/menu-items/

-------------------------------------------------------

use POST method
CREATE A MENU ITEM : http://127.0.0.1:8000/api/menu-items/

-------------------------------------------------------

use GET method
DISPLAY A SINGLE MENU ITEM : http://127.0.0.1:8000/api/menu-items/2

-------------------------------------------------------

use PUT method
UPDATE A SINGLE MENU ITEM : http://127.0.0.1:8000/api/menu-items/2

-------------------------------------------------------

use DELETE method
DELETE A SINGLE MENU ITEM : http://127.0.0.1:8000/api/menu-items/2

-------------------------------------------------------

use GET method
DISPLAY BOOKING LIST : http://127.0.0.1:8000/api/booking/tables

-------------------------------------------------------

use POST method
DISPLAY BOOKING LIST : http://127.0.0.1:8000/api/booking/tables





