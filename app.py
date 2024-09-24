# from flask import Flask, request, jsonify, render_template
# import re

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/flag')
# def flag():
#     input_text = request.args.get('input', '')
#     if re.match(r'^p.....F!?', input_text):
#         return jsonify({'flag': 'Congratulations! The flag is FLAG{correct_input}'})
#     else:
#         return jsonify({'flag': 'Incorrect input'})

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, request, jsonify, render_template
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/flag')
def flag():
    input_text = request.args.get('input', '')
    # Adjust the regex pattern to match the riddle's answer
    if re.match(r'^[Mm][aA][tT][rR][iI][xX][cC][tT][fF]!$', input_text):
    # if re.match(r'^matrixCTF!?', input_text, re.IGNORECASE):
        return jsonify({'flag': 'Congratulations! The flag is CTFFLAG{CSAM 2024 flag matched}'})
    else:
        return jsonify({'flag': 'Incorrect input'})

if __name__ == '__main__':
    app.run(debug=True)
