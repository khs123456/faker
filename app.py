# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import random
import csv

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
    
@app.route("/result")
def result():
    # 이름 받아오기
    name1 = request.args.get('name1')
    name2 = request.args.get('name2')
    
    # 랜덤으로 궁합 막 던져주기
    match = random.randrange(50,101)
    
    # names.csv 파일에 이름 저장하기
    f = open('names.csv','a')
    a = csv.writer(f)
    a.writerow([name1, name2])
    f.close()
    return render_template('result.html',name1=name1,name2=name2,match=match)
 
@app.route("/admin")
def admin():
    f = open('names.csv','r')
    rr = csv.reader(f)
    names = rr
    return render_template('admin.html', names=names)
    
# app.run(host='0.0.0.0', port='8080', debug=True)