import requests
import base64
import json

url = 'http://localhost:8000/generate-image'
prompt = 'kangaroo boxing with sand bag'
negative_prompt = 'blood'
num_images = 3
size = 512
truncation = 0.7
alpha = 0.5
step_size = 0.1
noise_scale = 0.05

response = requests.post(url, 
                         json={
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

# if response.status_code == 200:
#     data = response.json()
#     images = data['images']
#     for i, image in enumerate(images):
#         image_data = base64.b64decode(image)

#         with open(f'generated_image_{i}.png', 'wb') as f:
#             f.write(image_data)

# else:
#     print(f'Error generating image: {response.status_code}')
