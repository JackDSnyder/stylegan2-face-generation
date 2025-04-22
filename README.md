# StyleGAN2 Face Generation

This project uses StyleGAN2-ADA to generate realistic face images. It's a simplified interface for generating images using a pre-trained model.

## Setup

1. Clone this repository:
```bash
git clone https://github.com/JackDSnyder/stylegan2-face-generation.git
cd stylegan2-face-generation
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Make sure you have a trained model file (e.g., `network-final.pkl`) in the project directory.

2. Run the generation script:
```bash
python3 generate.py
```

This will:
- Generate 10 images by default
- Save them in the `generated_images` directory
- Use seeds 0-9 by default
- Use a truncation value of 0.7 for balanced quality/diversity

### Customization

You can modify the following parameters in `generate.py`:
- `num_images`: Number of images to generate
- `start_seed`: Starting seed number
- `truncation`: Controls variation vs. quality (lower = more average/higher quality)
- `output_dir`: Where to save generated images

## Model

The trained model (`network-final.pkl`) is stored separately due to its large size (333MB). You can download it from the Google Drive link above.

## Requirements

- Python 3.6+
- PyTorch with CUDA support (for GPU acceleration) 