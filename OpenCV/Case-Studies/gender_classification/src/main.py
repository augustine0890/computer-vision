import os
from flask import Flask
import views

path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
templates_dir = os.path.join(path, 'templates')
static_dir = os.path.join(path, 'static')

app = Flask(__name__,
            static_folder=static_dir,
            template_folder=templates_dir)
app.add_url_rule('/', 'base', views.base)
app.add_url_rule('/home', 'home', views.homepage, methods=['GET'])
app.add_url_rule('/faceid', 'faceid', views.faceapp, methods=['GET', 'POST'])


if __name__ == '__main__':
    app.run(debug=True)