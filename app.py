from flask import Flask, redirect, render_template, request
from db import Database
app = Flask(__name__)

db=Database()

@app.route('/')
def hello_world():
    return render_template('index.html')

#student module 
@app.route("/add-student", methods=['GET', 'POST'])
def addStudent():
    if request.method=='POST':
        stu_roll=request.form['stu_roll']
        f_name=request.form['f_name']
        l_name=request.form['l_name']
        gender=request.form.get('gender')
        dob=request.form['dob']
        stu_adrs=request.form['stu_adrs']
        stu_email=request.form['stu_email']
        stu_pass=request.form['stu_pass']
        stu_pass2=request.form['stu_pass2']
        phone=request.form['phone']
        if stu_pass==stu_pass2:
            db.insert_student(stu_roll, f_name, l_name, gender, dob, stu_adrs, stu_email, stu_pass, phone)
            return redirect('/all-student')
        else:
            return "invalid password"
            
    # print(allTodo)
    allStudent=db.fetch_all_student()
    return render_template('add_student.html',allStudent=allStudent)

@app.route("/all-student", methods=['GET', 'POST'])
def allStudentDeatils():
    # print(allTodo)
    allStudent=db.fetch_all_student()
    return render_template('all_student_details.html',allStudent=allStudent)

if __name__=='__main__':
    app.run(debug=True, port=8000)