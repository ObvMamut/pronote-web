from flask import Flask,request,render_template
import pronotepy

app = Flask(__name__, template_folder='templates', static_folder='staticFiles')


@app.route('/')
def hello_world():
    return render_template("page.html", info="")

@app.route('/',methods=['POST','GET'])
def login():
    name=request.form['username']
    pwd=request.form['password']

    client = pronotepy.Client('https://e048000a.index-education.net/pronote/eleve.html',
                                  username=name,
                                  password=pwd)

    avg = client.current_period.overall_average

    return render_template('page.html',info=avg)



if __name__ == '__main__':
    app.run()