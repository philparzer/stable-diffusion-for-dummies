import os
import sys
import utils
import pyinputplus as pyip
from colorama import init, Fore
import pyinputplus as pyip

def main():
    init()

    os.system('CLS')

    HEIGHT, WIDTH, N_ITER, N_SAMPLES, USE_SEED, SEED = utils.read_config()

    init_image_path = pyip.inputStr(f"\n{Fore.BLUE}Enter the PATH to your image:{Fore.WHITE}\nRight click on image, click 'Copy Path' and paste\n")
    try:
        utils.check_init_img_path(init_image_path)
    except Exception as e:
        print(f"\n{Fore.RED}Not a valid path, right click on the image and choose 'Copy Path' and paste the value into the console")
        return
    print(f'{Fore.GREEN}Set PATH to "{init_image_path}"')

    prompt = pyip.inputStr(f"\n{Fore.BLUE}Enter your PROMPT:{Fore.WHITE}\n")
    print(f'{Fore.GREEN}Set PROMPT to "{prompt}"')

    print(f'\n{Fore.BLUE}Specify how much the created images should resemble the original image:')
    strength = pyip.inputFloat('Enter a value between 0.0 (indistinguishable) and 0.9 (minor similarity):', min=0.0, max=0.9)
    print(f'{Fore.GREEN}Set STRENGTH to "{strength}"')

    print(f'\n{Fore.YELLOW}STARTING...\n{Fore.WHITE}')

    command = f'python optimizedSD/optimized_img2img.py --prompt "{prompt}" --init-img "{init_image_path}" --strength {strength} --n_samples {N_SAMPLES} --n_iter {N_ITER} --W {WIDTH} --H {HEIGHT}' 
    if(USE_SEED):
        command += f' --seed {SEED}'

    os.system(command)

if __name__ == "__main__":
    main()