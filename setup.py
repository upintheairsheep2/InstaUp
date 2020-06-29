from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='instaup',
    version='2020.06.29',
    description='An auto downloader and uploader for Instagram profiles.',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://github.com/Coloradohusky/InstaUp',
    author='Coloradohusky',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'instaup = instaup.instaup:main',
        ],
    },
    python_requires='>=3.5, <4',
    install_requires=['internetarchive>=1.9.3', 'instaloader>=4.4.3']
)
