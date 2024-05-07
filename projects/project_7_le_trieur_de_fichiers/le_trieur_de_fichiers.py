"""
Trier les fichiers contenus dans le dossier data selon les associations suivantes :
mp3, wav, flac : Musique
avi, mp4, gif : Videos
bmp, png, jpg : Images
txt, pptx, csv, xls, odp, pages : Documents
autres : Divers
"""

from pathlib import Path

files_type = {
    "Musique" : [".mp3", ".wav", ".flac"],
    "Videos" : [".avi", ".mp4", ".gif"],
    "Images" : [".bmp", ".png", ".jpg"],
    "Documents" : [".txt", ".pptx", ".csv", ".xls", ".odp", ".pages"]
}

path = Path.cwd().joinpath("data")

path_music = path.joinpath("Musique")
path_videos = path.joinpath("Videos")
path_pictures = path.joinpath("Images")
path_documents = path.joinpath("Documents")
path_various = path.joinpath("Divers")

path_music.mkdir(exist_ok=True)
path_videos.mkdir(exist_ok=True)
path_pictures.mkdir(exist_ok=True)
path_documents.mkdir(exist_ok=True)
path_various.mkdir(exist_ok=True)

files_in_folder_data = [f for f in path.iterdir() if f.is_file()]

for f in files_in_folder_data : 
    if f.suffix in files_type["Musique"] : 
        f.replace(path_music / f.name)
    elif f.suffix in files_type["Videos"] :
        f.replace(path_videos / f.name)
    elif f.suffix in files_type["Images"] :
        f.replace(path_pictures / f.name)
    elif f.suffix in files_type["Documents"] :
        f.replace(path_documents / f.name)
    else : 
        f.replace(path_various / f.name)