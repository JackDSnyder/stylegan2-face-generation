# StyleGAN2 Face Generation

This project uses StyleGAN2-ADA to generate realistic face images. It includes a trained model and a script to generate new faces.

## Setup

1. Clone this repository:
```bash
git clone https://github.com/JackDSnyder/stylegan2-face-generation.git
cd stylegan2-face-generation
```

2. Install Git LFS:
```bash
git lfs install
```

3. Pull the model file:
```bash
git lfs pull
```

4. Install required dependencies:
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

The trained model (`network-final.pkl`) is stored using Git LFS due to its large size (333MB).

## Requirements

- Python 3.6+
- PyTorch with CUDA support (for GPU acceleration)
- Git LFS (for handling large model files) 