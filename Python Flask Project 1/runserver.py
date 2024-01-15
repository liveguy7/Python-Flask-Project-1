from os import environ
from Python_Flask_Project_1 import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
    
    #app.config['SECRET_KEY'] = '5c629f2f2385c7de52baa3a586953a68'


    