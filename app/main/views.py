from flask import Flask
from . import main
from flask_login import login_required
from flask import render_template

from ..models import User

from .. import db
app = Flask(__name__)


# views
@main.route("/")
def index():
   '''
   title = "Pitch Perfect"
   '''
   title = 'Pitch Perfect'
   

   return render_template('index.html', title= title)
