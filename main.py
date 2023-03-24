from fastapi import FastAPI, Request
import os
from worker import generate_image_task

app = FastAPI()

default_params = {
    'num_images': 1,
    'size': 512,
    'truncation': 0.7,
    'alpha': 1.0,
    'step_size': 0.05,
    'noise_scale': 0.1,
}

@app.post("/generate-image")
async def generate_image(request: Request, data: dict):
    prompt = data.get('prompt')
    negative_prompt = data.get('negative_prompt')
    model = data.get('model', 'stabilityai/stable-diffusion-2-1')
    num_images = data.get('num_images', default_params['num_images'])
    size = data.get('size', default_params['size'])
    truncation = data.get('truncation', default_params['truncation'])
    alpha = data.get('alpha', default_params['alpha'])
    step_size = data.get('step_size', default_params['step_size'])
    noise_scale = data.get('noise_scale', default_params['noise_scale'])

    data = {
        'prompt': prompt,
        'negative_prompt': negative_prompt,
        'num_images': num_images,
        'size': size,
        'truncation': truncation,
        'alpha': alpha,
        'step_size': step_size,
        'noise_scale': noise_scale
    }

    if model:
        os.environ['X2IMG_MODEL'] = model

    generate_image_task.delay(prompt, negative_prompt, num_images, size, truncation, alpha, step_size, noise_scale)

    return 200
