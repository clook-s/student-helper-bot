from flask import *

main = Flask(__name__)


@main.route('/')
def index():
    return render_template('')


if __name__=='__main__':
    main.run(debug=True)