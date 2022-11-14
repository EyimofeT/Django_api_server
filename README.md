# SpeedPay-BE-Test
A mini-prototype mock api with limited functionalities which facilitates user wallet creations, 

## API DOCUMENTATION LINK
https://documenter.getpostman.com/view/15065406/2s8Yeixvw2




## installation
install required packages:
  -> pip install -r requirements.txt

 
to run server
    -> python3 manage.py runserver

to sync database
    -> python3 manage.py migrate --run-syncdb   

## Endpoints
EndPoints                     -         Method 
1 /api/                             - GET
2 /api/authentication/              - GET
3 /api/user                         - GET
4 /api/authentication/login/        - POST
5 /api/authentication/logout/       - GET
6 /api/user/signup/                 - POST 
7 /api/user/deposit/                - POST 
8 /api/user/withdrawal/             - POST
9 /api/user/accountdetails/         - GET
