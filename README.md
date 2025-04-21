# StyleGAN2 Face Generation

This project uses StyleGAN2-ADA to generate realistic face images. It includes a trained model and a script to generate new faces.

## Setup

1. Clone this repository:
```bash
git clone https://github.com/JackDSnyder/stylegan2-face-generation.git
cd stylegan2-face-generation
```

2. Download the trained model:
   - Download `network-final.pkl` from [Google Drive](https://drive.google.com/file/d/1wAvHUcJqC7XQVMyISsYqNOjbs91NTZF0/view?usp=sharing)
   - Place it in the root directory of the project

3. Install required dependencies:
```bash
pip install torch torchvision
```

## Usage

To generate images, run:
```bash
python generate.py
```

This will generate 10 images by default. You can modify the script to change:
- Number of images to generate
- Starting seed number
- Truncation value (controls image quality/variation)

## Model

The trained model (`network-final.pkl`) is stored separately due to its large size (333MB). You can download it from the Google Drive link above.

## Requirements

- Python 3.6+
- PyTorch with CUDA support (for GPU acceleration) 