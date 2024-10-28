from flask import Flask,jsonify
from data import x
app=Flask(__name__)

@app.route('/getdata')
def getdata():
    return jsonify(x)

if __name__=="__main__":
    app.run()
