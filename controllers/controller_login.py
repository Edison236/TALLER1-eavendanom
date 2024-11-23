from flask import Blueprint, render_template, request, jsonify
from flask_login import LoginManager, login_user, login_required
from models.user import User
from models.dog import Dog

login_bp = Blueprint('user', __name__)

@login_bp.route('/login', methods=['GET','POST'])
def user_login():
    print("si esta llegando")
    if request.method == 'GET':
        return render_template('login.html')
    else: 
        username = request.form["username"]
        password = request.form["password"]
    list_user = User.query.all()
    for user in list_user:
        if user.username == username and user.password == password:
            if user.is_admin == True:  
                dogs = Dog.get_list_dogs()  
                print(dogs)        
                return render_template('tabla.html', dogs = dogs )
            else:
                return render_template('welcome.html', user = username)    
    return render_template('login.html')
            
    


@login_bp.route('/ruta-logueada')
@login_required
def ruta():
    return render_template("ruta-logueada.html")
