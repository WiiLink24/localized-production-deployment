"""
This script clones Wii Room into the folder of your choosing.
This is meant to be used to quickly create an international server for Wii Room.
"""
import os
import subprocess

# First we make the housing directory for the language.
lang = input("Input the language you want to create: ")

# Clone the localized-production-deployment as the language.
subprocess.run(["git", "clone", "https://github.com/WiiLink24/localized-production-deployment.git", lang])

# Enter the directory
os.chdir(lang)

# Make the room-server assets folder
os.mkdir("room-assets")

print("Change your environment file and run docker compose up --build -d")
