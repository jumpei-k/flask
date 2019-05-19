# -*- coding: utf-8 -*-
"""
Created on Sat May 18 22:08:11 2019

@author: Jumpei
output to http://localhost:5000/
"""
from flask import Flask, render_template, request, send_file
app = Flask(__name__)

@app.route('/')
def index():
    # index.html をレンダリングする
    title = "title_of_index.html"
    value_dates = [2017, 2018, 2019]
    return render_template('index.html', title=title, value_dates=value_dates)

@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        input_id = request.form['input_id']
    else:
        input_id = "no name."
    return render_template('index.html', title='flask test', name=input_id)

@app.route('/download', methods=['GET', 'POST'])
def download_report():
    input_report_id = request.form['input_report_id']
    value_date = request.form['value_date']
    download_file_name = value_date +'_' + input_report_id + '.csv'
    return send_file(download_file_name, as_attachment=True, \
         attachment_filename=download_file_name)

if __name__ == "__main__":
    app.run(debug=True)