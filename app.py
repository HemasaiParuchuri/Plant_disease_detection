from flask import Flask, render_template, request
from model import predict_image
import utils
from markupsafe import Markup 

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            file = request.files['file']
            img = file.read()
            prediction = predict_image(img)
            print(prediction)
            res = Markup(utils.disease_dic[prediction])
            return render_template('display.html', status=200, result=res)
        except Exception as e:
            print(e)  # It's good practice to log the actual error
            return render_template('index.html', status=500, res="this is not a leaf")
    return render_template('index.html')

@app.route('/togglePlayPause', methods=['POST'])
def togglePlayPause():
    language = request.form['languages']
    return render_template('index.html', language=language)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
