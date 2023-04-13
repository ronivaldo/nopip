from nopip import install

install.from_requirements('./requirements.txt')
install.module('requests')
install.modules(['requests==2.5.1', 'beautifulsoup4==4.10.0'])

try:
    from flask import Flask
except:
    install.module('Flask==2.2.3')


from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'