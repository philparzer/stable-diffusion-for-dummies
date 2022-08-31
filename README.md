# Stable Diffusion for Dummies

## 0. Prerequisites

What you'll need:

- [x] Windows 10 or 11
- [x] decent NVIDIA graphics card (about 4 VRAM and more)

## 1. Downloads

Let's download some stuff.

### 1.1 CUDA

<a href="https://developer.nvidia.com/cuda-11-6-2-download-archive?target_os=Windows&target_arch=x86_64" rel="noopener noreferrer">Download and install CUDA drivers
</a>

### 1.2 Anaconda

<a href="https://www.anaconda.com/" rel="noopener noreferrer">Download and install Anaconda</a>

### 1.3 Visual Studio Code

<a href="https://code.visualstudio.com/Download" rel="noopener noreferrer">Download and install Visual Studio Code</a>

### 1.4 This Repo

- Download **this repo** as .zip
- unzip it in an appropriate location (preferably on a SSD)

TODO GIF

### 1.5 Stable Diffusion Weights

- <a href="https://huggingface.co/CompVis/stable-diffusion-v-1-4-original" rel="noopener noreferrer">Download the model weights from Huggingface</a> (you'll need to create an account)
- unzip the file
- move it into the folder you've downloaded before ```stable-diffusion-for-dummies/models/ldm/stable-diffusion-v1```
- rename the file to *model.ckpt*

TODO GIF

## 2. Setup

- use Windows Search to search for 'Anaconda' and open 'Anaconda Prompt'
- in Anaconda Prompt type the following:

``` command prompt
conda env create -f environment.yaml
conda activate ldm
```

- in Visual Studio Code, navigate to the folder ```stable-diffusion-for-dummies/```

TODO GIF

- this could take a while, go grab a cup of coffee ☕

## 3. Usage

We're all set, let's generate some images. We've implemented several different ways to use Stable Diffusion. But first let's talk about configuration.

### 3.1 Configuration

In the root folder ```stable-diffusion-for-dummies/``` you should see ```config.ini```. This file contains several fields you are free to update.

| config.ini fields | description |
| ------------- | ------------- |
| image_height = 512  | height of the generated image, in pixels  |
| image_width = 512  | width of the generated image, in pixels  |
| number_of_iterations = 1  |  number of times the generation process is going to run  |
| number_of_images_per_iteration* = 2  | how many images are generated each time the generation process runs |
| seed | TODO  |

*If your number_of_iterations (batch_size) is too big, you could run into problems. I'd suggest starting out small (at like < 5) and increasing it in small steps to find out how many images your graphics card can handle.

### 3.2 Using this repo

There is one important distinction other than user experience when it comes to the ways of using this repo described below:

- txt-2-img (text to image) -> generates an image based on a given prompt
- img-2-img (image to image) -> generates a new image based on a given image and a prompt

Before using any of the methods listed below, make sure to open a command prompt in Visual Studio Code and enter this command:

TODO GIF

``` command prompt
conda activate ldm
```

### 3.2 Start the graphic user interface

The most straight-forward, albeit not the fastest, way of using this repository for image generation is to enter the command below and pick one of three choices. This opens up a graphical user interface that you might feel more comfortable working with.

```command prompt
python start.py 
```

### 3.3 Start generating in the console

The following two commands have the same functionality as the previous command, the difference is that they don't use a graphical user interface.

```command prompt
python txt2img.py
```

```command prompt
python img2img.py 
```

The next two commands allow the program to go through a list of prompts that were set by you in a txt file beforehand.

TODO GIF

```command prompt
python txt2img_prompt_queue.py 
```

```command prompt
python img2img_prompt_queue.py 
```

## 4. Where to go from here

TODO
