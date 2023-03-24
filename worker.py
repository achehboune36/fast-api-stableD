import os
import requests
from celery import Celery
import base64


celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")

app = Celery('tasks', broker='redis://localhost:6379/0')

@celery.task(name="create_task")
def generate_image_task(prompt, negative_prompt, num_images, size, truncation, alpha, step_size, noise_scale):
    response = requests.post(
        'https://abxr-stable-diff.loca.lt//text2img', json={
            'prompt': prompt, 
            'negative_prompt': negative_prompt, 
            'num_images': num_images, 
            'size': size, 
            'truncation': truncation, 
            'alpha': alpha, 
            'step_size': step_size, 
            'noise_scale': noise_scale
            }
        )

    if response.status_code == 200:
        data = response.json()
        images = data['images']
        for i, image in enumerate(images):
            image_data = base64.b64decode(image)

            with open(f'generated_images/generated_image_{i}.png', 'wb') as f:
                f.write(image_data)

    else:
        print(f'Error generating image: {response.status_code}')
