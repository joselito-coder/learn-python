from flask import Flask
from flask import render_template
import pickle


with open('model.pkl','rb') as model:
    clf = pickle.load(model)

app = Flask(__name__)

@app.route("/")
def hello_world():

    # Code for inference
    input_feature = [[110,1,22,1,1]]
    infProb = clf.predict_proba(input_feature)[0][1]

    # return "<p>Hello, World!</p> "+ str(infProb)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)