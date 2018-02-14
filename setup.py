"""OpenPixelControl setup module
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

setup(
    name='pyopc',
    version='1.0.0',
    description='A python OpenPixel client',
    url='https://github.com/kj4ips/pyopc',
    author='Aaron Haun, based on work by zestyping',
    author_email='aaron@haun.guru',
    classifiers=[  
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 2',
    ],
    keywords='opc openpixel ledmatrix',
    packages=find_packages()
)
