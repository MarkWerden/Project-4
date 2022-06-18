from binascii import Incomplete
from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

@app.route('/')
def hello():
   return render_template('index.html')



@app.route('/', methods =["POST"])
def gfg():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       gender = request.form.get("gender")
       print(gender)
       married = request.form.get("married")
       print(married)
       dependents = request.form.get("dependents")
       print(dependents)
       education = request.form.get("education")
       print(education)
       employment = request.form.get("employment")
       print(employment)
       income_applicant = request.form.get("income_applicant")
       print(income_applicant)
       income_coapplicant = request.form.get("income_coapplicant")
       print(income_coapplicant)
       loan = request.form.get("loan")
       print(loan)
       credit = request.form.get("credit")
       print(credit)

       data = []
       data.append(int(income_applicant))
       data.append(int(income_coapplicant))
       data.append(int(loan))
       data.append(int(credit))
       if gender == "Male":
           data.append(0)
           data.append(1)
       else:
           data.append(1)
           data.append(0)
       if married == "Yes":
           data.append(0)
           data.append(1)
       else:
           data.append(1)
           data.append(0)
       if dependents == "0":
           data.append(1)
           data.append(0)
           data.append(0)
           data.append(0)
       elif dependents == "1":
           data.append(0)
           data.append(1)
           data.append(0)
           data.append(0)
       elif dependents == "2":
           data.append(0)
           data.append(0)
           data.append(1)
           data.append(0)
       else:
           data.append(0)
           data.append(0)
           data.append(0)
           data.append(1)
       if education == "Non-Graduate":
           data.append(0)
           data.append(1)
       else:
           data.append(1)
           data.append(0)
       if employment == "Yes":
           data.append(0)
           data.append(1)
       else:
           data.append(1)
           data.append(0)
    print(data)
    loaded_model = pickle.load(open("finalized_model.sav", 'rb'))
    result = loaded_model.predict(np.array(data, dtype=np.int32).reshape(1,-1))
    print(f"result = {result}")
    if result[0] == 0:
        output = "Not Approved"
    else:
        output = "Approved"

  





       # getting input with name = lname in HTML form
    #    last_name = request.form.get("lname")
    #    return "Your name is "+first_name + last_name
    return render_template("index.html", result=output)


if __name__ == '__main__':
    app.run(debug=True)

# Index(['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Gender_Female',
#        'Gender_Male', 'Married_No', 'Married_Yes', 'Dependents_0',
#        'Dependents_1', 'Dependents_2', 'Dependents_3+', 'Education_Graduate',
#        'Education_Not Graduate', 'Self_Employed_No', 'Self_Employed_Yes'],

