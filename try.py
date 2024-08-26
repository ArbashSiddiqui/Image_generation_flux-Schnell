import os


from huggingface_hub import login
login(token="Your_hugging_face_access_token")

from  gradio_client import Client 

client=  Client("black-forest-labs/FLUX.1-schnell")
e_prompts = "generate a raw image and realistic image of high quality but make sure image should be realistic"
u_prompts= input("enter you query: ")

result = client.predict(
        prompt= e_prompts+u_prompts, 
        seed= 0,
        randomize_seed= True,
        width=1024,
        height=1024,
        num_inference_steps=4,
        api_name="/infer"
        
        
        
)
print(e_prompts+u_prompts)

print(result)
print ("haha")
