from flask import Flask, render_template, url_for, request, redirect
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html')
    
    if request.method == 'POST':
        # store the url of the route of backend api
        BACKEND_POST_API_URL = "http://127.0.0.1:8000/create"
        ## get request form from the html templates
        ##  ... and assign them to each key 
        ##   ... and store the dictionary in a variable
        form_data = {
            'first name': request.form.get('first name'),
            'last name': request.form.get('last name'),
            'age': request.form.get('age'),
            'gender': request.form.get('gender')
        }
        # save the requests.post with its two parameters in a variable
        response = requests.post(BACKEND_POST_API_URL, form_data)

        # check if the status is 200 and the go to /student
        if response.status_code == 200:
            return redirect(url_for('student'))
        # if the status if not 200, write an error message
        else:
            return "An Error occur in the POST request !"
    

@app.route ('/student', methods=['GET', 'POST'])
def student():
    # store the url for the rout of the backend api in a variable
    BACKEND_GET_API_URL = "http://127.0.0.1:8000/read"

    # save the requests.get with only one parameter in a variable
    response = requests.get(BACKEND_GET_API_URL)

    # check if the status is 200
    if response.status_code == 200:
        # convert the json format to python object
        response_py = response.json()
        # get the key (data) you want from the python object
        myStudents = response_py.get('students', [])
        # return render template student.html
        return render_template('student.html', myStudents = myStudents)
    # check if the status is not 200, return render error
    else:
        return "The GET methord has an error"
    

if __name__ == '__main__':
    app.run(port=5000, debug=True)