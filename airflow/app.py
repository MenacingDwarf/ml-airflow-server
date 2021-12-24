import os
from flask import Flask, request, render_template,url_for
from predict import predict

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        print('Taking text!')
            
        text_to_predict = request.form['text_to_predict']
        result = predict([text_to_predict])[0]

        return render_template('image_score.html',result=result)
        
    return render_template('image_score.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5005)
