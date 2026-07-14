import requests

prompt="Monkey D. Luffy standing atop the legendary One Piece treasure on Laugh Tale, smiling triumphantly as the newly crowned Pirate King. Golden sunrise, dramatic ocean backdrop, flowing red captain's coat, cinematic anime style, ultra-detailed, vibrant colors, dynamic composition, volumetric lighting, masterpiece, 8K."
url=f"https://image.pollinations.ai/prompt/{prompt}"

print(f"Generating for:{prompt}")

response=requests.get(url)

print(response)

if response.status_code==200:
    with open("GOAT.png","wb") as file:
        file.write(response.content)
    print("Sucess")
else:
    print("error")