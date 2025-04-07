from flask import Flask, render_template, request
from PIL import Image
import secrets

app= Flask(__name__)
app.config['SECRET_KEY']= secrets.token_hex(16)
num_output= 3

@app.route('/')
def hello():
    return render_template(
        "index.html", 
        btn_range= range(num_output), 
        prompt_images= ["/static/images/placeholder_image copy.png" for i in range(num_output)]
    )

@app.route('/prompt', methods=['POST', 'GET'])
def prompt():
    print("user prompt received:", request.form['prompt_input'])
    
    return render_template(
        "index.html", 
        btn_range= range(num_output), 
        prompt_images= ["/static/images/placeholder_image.png" for i in range(num_output)]
    )

@app.route('/supersample', methods=['POST', 'GET'])
def supersample():
    print("save button", request.form['save_btn'], "was clicked!")

    return render_template(
        "index.html", 
        btn_range= range(num_output), 
        prompt_images= ["/static/images/placeholder_image.png" for i in range(num_output)]
    )

if __name__ == '__main__':
    app.run(
        host= '0.0.0.0', 
        port= 8000, 
        debug= True
    )   

