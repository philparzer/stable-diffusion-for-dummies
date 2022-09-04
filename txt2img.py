import os
import sys
import utils
from colorama import init, Fore
import pyinputplus as pyip

def main():
    init()

    os.system('CLS')
    print(f'{Fore.YELLOW}Read up on the documentation at https://github.com/philparzer/stable-diffusion-for-dummies#readme if you have any troubles\n{Fore.WHITE}')

    HEIGHT, WIDTH, N_ITER, N_SAMPLES, USE_SEED, SEED = utils.read_config()

    prompt = pyip.inputStr(f"\n{Fore.BLUE}Enter your PROMPT:{Fore.WHITE}\n")
    print(f'{Fore.GREEN}Set PROMPT to "{prompt}"')

    print(f'\n{Fore.YELLOW}STARTING...\n{Fore.WHITE}')

    command = f'python optimizedSD/optimized_txt2img.py --prompt "{prompt}" --n_samples {N_SAMPLES} --n_iter {N_ITER} --W {WIDTH} --H {HEIGHT}'

    if(USE_SEED):
        command += f' --seed {SEED}'

    os.system(command)
    
if __name__ == "__main__":
    main()