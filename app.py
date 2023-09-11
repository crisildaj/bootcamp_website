from flask import Flask, Response, request, render_template
app = Flask(__name__, static_folder='static')
app.config['STATIC_FOLDER'] = 'static'

@app.route('/')
@app.route('/home', methods=['GET'])
def home():
    return render_template('index.html', title='Technophobes')

if __name__ == "__main__":
    # Execute only if ran directly as a program
    # Ignore if imported as a module.
    app.run(debug=True)