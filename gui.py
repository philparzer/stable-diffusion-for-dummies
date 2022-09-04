import os
import sys
import utils
from colorama import init, Fore
import pyinputplus as pyip

def main():
    init()
    os.system('CLS')
    print(f'{Fore.YELLOW}Read up on the documentation at https://github.com/philparzer/stable-diffusion-for-dummies#readme if you have any troubles\n{Fore.WHITE}')
    print(f'{Fore.BLUE}')
    response = pyip.inputMenu(['txt2img', 'img2img'], numbered=True)
    print(f'{Fore.GREEN}Starting graphical user interface for {response}')
    print(f'{Fore.WHITE}(ALT + left click on the link "Running on local URL: {Fore.YELLOW}<URL>{Fore.WHITE}" in the console as soon as the model has loaded)\n')

    os.system(f'python optimizedSD/{response}_gradio.py')

if __name__ == "__main__":
    main()