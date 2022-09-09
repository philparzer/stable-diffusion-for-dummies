# Stable Diffusion for Dummies

**Who this repo is for:**

<details open>
<summary><b>Newbies 👶</b></summary>
<p>We maintain this repo to simplify the setup and installation process as well as user experience for newcomers. We try to break down barriers of entry and make it possible for creative people of all backgrounds to be able to use state-of-the-art image generation models.</p>

</details>

<details closed>
<summary><b>Stakeholders 👩‍💻</b></summary>
This repo is primarily focused on simplifying the setup process and UX. In addition to that, there are some unique features sprinkled in 🧂</br></br>
List of features and changes compared to <a target="_blank" href="https://github.com/basujindal/stable-diffusion" rel="noopener noreferrer">Basujindal's Optimized Stable Diffusion</a>:

- easier to use CLI
- <a href="#animation.py">animation.py</a>
- readme for non-technical people

</details>

---

<p>If anything below doesn't work, hit me up <a target="_blank" href="https://twitter.com/philipp_parzer" rel="noopener noreferrer">on Twitter (my DMs are open)</a> 🤗</p>

<p>If everything does work, consider <a target="_blank" href="https://ko-fi.com/philparzer" rel="noopener noreferrer">buying me a coffee</a> ☕</p>

---

# 0. Prerequisites 🎒

What you'll need:

- [x] Windows 10 or 11
- [x] decent NVIDIA graphics card (about 4 VRAM and more)
- [x] ~15gb of disk space (preferably on an SSD)

> On an Apple Silicon (M1, M2) Mac?
Check out <a target="_blank" href="https://twitter.com/levelsio/status/1565731907664478209" rel="noopener noreferrer">this guide</a>

# 1. Downloads ⬇️

Let's download some stuff.

### 1.1 Visual Studio

<a target="_blank" href="https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Community&channel=Release&version=VS2022&source=VSLandingPage&cid=2030&passive=false" rel="noopener noreferrer">Download and install Visual Studio with "Desktop Development with C++" workload
</a>

<img src="https://raw.githubusercontent.com/philparzer/stable-diffusion-for-dummies-assets/master/gifs/install-vs.gif"></img>

### 1.2 CUDA

<a target="_blank" href="https://developer.nvidia.com/cuda-11-6-2-download-archive?target_os=Windows&target_arch=x86_64" rel="noopener noreferrer">Download and install CUDA drivers
</a>

---
### ⚠ Restart your PC after CUDA has been installed
---

### 1.3 Anaconda

<a target="_blank" href="https://www.anaconda.com/" rel="noopener noreferrer">Download and install Anaconda</a>

### 1.4 Visual Studio Code

<a target="_blank" href="https://code.visualstudio.com/Download" rel="noopener noreferrer">Download and install Visual Studio Code</a>

### 1.5 This Repository

- Download **this repo** as .zip
- unzip it in an appropriate location (preferably on an SSD)

<img src="https://raw.githubusercontent.com/philparzer/stable-diffusion-for-dummies-assets/master/gifs/download-repo.gif"></img>

### 1.6 Stable Diffusion Weights

