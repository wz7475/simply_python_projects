from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/oferta-tworzenia-stron-www')
def oferta():
    return render_template("oferta.html")

@app.route('/kontakt-ze-mna')
def kontakt():
    return render_template("kontakt.html")

@app.route('/kim-jestem')
def kimjestem():
    return render_template("kimjestem.html")

@app.route('/curriculum-vitae')
def cv():
    return render_template("cv.html")

if __name__ == "__main__":
    app.run(debug=True)
