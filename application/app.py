from utils import *
from model import *

token_file= "model/token.txt"
# user_prompt= "A cowboy shooting a shotgun while riding a motorcycle."

app= Flask(__name__)
app.config['SECRET_KEY']= secrets.token_hex(16)
num_output= 1

@app.route('/')
def hello():
    return render_template(
        "index.html", 
        btn_range= range(num_output), 
        prompt_images= ["/static/images/placeholder_image.png" for i in range(num_output)]
    )

@app.route('/prompt', methods=['POST', 'GET'])
def prompt():
    print("user prompt received:", request.form['prompt_input'])
    call_model(token_file= token_file, user_prompt= request.form['prompt_input'])

    return render_template(
        "index.html", 
        btn_range= range(num_output), 
        prompt_images= ["/static/images/output_image.png" for i in range(num_output)]
    )

@app.route('/supersample', methods=['POST', 'GET'])
def supersample():
    print("save button", request.form['save_btn'], "was clicked!")
    output_dir= 'output'
    if not os.path.exists(output_dir): os.makedirs(output_dir)
    src, dst= 'application/static/images/output_image.png', f'{output_dir}/output_image.png'
    shutil.copy(src, dst)
    Image.open(dst).show()
    try:
        if platform.system() == "Windows":
            os.startfile(output_dir)
        elif platform.system() == "Darwin":
            subprocess.run(["open", output_dir])
        else:
            subprocess.run(["xdg-open", output_dir])
    except:
        pass


    return render_template(
        "index.html", 
        btn_range= range(num_output), 
        prompt_images= ["/static/images/output_image.png" for i in range(num_output)]
    )
