from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name="mediar",
    description="MEDIAR: Harmony of Data-Centric and Model-Centric for Multi-Modality Microscopy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mrjholt/MEDIAR/tree/mediar-bluemorpho", # Replace with actual URL
    packages=find_packages(include=['core', 'image', 'train_tools', 'core.*', 'image.*', 'train_tools.*']),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License", # Assuming MIT based on LICENSE file
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9', # Based on README
) 