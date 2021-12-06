from flask import Flask,request
from flask import render_template
import pickle


with open('model.pkl','rb') as model:
    clf = pickle.load(model)

app = Flask(__name__)

@app.route("/",methods=['post','get'])
def hello_world():
    if request.method == "POST":
        print(request.form)
        values  = request.form

        fever = int(values['fever'])
        age = int(values['age'])
        pain = int(values['pain'])
        runnyNose = int(values['runnyNose'])
        diffBreath = int(values['diffBreath'])

        # Code for inference
        input_feature = [[fever,pain,age,runnyNose,diffBreath]]
        infProb = clf.predict_proba(input_feature)[0][1]
        print(infProb)
        infProb = round(infProb* 100) 
        return render_template('show.html',inf=infProb)

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)