from pygame import mixer
import os
path = os.listdir()
print("----------------------------------------------------------------")
print("перекиньте музыку в директорию с ctOS:")
print("ЧТОБЫ ВЫЙТИ НАПИШИТЕ exit")
print(path)
print("----------------------------------------------------------------")
work = True
while(work):
    file = input("напишите название файла: ")
    if (file != "exit"):
        mixer.init()
        mixer.music.load(file)
        mixer.music.play()
        print("Загрузка...")
    if (file == "exit" or file == "Exit"):
        print("Выход...")
        work = False