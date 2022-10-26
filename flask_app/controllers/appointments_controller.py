from flask_app import app, bcrypt
from  flask import render_template, redirect , request , session

# this imports the model file
# from flask_app.models import model_table_name

# Display homepage route
@app.route('/')
def home_page():
    return render_template('home.html')

# Display about us route
@app.route('/about/us')
def about_us():
    return render_template('aboutUs.html')

# Display Services route
@app.route('/services')
def services():
    return render_template('services.html')

# # Display Book appt route
@app.route('/book/appointment')
def aboutUs():
    return render_template('bookAppt.html')

# Display Request a Quote route
@app.route('/request/quote')
def quotes():
    return render_template('quotes.html')

# ACTION ROUTE
@app.route('/table_name/create', methods=['POST'])
def table_name_create():
    return redirect('/')

# Display route
@app.route('/table_name/<int:id>')
def table_name_show(id):
    return render_template('table_name_show.html')

# Display route
@app.route('/table_name/<int:id>/update', methods=['POST'])
def table_name_edit(id):
    return render_template('table_name_edit.html')

# ACTION ROUTE
@app.route('/table_name/<int:id>/update', methods=['POST'])
def table_name_update(id):
    return redirect('/')

@app.route('/table_name/<int:id>/delete')
def table_name_delete(id):
    return redirect('/')