from flask import Flask
from . import main
from flask_login import login_required
from flask import render_template, redirect, url_for, abort, flash
import datetime
from ..models import User, Pitch, Comment
from .forms import UpdateProfile, PitchForm , CommentForm
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

@main.route('/pitch/new', methods=['GET','POST'])
@login_required
def new_pitch():
    form = PitchForm()

    if form.validate_on_submit():

        title=form.title.data
        content=form.content.data
        category=form.category.data
        pitch = Pitch(title=title, content=content,category=category)
        # pitch.save_pitch(pitch)
        db.session.add(pitch)
        db.session.commit()

        flash('Your pitch has been created!', 'success')
        return redirect(url_for('main.index', id=pitch.id))

    return render_template('new_pitch.html', title='New Post', pitch_form=form, post ='New Post')   
