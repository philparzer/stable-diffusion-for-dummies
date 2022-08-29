import os
import sys
import utils
from colorama import init, Fore
import pyinputplus as pyip

def main():
    init()

    response = pyip.inputMenu(['txt2img', 'img2img', 'inpaint'], numbered=True)

    os.system(f'python optimizedSD/{response}_gradio.py')

if __name__ == "__main__":
    main()