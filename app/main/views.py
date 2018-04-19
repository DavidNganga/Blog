from . import main

@main.route('/')
def index():
    return '<h1> Hello World </h1>'
    return render_template('index.html')

# @main.route('/movie/review/new/<int:id>', methods = ['GET','POST'])
# @login_required
# def new_review(id):
