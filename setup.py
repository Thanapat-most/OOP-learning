﻿import io
from os.path import abspath, dirname, join
from setuptools import find_packages, setup


HERE = dirname(abspath(__file__))
LOAD_TEXT = lambda name: io.open(join(HERE, name), encoding='UTF-8').read()
DESCRIPTION = '\n\n'.join(LOAD_TEXT(_) for _ in [
    'README.rst'
])

setup(
  name = 'mostoop',      
  packages = ['mostoop'], 
  version = '0.0.3',  
  license='MIT', 
  description = 'OOP Learning by Most',
  long_description=DESCRIPTION,
  author = 'Thanapat-most',                 
  author_email = 'thanapat.most2543@gmail.com',     
  url = 'https://github.com/Thanapat-most/OOP-learning',  
  download_url = 'https://github.com/Thanapat-most/OOP-learning/archive/v0.0.3.zip',  
  keywords = ['OOP', 'most', 'learning'],   
  classifiers=[
    'Development Status :: 3 - Alpha',     
    'Intended Audience :: Education',     
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)