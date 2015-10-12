

# install python 3.5 then create a virtualenv
python3.5 -m venv env
source env/bin/activate

# make sure you have the last version of setuptools
pip install setuptools --upgade

# install crossbar
pip install crossbar

# install dependancies
pip install -r requirements.txt

# clone the repo
git clone https://github.com/mameebox/mameebox.git

# install the mameebox package
python setup.py install