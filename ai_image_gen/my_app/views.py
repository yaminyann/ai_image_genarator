import requests
from django.shortcuts import render
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/dreamlike-art/dreamlike-photoreal-2.0"
headers = {
    "Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_TOKEN')}"
}

def prompt_input(request):
    return render(request, 'prompt_input.html')

def generate_image(request):
    if request.method == "POST":
        prompt = request.POST.get("prompt")

        try:
            response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
            
            if response.status_code == 200:
                image_data = response.content
                # Save image temporarily
                image_path = "static/generated.png"
                with open(image_path, "wb") as f:
                    f.write(image_data)
                return render(request, 'generated_image.html', {
                    'prompt': prompt,
                    'image_url': "/" + image_path
                })
            else:
                return render(request, 'generated_image.html', {
                    'error': f"HuggingFace Error: {response.status_code} - {response.text}"
                })

        except Exception as e:
            return render(request, 'generated_image.html', {
                'error': str(e)
            })
