
from setuptools import setup, find_packages

setup(
    name='mameebox',
    version=0.1,
    packages=find_packages(),
    author="Mameebox",
    author_email="mameebox@gmail.com",
    description="IoT thermal printer",
    long_description=open('README.rst').read(),
    install_requires=['crossbar', 'path.py'] ,
    include_package_data=True,
    url='http://github.com/mameebox/mameebox',

    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3.5",
        "Topic :: Printing",
    ]
)