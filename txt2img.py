import os
import sys
import utils
from colorama import init, Fore

def main():
    init()

    HEIGHT, WIDTH, N_ITER, N_SAMPLES = utils.read_config()

    if(len(sys.argv[1:]) != 1):
        print(f'{Fore.YELLOW}Make sure that your prompt is enclosed in quotation marks.\n{Fore.RED}Usage:{Fore.WHITE} python txt2img.py {Fore.RED}"{Fore.WHITE}your image prompt{Fore.RED}"')
        return
    prompt = sys.argv[1]

    os.system(f'python optimizedSD/optimized_txt2img.py --prompt "{prompt}" --n_samples {N_SAMPLES} --n_iter {N_ITER} --W {WIDTH} --H {HEIGHT}')

if __name__ == "__main__":
    main()