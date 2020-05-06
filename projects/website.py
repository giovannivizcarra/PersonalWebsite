from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
#def template():
 #   return render_template('template.html')
#@app.route('/home/')
def home():
    return render_template('home.html')

@app.route('/LEDHARP/')
def LEDHARP():
    return render_template('LEDHARP.html')
@app.route('/McnairPresentation/')
def McnairPresentation():
    return render_template('McnairPresentation.html')
@app.route('/QRAM/')
def QRAM():
    return render_template('QRAM.html')
@app.route('/QRAMFinalPaper/')
def QRAMFinalPaper():
    return render_template('QRAMFinalPaper.html')
if __name__ == '__main__':
    app.run(debug=True)



