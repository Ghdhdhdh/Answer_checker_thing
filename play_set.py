import os
import playsound

def does_file_exist(file_name):
    if os.path.isfile(f"./sets/{file_name}.txt") == True:
        return True
    else:
        raise FileNotFoundError(f"File Does not exist")
    
def does_folder_exist(folder):
    if os.path.exists(f"./sets/{folder}") == False:
        raise FileExistsError
    
with open("apikey.key", "r") as f:
    key = f.read()

while True:
    try:
        folder_name = str(input("filename of answers: "))
        does_folder_exist(folder_name)
        break
    except FileNotFoundError:
        print("Folder Does not exist! Try again")
i = 1
while True:
    try:
        playsound.playsound(f"sets/{folder_name}/voice_{i}.mp3")
        i += 1
        temp = input("Press Enter for next")
    except FileExistsError:
        print("No More Files!")
        break
    except KeyboardInterrupt:
        print("\nStopped!")
        break
    

    