- <a target="_blank" href="https://huggingface.co/CompVis/stable-diffusion-v-1-4-original" rel="noopener noreferrer">Download the model weights from Huggingface</a> (you'll need to create an account first)

<img src="https://raw.githubusercontent.com/philparzer/stable-diffusion-for-dummies-assets/master/gifs/download-weights.gif"></img>

- move it into the folder you've downloaded before ```stable-diffusion-for-dummies-main/models/ldm/stable-diffusion-v1```
- rename the file to *model.ckpt*

# 2. Setup 🛠️

- use Windows Search to search for 'Anaconda' and open 'Anaconda Prompt'
- in Anaconda Prompt enter the following 

``` command prompt
code
```
<img src="https://raw.githubusercontent.com/philparzer/stable-diffusion-for-dummies-assets/master/gifs/open-anaconda.gif"></img>

- in the newly opened Visual Studio Code Window navigate to the folder ```stable-diffusion-for-dummies-main/```

<img src="https://raw.githubusercontent.com/philparzer/stable-diffusion-for-dummies-assets/master/gifs/open-folder.gif"></img>

- in Visual Studio Code, open a command prompt and enter the following command, this could take a while, go grab a cup of coffee ☕:
```command prompt
conda env create -f environment.yaml
```

<img src="https://raw.githubusercontent.com/philparzer/stable-diffusion-for-dummies-assets/master/gifs/activate-env.gif"></img>


- enter the following command in your command prompt:

``` command prompt
pip install gradio
```

- woah you've made it all the way through, good job 👏 

# 3. Usage 🖼️

We're all set, let's generate some images. 

## 3.1 Usage Basics

There is one important distinction other than user experience when it comes to the ways of using this repo described below:

- txt2img (text to image) -> generates an image based on a given prompt
- img2img (image to image) -> generates a new image based on a given image and a prompt
- animation -> generates a number of frames based on a given image and prompt

We've implemented several different ways to use Stable Diffusion.
Before using any of the methods listed below, make sure to open Visual Studio Code with Anaconda. 
In Visual Studio Code open a command prompt and enter this command:

``` command prompt
conda activate ldm
```

<img src="https://raw.githubusercontent.com/philparzer/stable-diffusion-for-dummies-assets/master/gifs/before-use.gif"></img>

Then, enter any of the commands described below into this command prompt.

## 3.2 Use the graphical user interface (GUI)

The most straight-forward, albeit not the fastest, way of using this repository for image generation is to enter the command below and pick one of two choices. This opens up a graphical user interface that you might feel more comfortable working with.

```command prompt
python gui.py 
```

<img src="https://raw.githubusercontent.com/philparzer/stable-diffusion-for-dummies-assets/master/gifs/start-gui.gif"></img>
<img src="https://raw.githubusercontent.com/philparzer/stable-diffusion-for-dummies-assets/master/gifs/use-gui.gif"></img>

Find all generated images in the folder ```/outputs/txt2img-samples/<your-prompt>```.
Or ```/outputs/img2img-samples/<your-prompt>``` if you chose img2img.

## 3.3 Configure the Console

We recommend using the CLI (Command Line Interface) as soon as you feel more comfortable.
There are several commands to use that all serve a different purpose.

But first, let's talk about configuration. We've implemented a config file where you can set specific values and save them, so that you don't need to input them every time you want to generate an image.

In the root folder ```stable-diffusion-for-dummies/``` you should see ```config.ini```. This file contains several fields you are free to update.

<img src="https://raw.githubusercontent.com/philparzer/stable-diffusion-for-dummies-assets/master/gifs/configure.gif"></img>

>💡 notice the white circle right next to the file name ```config.ini```? the circle indicates that your changes are not saved, save the file by hitting CTRL+S

| config.ini fields | description |
| ------------- | ------------- |
| image_height = 512  | height of the generated image, in pixels  |
| image_width = 512  | width of the generated image, in pixels  |
| number_of_iterations = 1  |  number of times the generation process is going to run  |
| number_of_images_per_iteration* = 2  | how many images are generated each time the generation process runs |
| use_seed | set this to 'True' if you want to use a preconfigured seed or 'False' if you don't  |
| seed | unique identifier of your image (share seed and prompt to enable other people to generate the same image as you)  |

>💡 *If your number_of_iterations (batch_size) is too big, you could run into problems. I'd suggest starting out small (at like < 5) and increasing it in small steps to find out how many images your graphics card can handle.

## 3.3 Use the Console

Enter one of the commands below and the CLI will guide you through the whole process, just make sure to read the console output.
>💡 if you ever want to stop a running process in the console, click on the console and hit CTRL+C

### 3.3.1 Simple txt2img + img2img

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

### 3.3.2 Queue a list of prompts and generate

The next two commands allow the program to go through a list of prompts that were set by you in ```prompt_list.txt``` beforehand.

<img src="https://raw.githubusercontent.com/philparzer/stable-diffusion-for-dummies-assets/master/gifs/edit-prompt-list.gif"></img>

Don't forget to hit CTRL + S to save ```prompt_list.txt``` after you're finished editing.

```command prompt
python txt_queue.py 
```

```command prompt
python img_queue.py 
```

Find all generated images in the folder ```/outputs/txt2img-samples/<your-prompt>```.
Or ```/outputs/img2img-samples/<your-prompt>``` if you chose img2img.

---

### 3.3.2 Generate an animation

<p id ="animation.py">The last command is a special addition that allows you to generate an animation based on a given image and prompt.</p>

```command prompt
python animation.py 
```

<img src="https://raw.githubusercontent.com/philparzer/stable-diffusion-for-dummies-assets/master/gifs/start-animation.gif"></img>

Find all generated frames in the folder ```/outputs/animation-samples/<your-prompt>```.

We recommend using <a target="_blank" href="https://ezgif.com/maker" rel="noopener noreferrer">EZGIF</a> to generate the animation. Just upload all frames, hit generate and edit the animation to your liking.

<img src="https://raw.githubusercontent.com/philparzer/stable-diffusion-for-dummies-assets/master/gifs/example-animation.gif"></img>
> cat litter box full of snails, cat sitting in litter box, painting in style of Salvador Dali

# 4. Where to go from here 🛣️

- Suggest some features <a target="_blank" href="https://twitter.com/philipp_parzer" rel="noopener noreferrer">on Twitter (my DMs are open)</a> 💡
- Contribute to Stable Diffusion for Dummies 🤗
- Get some inspiration over at <a target="_blank" href="https://lexica.art/" rel="noopener noreferrer">Lexica.art</a>
- Download and use a <a target="_blank" href="https://huggingface.co/CompVis/stable-diffusion-v-1-4-original" rel="noopener noreferrer">  different checkpoint of the model </a>

# 5. Planned features 🚧

- ```animation.py```
    - convert frames to animated format
    - implement zoom-zones
    - implement color filters
    - implement strength change over frame count
- ```gui.py```
    - implement animation support
    - implement inpainting
- ...

# 6. Issues ❗

- animation.py -> red/violet hue after frame 60 -> needs more testing
