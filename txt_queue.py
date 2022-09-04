import os
import utils
from colorama import init, Fore

def main():

    init()

    os.system('CLS')

    HEIGHT, WIDTH, N_ITER, N_SAMPLES, USE_SEED, SEED = utils.read_config()
    print(f'\n{Fore.YELLOW}STARTING...\n{Fore.WHITE}')
    command = f'python optimizedSD/optimized_txt2img.py --from-file prompt_list.txt --n_samples {N_SAMPLES} --n_iter {N_ITER} --W {WIDTH} --H {HEIGHT}'
    if(USE_SEED):
        command += f' --seed {SEED}'

    os.system(command)

if __name__ == "__main__":
    main()