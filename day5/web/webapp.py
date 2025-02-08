from flask import Flask, request, render_template
app=Flask(__name__) # create an instance of the Flask class run on localhost:5000

@app.route('/') # decorator to tell Flask what URL should trigger the function
def homepage():
    return "<h1 style='color:blue'>Welcome to Hello page</h1>"

@app.route('/about')
def aboutpage():
    #make db call with threading 
    return "<h2 style='color:green'>TechMojo started ....1970</h2>"

if __name__ == '__main__':
    app.run(debug=True) # run the application        