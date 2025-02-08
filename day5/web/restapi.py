from flask import Flask, jsonify, request

app = Flask(__name__)  # Create an instance of the Flask class

# Sample customer data
customers = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]

@app.route('/')  # Define the route for the root URL of the web server
def welcome():
    return jsonify({"message": "Welcome to the API"})  # Return a JSON response

@app.route('/customers', methods=['GET'])  # Define the route for getting customers
def get_customers():
    return jsonify(customers)  # Return the list of customers as a JSON response

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app with debug mode enabled