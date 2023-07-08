from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('')


@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    # Perform backend processing here
    output = "Yes"
    return output


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=81)
