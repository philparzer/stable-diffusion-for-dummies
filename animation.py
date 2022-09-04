import os
import sys
import utils
import pyinputplus as pyip
from colorama import init, Fore, Style

def main():
    init()

    os.system('CLS')
    print(f'{Fore.YELLOW}Read up on the documentation at https://github.com/philparzer/stable-diffusion-for-dummies#readme if you have any troubles\n{Fore.WHITE}')

    init_image_path = pyip.inputStr(f"\n{Fore.BLUE}Enter the PATH to your image:{Fore.WHITE}\nRight click on image, click 'Copy Path' and paste\n")
    try:
        utils.check_init_img_path(init_image_path)
    except Exception as e:
        print(f"\n{Fore.RED}Not a valid path, right click on the image and choose 'Copy Path' and paste the value into the console")
        return
    print(f'{Fore.GREEN}Set PATH to "{init_image_path}"')

    prompt = pyip.inputStr(f"\n{Fore.BLUE}Enter your PROMPT:{Fore.WHITE}\nWe recommend using the same prompt as the init image.\n")
    print(f'{Fore.GREEN}Set PROMPT to "{prompt}"')

    strength = pyip.inputFloat(f'\n{Fore.BLUE}Specify how much the created images should resemble the original image.\nEnter a value between 0.0 (indistinguishable) and 0.9 (minor similarity):{Fore.WHITE}\nWe recommend 0.5, press enter to use 0.5.\n', min=0.0, max=0.9, default=0.5, blank=True)
    if (strength == ""):
        strength = 0.5
    print(f'{Fore.GREEN}Set STRENGTH to {strength}')

    frames = pyip.inputInt(f'\n{Fore.BLUE}Enter the number of FRAMES you want to generate:{Fore.WHITE}\nThe default number of frames is 40, press enter to use 40.\n', default = 40, blank=True)
    if (frames == ""):
        frames = 40
    print(f'{Fore.GREEN}Set FRAMES to {frames}')

    zoom_factor = pyip.inputFloat(f'\n{Fore.BLUE}Enter your ZOOM FACTOR (a decimal point value bigger than one):{Fore.WHITE}\nWe recommend 1.1, press enter to use 1.1\n', min = 1.001, default = 1.1, blank=True)
    if (zoom_factor == ""):
        zoom_factor = 1.1
    print(f'{Fore.GREEN}Set ZOOM FACTOR to {zoom_factor}')

    print(f'\n{Fore.YELLOW}STARTING...\n{Fore.WHITE}')

    command = f'python optimizedSD/optimized_animation.py --prompt "{prompt}" --init-img "{init_image_path}" --frames "{frames}" --strength "{strength}" --zoom-factor "{zoom_factor}"' 

    os.system(command)

if __name__ == "__main__":
    main()