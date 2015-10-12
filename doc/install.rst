

# install python 3.5 then create a virtualenv
python3.5 -m venv env
source env/bin/activate

# make sure you have the last version of setuptools
pip install setuptools --upgade

# install crossbar
pip install crossbar

# install dependancies
pip install -r requirements.txt
