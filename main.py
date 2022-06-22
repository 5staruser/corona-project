from flask import Flask,render_template,request
app = Flask(__name__)
import pickle
file=open("model.pkl","rb")
clf=pickle.load(file)
file.close()
@app.route("/",methods=["GET","POST"])
def hello_world():
    if request.method=="POST":
        mydict=request.form
        fever=int(mydict["fever"])
        age=int(mydict["age"])
        pain=int(mydict["pain"])
        runnyNose=int(mydict["runnyNose"])
        diffBreath=int(mydict["diffBreath"])
        inputFeatures=[fever,pain,runnyNose,age,diffBreath]
        infprob=clf.predict_proba([inputFeatures])[0][1]
        print(infprob)
        return render_template('show.html', inf=round(infprob*100))
    return render_template("index.html")
    # return "<p>Hello, World!</p>"+ str(infprob)
if __name__ == '__main__':
    app.run(debug=True)