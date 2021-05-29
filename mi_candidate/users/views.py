# mi_candidate/users/views.py
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from mi_candidate import db
from werkzeug.security import generate_password_hash,check_password_hash
from mi_candidate.models import User, BlogPost
from mi_candidate.users.forms import RegistrationForm, LoginForm, UpdateUserForm
from mi_candidate.users.picture_handler import add_profile_pic


##############################
# USERS BLUEPRINT INSTANTIATION
##############################
users = Blueprint('users', __name__)

##############################
# USER REGISTRY VIEW #########
##############################
@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    # this operates on submit only
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering! Now you can login!')
        return redirect(url_for('users.login'))
    # this is whats is rendered on route
    return render_template('register.html', form=form)

##############################
# USER LOGIN VIEW ############
##############################
@users.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        # Grab the user from our User Models table
        user = User.query.filter_by(email=form.email.data).first()

        # Check that the user was supplied and the password is right
        # The verify_password method comes from the User object
        if user.check_password(form.password.data) and user is not None:
            #Log in the user
            login_user(user)
            flash('Logged in successfully.')
            # If a user was trying to visit a page that requires a login
            # flask saves that URL as 'next'.
            next = request.args.get('next')

            # So let's now check if that next exists, otherwise we'll go to
            # the welcome page.
            if next == None or not next[0]=='/':
                next = url_for('core.index')

            return redirect(next)
    return render_template('login.html', form=form)

##############################
# USER ACCOUNT UPDATE ##########
##############################
@users.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateUserForm()

    if form.validate_on_submit():
        if form.picture.data:
            username = current_user.username
            # imported from picture_handler.py
            pic = add_profile_pic(form.picture.data,username)
            current_user.profile_image = pic

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('User Account Updated')
        return redirect(url_for('users.account'))

    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    profile_image = url_for('static', filename='profile_pics/' + current_user.profile_image)
    return render_template('account.html', profile_image=profile_image, form=form)

##############################
# USER VIEW ##################
##############################
@users.route("/<username>")
def user_posts(username):
    # TODO: create template
    # alows to circle if several pages to present
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    blog_posts = BlogPost.query.filter_by(author=user).order_by(BlogPost.date.desc()).paginate(page=page, per_page=5)
    return render_template('user_blog_posts.html', blog_posts=blog_posts, user=user)

##############################
# LOGOUT USER VIEW ###########
##############################
@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('core.index'))
