from flask import Flask, jsonify

# Create app instance to create flask app
app = Flask(__name__)


# Create app route
@app.route("/api/home", methods=['GET'])
def return_home():
    return jsonify({
        'message': "Hello world!"
    })



# Create a way to run the app
if __name__ == '__main__':
    # Lets the file know you're in development mode.  Only remove 'debug=True' if you will deploy the app into production.
    app.run(debug=True)