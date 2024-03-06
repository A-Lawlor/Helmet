from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle file upload
        f = request.files['datafile']
        # Read the file content
        content = f.read().decode('utf-8')
        # You might want to process this content or save it for later use
        # ...
        return content  # Sending the file content back to the frontend
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)