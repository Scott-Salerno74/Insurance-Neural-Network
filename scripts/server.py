from flask import Flask
from flask import jsonify
from flask import request
import kmeans_insurance as insurance
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello, world!"

@app.route('/get_some_data')
def hello_world_2():
   return jsonify(
        boundary1=500, 
        boundary2 = 1000
        )

# accept arguemnts from url 
# http://127.0.0.1:3000/send-data?prescriptions=5&age=55&salary=65000
@app.route('/send-data')
def get_parameters():
    insurance.kmeans_on_insurance_data
    user_input_prescriptions = request.args.get('prescriptions', default = 1, type = int)
    user_input_age = request.args.get('age', default = 1, type = int)
    user_input_salary = request.args.get('salary', default = 1, type = int)
    array = [user_input_prescriptions, user_input_age, user_input_salary]
    premium_range = insurance.hit_the_nuke_button(array)
    return jsonify(
        boundary1 = premium_range[0], 
        boundary2 = premium_range[1]
    )
