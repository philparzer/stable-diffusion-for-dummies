import os
import utils
from colorama import init

init()

HEIGHT, WIDTH, N_ITER, N_SAMPLES, SEED = utils.read_config()

with open("prompt_list.txt",'r') as f:
    lines = f.read().splitlines() 

for prompt in lines:
    os.system(f'python optimizedSD/optimized_txt2img.py --prompt "{prompt}" --n_samples {N_SAMPLES} --n_iter {N_ITER} --W {WIDTH} --H {HEIGHT} --seed {SEED}')