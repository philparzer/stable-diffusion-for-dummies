# Stable Diffusion for Dummies

Who this repo is for:

<details open>
<summary>Newbies</summary>
<p>We created this repo to simplify the setup and installation process as well as user experience for newcomers. We try to break down barriers of entry and make it possible for creative people of all backgrounds to be able to use state-of-the-art image generation models.</p>

</details>

<details closed>
<summary>Stakeholders</summary>
This repo is primarily focused on simplifying the setup process and UX. In addition to that, there are some unique features sprinkled in 🧂</br></br>
List of features and changes compared to <a href="https://github.com/basujindal/stable-diffusion" rel="noopener noreferrer">Basujindal's Optimized Stable Diffusion</a>:

- easier to use CLI
- <a href="#animation.py">animation.py</a>
- readme for non-technical people

</details>
</br>
<p>If anything below doesn't work, hit me up <a href="https://twitter.com/philipp_parzer" rel="noopener noreferrer">on Twitter (my DMs are open)</a> 🤗</p>

<p>If everything does work, consider <a href="https://ko-fi.com/philparzer" rel="noopener noreferrer">buying me a coffee</a> ☕</p>

## 0. Prerequisites 🎒

What you'll need:

- [x] Windows 10 or 11
- [x] decent NVIDIA graphics card (about 4 VRAM and more)

On an Apple Silicon Mac?
Check out <a href="https://twitter.com/levelsio/status/1565731907664478209" rel="noopener noreferrer">this guide</a>

## 1. Downloads ⬇️

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

## 2. Setup 🛠️

- use Windows Search to search for 'Anaconda' and open 'Anaconda Prompt'
- in Anaconda Prompt type the following:

``` command prompt
conda env create -f environment.yaml
conda activate ldm
```

- in Visual Studio Code, navigate to the folder ```stable-diffusion-for-dummies/```

TODO GIF

- this could take a while, go grab a cup of coffee ☕

## 3. Usage 🖼️

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

> *If your number_of_iterations (batch_size) is too big, you could run into problems. I'd suggest starting out small (at like < 5) and increasing it in small steps to find out how many images your graphics card can handle.

### 3.2 Usage Basics

There is one important distinction other than user experience when it comes to the ways of using this repo described below:

- txt-2-img (text to image) -> generates an image based on a given prompt
- img-2-img (image to image) -> generates a new image based on a given image and a prompt
- animation -> generates a number of frames based on a given image and prompt

Before using any of the methods listed below, make sure to open Visual Studio Code with Anaconda:

TODO GIF

Then, open a command prompt in Visual Studio Code and enter this command:

``` command prompt
conda activate ldm
```

TODO GIF

### 3.2 Use the graphical user interface (GUI)

The most straight-forward, albeit not the fastest, way of using this repository for image generation is to enter the command below and pick one of two choices. This opens up a graphical user interface that you might feel more comfortable working with starting out.

```command prompt
python gui.py 
```

TODO GIF

Find all generated images in the folder ```/outputs/txt2img-samples/<your-prompt>```.
Or ```/outputs/img2img-samples/<your-prompt>``` if you chose img2img.

### 3.3 Use the console

We recommended using the CLI (Command Line Interface) as soon as you feel more comfortable.
There are several commands to use that all serve a different purpose. Enter one of the commands below and the CLI will guide you through the whole process, just make sure to read the console output.

The first two commands are fairly straightforward and handle txt2img and img2img generation.

```command prompt
python txt2img.py
```

```command prompt
python img2img.py 
```

Find all generated images in the folder ```/outputs/txt2img-samples/<your-prompt>```.
Or ```/outputs/img2img-samples/<your-prompt>``` if you chose img2img.

---

The next two commands allow the program to go through a list of prompts that were set by you in ```prompt_list.txt``` beforehand.

TODO GIF

```command prompt
python txt2img_prompt_queue.py 
```

```command prompt
python img2img_prompt_queue.py 
```

Find all generated images in the folder ```/outputs/txt2img-samples/<your-prompt>```.
Or ```/outputs/img2img-samples/<your-prompt>``` if you chose img2img.

---

<p id ="animation.py">The last command is a special addition that allows you to generate an animation based on a given image and prompt.</p>

```command prompt
python animation.py 
```

TODO GIF

Find all generated frames in the folder ```/outputs/animation-samples/<your-prompt>```.
We recommend using <a href="https://ezgif.com/maker" rel="noopener noreferrer">EZGIF</a> to generate the animation. Just upload all frames, hit generate and edit the animation to your liking.

TODO GIF

## 4. Where to go from here 🛣️

- Suggest some features <a href="https://twitter.com/philipp_parzer" rel="noopener noreferrer">on Twitter (my DMs are open)</a> 💡
- Contribute to Stable Diffusion for Dummies 🤗
- Get some inspiration over at <a href="https://lexica.art/" rel="noopener noreferrer">Lexica.art</a>
- Download and use a <a href="https://huggingface.co/CompVis/stable-diffusion-v-1-4-original" rel="noopener noreferrer">  different checkpoint of the model </a>

## 5. Planned features 🚧

- ```animation.py```
    - convert frames to animated format
    - implement zoom-zones
    - implement color filters
    - implement strength change over frame count
- ```gui.py```
    - implement animation support
    - implement inpainting
- ...
