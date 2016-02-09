from flask import Flask 
from flask import render_template
app = Flask(__name__)
@app.route('/') 

# def hello_world():
# 	return 'Hello World!'

def hello():
	return render_template('/templates/template1.html')	
	
if __name__ == '__main__': 
	app.run()