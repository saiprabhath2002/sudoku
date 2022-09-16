from flask import Flask ,request,render_template,redirect,jsonify
import configparser
from datetime import datetime
import sys
import numpy
#from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)

def find_zero(s):
    for i in range(len(s)):
        for j in range(len(s[0])):
            if(s[i][j]==0):
                    return(i,j)
    return None
def valid(s,row,cl,n):
    for i in range(len(s[0])):
        if(s[row][i]==n and i!=cl):
            return False
    for i in range(len(s)):
        if(s[i][cl]==n and i!=row):
            return False
    box_x = cl // 3
    box_y = row // 3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if s[i][j] == n and (i,j) != (row,cl):
                return False
    return True
def solve(s):
    find=find_zero(s)
    if not find:
        return True
    else:
        r,c=find
    for i in range(1,10):
        if valid(s,r,c,i):
            s[r][c]=i
            if(solve(s)):
                return True
            s[r][c]=0
    return False
@app.route('/')
def index():
    return render_template('ans.html')
@app.route('/solve1',methods=['POST'])
def solve1():
    s=numpy.zeros(81)
    for i in range(0,81):
        stri="cell-"+str(i)
        s[i]=int(request.form[stri])
    new=s.reshape(9,9)
    solve(new)
    new=new.reshape(1,81)
    new=new.astype(int)
    return render_template('home.html',arr=new)
if __name__=="__main__":
    app.run(host="0.0.0.0" ,port=5000)