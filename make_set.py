import os
import requests
import playsound
import time
import shutil

with open("apikey.key", "r") as f:
    key = f.read()
def does_folder_exist(folder):
    if os.path.exists(folder) == False:
        raise FileExistsError

def get_voice(text, i, path):
    url = "https://api.elevenlabs.io/v1/text-to-speech/pNInz6obpgDQGcFmaJgB"

    payload = {
    "text": f"{text}",
    "model_id": "eleven_multilingual_v2",
    "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.8,
        "style": 0.0,
        "use_speaker_boost": True
    }
}


    headers = {
        "xi-api-key": f"{key}",
        "Content-Type": "application/json"
    }
    response = requests.request("POST", url, json=payload, headers=headers)
    try:
        os.makedirs(f"./sets/{path}")
    except FileExistsError:
        pass

    if response.ok:
    # Open the output file in write-binary mode
        voice_filename = f"voice_{i}.mp3"
        with open(f"./sets/{path}/{voice_filename}", "wb") as f:
            
            # Read the response in chunks and write to the file
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)
        # Inform the user of success
        print("Audio stream saved successfully.")
    else:
        # Print the error message if the request was not successful
        print(response.text)



def does_file_exist(file_name):
    if os.path.isfile(f"./answers/{file_name}.txt") == True:
        return True
    else:
        raise FileNotFoundError(f"File Does not exist")
    

    



while True:
    try:
        file_name = str(input("filename of answers: "))
        does_file_exist(file_name)
        break
    except FileNotFoundError:
        print("File Does not exist! Try again")


folder_name = str(input("Folder to store sets in: "))


individual_answers = []
with open(f"./answers/{file_name}.txt") as f:
    for line in f:
        # Add each line to the list, stripping newline characters
        individual_answers.append(line.strip())

i = 1
for answer in individual_answers:
    get_voice(answer, i, folder_name)
    i += 1