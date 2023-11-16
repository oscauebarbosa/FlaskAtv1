from flask import Flask, render_template

app = Flask(__name__)



@app.route('/futuro')
def futuro():
    return render_template('site1.html')

@app.route('/selo')
def selo():
    return render_template('site2.html')

@app.route('/hamburguer')
def hamburguer():
    return render_template('site3.html')



if __name__ == '__main__':
    app.run()
