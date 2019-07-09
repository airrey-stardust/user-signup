######  To Do   #####
# 1. error when fields left blank, except email
# 2. error when invalid characters - what email addresses can contain
# 3. character limits


# DO NOT FORGET TO ACTIVATE FLASK IN GIT WHEN RUNNING - source activate flask-env ######

from flask import Flask, render_template, request, redirect
import re

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/', methods=['POST', 'GET'])

def index():
    username = ''
    email = ''
    password = ''
    verify_password = ''
    error_username = ''
    error_password = ''
    error_password_verification = ''
    error_email_message = ''

    if request.method == 'POST':
######## USERNAME #####
        username = request.form['username']
        password = request.form['password']
        verify_password = request.form['verify_password']
        email = request.form['email']

        for i in username:
            if i.isspace():
                error_username = 'Spaces are not allowed in the username.'
                username = ''
            else: 
                if(len(username) < 3) or (len(username) > 20):
                    error_username = 'Usernames must be between 3 and 20 characters long.'
                    username = ''
                
        if (username == ''):
            error_username = 'Please enter a username.'
            username = ''   

        
######### PAsSWORD #####
        for i in password:       
            if i.isspace():
                error_password= 'Spaces are not allowed in the username'
                password = ''
            else: 
                if (len(password) < 3) or (len(password) > 20):
                    error_password = 'Passwords must be between 3 and 20 characters long.'
                    password = ''

        if (password == ''):
            error_password = 'Please enter a password.'
            password = ''        

#####   PASSWORD VERIFICATION ####
    

        for i in verify_password:
            if i.isspace():
                error_password_verification = 'Passwords may not contain spaces'
                verify_password = ''
            else: 
                if password != verify_password:
                    error_password_verification = 'The passwords must match. Please verify the passwords.'
                    verify_password = ''
        if (verify_password == ''):
            error_password_verification = 'Please verify the password.'
            verify_password = ''
##########      EMAIL    ######
    
       
            
        if (email != '') and (not re.match('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email)):
            error_email_message = 'The email address is invalid'
            
                
############# END TEXT VALIDATION #######           
        if (not error_username) and (not error_password) and (not error_password_verification) and (not error_email_message):
            return redirect('/hello_user?username={0}'.format(username))

    
    #### this is good #####
    return render_template('index.html', username=username, password=password, email=email, verify_password=verify_password, error_email_message=error_email_message, error_password=error_password, error_password_verification=error_password_verification, error_username=error_username)

### only shows error messages if there is errors in the html form, use jinja ####

@app.route('/hello_user')
def hello_user():
    username = request.args.get('username')
    return render_template('hello_user.html', username=username)

app.run()
