from flask import Flask 
app = Flask(__name__) 
  
@app.route('/') 
def hello(): 
    # marked = false
    return "welcome to the flask tutorials dsfds"
  
def failedTestMethod(v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20, v21, v22, v23, v24, v25, v26, v27):
  print("in the FailedTestMethod")
  
  
if __name__ == "__main__": 
    app.run(host ='0.0.0.0', port = 5001, debug = True)
