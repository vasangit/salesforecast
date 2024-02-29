import json
import os
from flask import Flask,jsonify, request, Response
from flask import request
from flask_cors import CORS
app=Flask(__name__)
CORS(app)
import modelpy
obj=modelpy.Model()

@app.route('/')
def hm():
    return json.dumps("vasanth")

@app.route('/get', methods = ['GET'])
def getf():
    return json.dumps("connected")

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLD = '/Users/vasanthakumarb/Documents/time_series_analysis'
UPLOAD_FOLDER = os.path.join(APP_ROOT, UPLOAD_FOLD)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/home', methods=['POST'])
def upload_file():
    file = request.files['file']

    if 'file' not in request.files:
     print('no file in request')
     return jsonify("no file")

    if file.filename == '':
       print('no selected file')
       return jsonify("file is empty")
    if file :
      #print("hello")
      filename = (file.filename)
      file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      return jsonify("file uploaded ")


@app.route('/val', methods=['POST'])
def getvalue():
        input_data=request.json
        if input_data["period"]=="days":
            input_date=int(input_data["target"])
            result=obj.predict_on_days(input_date)

            return result

        elif input_data["period"]=="months":
            input_month=int(input_data["target"])
            result=obj.predict_on_months(input_month)

            return result

        elif input_data["period"]=="years":
            input_year=int(input_data["target"])
            result=obj.predict_on_years(input_year)

            return result

        elif input_data["period"] == "weeks":
            input_week = int(input_data["target"])
            result= obj.predict_on_weeks(input_week)

            return result


        else:

            return "NOT A PROPER JSON FORMAT"


if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=5003)