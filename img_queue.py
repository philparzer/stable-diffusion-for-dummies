import os
import utils
import pyinputplus as pyip
from colorama import init, Fore

init()

HEIGHT, WIDTH, N_ITER, N_SAMPLES, USE_SEED, SEED = utils.read_config()

os.system('CLS')
print(f'{Fore.YELLOW}Read up on the documentation at https://github.com/philparzer/stable-diffusion-for-dummies#readme if you have any troubles\n{Fore.WHITE}')

init_image_path = pyip.inputCustom(utils.check_init_img_path, 'Specify the path to the source image: ')

print('Specify how much the created images should resemble the original image:')
strength = pyip.inputFloat('Enter a value between 0.0 (indistinguishable) and 0.9 (minor similarity):', min=0.0, max=0.9) # 1 throws
print(f'\n{Fore.YELLOW}STARTING...\n{Fore.WHITE}')
command = f'python optimizedSD/optimized_img2img.py --from-file prompt_list.txt --init-img "{init_image_path}" --strength {strength} --n_samples {N_SAMPLES} --n_iter {N_ITER} --W {WIDTH} --H {HEIGHT}'

if(USE_SEED):
    command += f' --seed {SEED}'

os.system(command)