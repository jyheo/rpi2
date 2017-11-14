from flask import Flask
from flask import render_template
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello():
    return 'Hello World'


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/greeting')
@app.route('/greeting/<name>')
def greeting(name=None):
    return render_template('greeting.html', name=name)


@app.route('/formtest', methods=['POST', 'GET'])
def form_test():
    if request.method == 'POST':
        return 'Username: %s' % (request.form['username'])
    else:
        return '''  <form action="/formtest" method="post">
            Name: <input name="username" type="text" /> <br/>
            <input value="Send" type="submit" />
        </form>  '''


@app.route('/list')
def list():
    retstr = ""
    with open('list.txt') as f:
        for l in f.readlines():
            retstr += l + '<br/>'
    return retstr


@app.route('/write', methods=['POST', 'GET'])
def write_article():
    if request.method == 'POST':
        article = request.form['article']
        with open('list.txt', 'a') as f:
            f.write(article)
            return 'Write Successful'
        return 'Write Error'
    else:
        return '''  <form action="/write" method="post">
            Article: <input name="article" type="text" /> <br/>
            <input value="Write" type="submit" />
        </form>  '''


if __name__ == '__main__':
    app.run(host='0.0.0.0')

