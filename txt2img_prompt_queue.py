import os
import utils
from colorama import init

def main():

    init()

    HEIGHT, WIDTH, N_ITER, N_SAMPLES, SEED = utils.read_config()

    os.system(f'python optimizedSD/optimized_txt2img.py --from-file prompt_list.txt --n_samples {N_SAMPLES} --n_iter {N_ITER} --W {WIDTH} --H {HEIGHT} --seed {SEED}')

if __name__ == "__main__":
    main()