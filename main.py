from flask import *

main = Flask(__name__)

@main.route('/')
def index():
    return 'мой первый проект с git!!!'

if __name__=='__main__':
    main.run(debug=True)