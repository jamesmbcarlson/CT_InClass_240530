from flask import Flask, request

app = Flask(__name__)

# create a route with the endpoint /
# Status 200 OK on GET, 405 on POST
# Should return "Welcome to the Flask App"
@app.route('/', methods=['GET'])
def index():
    return "Welcome to the Flask App"

# Create a route with the endpoint /add
# Status 405 on GET, 200 on POST
# Should get request body num1 and num2 and return result
# If num1 and/or num2 not in body, default to 0
@app.route('/add', methods=['POST'])
def add():
    data = request.json
    num1 = data.get('num1', 0)
    num2 = data.get('num2', 0)
    return {'result': num1+num2}

if __name__ == "__main__":
    app.run(debug=True)