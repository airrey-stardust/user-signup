



######  To Do   #####
# 1. error when fields left blank, except email
# 2. error when invalid characters - what email addresses can contain
# 3. character limits


# DO NOT FORGET TO ACTIVATE FLASK IN GIT WHEN RUNNING - source activate flask-env ######

from flask import Flask, render_template, request
import jinja2


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/', methods=['POST', 'GET'])
### OR? #####
#@app.route('/')


def index():

    #variable names and error messages
        
    username = ""
    email = ""
    password = ""
    verify_password = ""
    error_username = ""
    error_password = ""
    error_password_verification = ""
    error_email_message = ""

    ######

    if request.method == 'POST':

######## USERNAME #####
    
        username = request.form['username']

        if username == "":
            error_username = "The username can not be blank."

        for i in username:

            if i.isspace():
               
                error_username = "Spaces are not allowed in the username."
        
        if (len(username) < 3) or (len(username) > 20):
            error_username = "Usernames must be between 3 and 20 characters long."


######### PAsSWORD #####
            
        password = request.form['password']
            
        if password == "":
                error_password = "The password can not be blank."

        for i in password:
                
            if i.isspace():
                error_password = "Passwords can not have spaces."
            
        if (len(password) < 3) or (len(password) > 20):
            error_password = "Passowrds must be between 3 and 20 characters long."

                

#####   PASSWORD VERIFICATION ####
    
        verify_password = request.form['verify_password']
           
        if verify_password == "":
            error_password_verification = "The password verification can not be blank."
            #redundant because of password = verification password in prev step?

        for i in verify_password:

            if i.isspace():
                error_password = "Passwords may not contain spaces"

        if password != verify_password:
            error_password_verification = "The passwords must match. Please verify the passwords."

##########      EMAIL    ######
    
        email = request.form['email']
            
        #email addresses can only contain letters, ., numbers, @
        #must contain @ and ., only one @?
        #make allowed character set? no {}[]? make a list?
        #email address may be blank

            #if email.count('@') != 1:
                #error_email_message = "The email address must contain only one @."
         
        if (len(email) < 3) or (len(email) > 20):
            error_email_message = "Email addresses must be between 3 and 20 characters long and contain an @."

        for i in email:

            if i.isspace():
                error_email_message = "The email address can not contain a space."
                
                
    ############# END TEXT VALIDATION #######           
                

    if not error_username and not error_password and not error_password_verification and not error_email_message:   
        
        return render_template('index.html', username=username, password=password, email=email, verify_password=verify_password, error_email_message=error_email_message, error_password=error_password, error_username=error_username, error_password_verification=error_password_verification)
    
    
    return render_template('hello_user.html', username=username)
    



app.run()
