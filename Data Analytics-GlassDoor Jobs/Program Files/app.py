from flask import Flask,render_template
app = Flask(__name__,template_folder='templates')
@app.route('/')
def helloworld():
    return render_template('index1.html')

if __name__=='__main__':
    app.run(debug=True,port=3300)

