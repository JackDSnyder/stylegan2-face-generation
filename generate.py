# CELL: Edit generate.py
import os
import sys
import subprocess
import torch


# setup
def setup_stylegan():
    # Clone repository if it doesn't exist
    if not os.path.exists("stylegan2-ada-pytorch"):
        subprocess.run(
            ["git", "clone", "https://github.com/NVlabs/stylegan2-ada-pytorch.git"]
        )


def generate_images(
    network_path,
    num_images=10,
    start_seed=10,
    truncation=0.7,
    output_dir="generated_images",
):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Generate a range of seeds
    seeds = range(start_seed, start_seed + num_images)

    # Use subprocess to run the StyleGAN2 generate script
    cmd = [
        "python",
        os.path.join("stylegan2-ada-pytorch", "generate.py"),
        f"--outdir={output_dir}",
        f"--trunc={truncation}",
        f"--seeds={','.join(map(str, seeds))}",
        f"--network={network_path}",
    ]

    print(
        f"Generating {num_images} images with seeds {start_seed} to {start_seed + num_images - 1}..."
    )
    subprocess.run(cmd)


if __name__ == "__main__":
    # Setup StyleGAN2
    setup_stylegan()

    # Set your parameters here
    network_path = "network-final.pkl"  # Path to your trained model
    num_images = 10  # Number of images to generate
    start_seed = 0  # Starting seed number
    truncation = (
        0.7  # Controls variation vs. quality (lower = more average/higher quality)
    )
    output_dir = "generated_images"  # Where to save generated images

    # Generate multiple images
    generate_images(network_path, num_images, start_seed, truncation, output_dir)
    print(f"Generated {num_images} images saved in {output_dir}")
