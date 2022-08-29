import os
import sys
import utils
import pyinputplus as pyip
from colorama import init, Fore

def main():
    init()

    HEIGHT, WIDTH, N_ITER, N_SAMPLES = utils.read_config()

    if(len(sys.argv[1:]) != 2):
        print(f'{Fore.YELLOW}Make sure that your prompt and path are enclosed in quotation marks.\n{Fore.RED}Usage:{Fore.WHITE} python img2img.py {Fore.RED}"{Fore.WHITE}path/to/your/image.png|jpg{Fore.RED}"{Fore.WHITE} {Fore.RED}"{Fore.WHITE}your image prompt{Fore.RED}"')
        return
    init_image_path, prompt  = sys.argv[1:]

    try:
        utils.check_init_img_path(init_image_path)
    except Exception as e:
        print(e)
        return

    print('Specify how much the created images should resemble the original image:')
    strength = pyip.inputFloat('Enter a value between 0.0 (indistinguishable) and 0.9 (minor similarity):', min=0.0, max=0.9)

    os.system(f'python optimizedSD/optimized_img2img.py --prompt "{prompt}" --init-img "{init_image_path}" --strength {strength} --n_samples {N_SAMPLES} --n_iter {N_ITER} --W {WIDTH} --H {HEIGHT}')

if __name__ == "__main__":
    main()