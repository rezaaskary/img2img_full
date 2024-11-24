from setuptools import setup, find_packages
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='image2image_translation',
    version='0.1',
    packages=find_packages(),
    install_requires=required,
    entry_points={
        'console_scripts': [
            'my_script = my_module.module1:main_function',
        ],
    },
    author='Mohammad Reza Askari',
    author_email='reza.askary99@gmail.com',
    description='Implementation of CycleGAN & Pix2Pix',
    long_description=open('./README.md').read(),
)
