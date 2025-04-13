from utils import *

def call_model(token_file:str, user_prompt:str):

    try:
        with open(token_file, "r") as file:
            API_TOKEN= file.read().strip()
    except FileNotFoundError:
        print(f"Error: {token_file} not found. Please create it and add your Hugging Face token.")
        exit(1)

    API_URL= "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4"
    headers= {"Authorization": f"Bearer {API_TOKEN}"}
    payload= {
        "inputs": user_prompt,
        "parameters": {
            "num_inference_steps": 50,
            "guidance_scale": 7.5
        }
    }

    output_dir= "application/static/images"

    max_retries= 3
    retry_delay= 10

    for attempt in range(max_retries):
        response= requests.post(API_URL, headers= headers, json= payload)
        
        if response.status_code == 200:
            image_data= response.content
            image= Image.open(BytesIO(image_data))
          
            output_path= os.path.join(output_dir, "output_image.png")
            image.save(output_path)
            print("Image successfully saved to", output_path)
            # image.show()
            break
        elif response.status_code == 503:
            print(f"503 Error: Model is loading. Waiting {retry_delay} seconds...")
            time.sleep(retry_delay)
        else:
            print(f"Error: {response.status_code} - {response.text}")
            break
    else:
        print("All attempts failed. Please try again later!")