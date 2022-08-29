import configparser
import os
from PIL import Image
from colorama import Fore

def read_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
        
    try:
        HEIGHT = config['SETTINGS'].getint('image_height')
        WIDTH = config['SETTINGS'].getint('image_width')
        N_ITER = config['SETTINGS'].getint('number_of_iterations')
        N_SAMPLES = config['SETTINGS'].getint('number_of_images_per_iteration')
        SEED = config['SETTINGS'].getint('seed')
    except:
        print(Fore.YELLOW +'Your configuration file seems to be invalid.'+ Fore.WHITE)
        exit()

    return HEIGHT, WIDTH, N_ITER, N_SAMPLES, SEED

def check_init_img_path(path):
    if(os.path.isfile(path)):
        try:
            Image.open(path)
            return path
        except:
            raise Exception(Fore.YELLOW +'Incompatible file format.'+ Fore.WHITE)
    raise Exception(Fore.YELLOW +'The specified file does not exist.'+ Fore.WHITE)
    
