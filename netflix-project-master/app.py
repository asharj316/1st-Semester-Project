from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'


users = [
    {"email": "zhengpou@gmail.com", "password": "phpzindabad", "username": "callmecj_3"},
    {"email": "asharjaffery7@gmail.com", "password": "gptzindabad", "username": "muhammad.ashar7"}
]

@app.route('/')
def netflix():
    return render_template('netflix.html')  

@app.route('/main')
def main():
    return render_template('main.html')  

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email_or_username = request.form.get('email_or_username')
        password = request.form.get('password')

        
        for user in users:
            if user["email"] == email_or_username or user["username"] == email_or_username:
                if user["password"] == password:
                    flash(f"Welcome back {user['username']}!", "success")
                    return redirect(url_for('main'))  
                else:
                    flash("Incorrect password!", "danger")
                    return redirect(url_for('login'))
        flash("No account found with those credentials!", "danger")
        return redirect(url_for('login'))

    return render_template('login.html')  

@app.route('/logout')
def logout():
    flash("You have been logged out successfully.", "info")
    return redirect(url_for('login'))  

if __name__ == '__main__':
    app.run(debug=True)
