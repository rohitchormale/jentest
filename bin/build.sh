#!/bin/bash
PYENV_HOME=$WORKSPACE/.jentest/
if [ -d $PYENV_HOME ]; then
  rm -rf $PYENV_HOME
fi

virtualenv --no-site-packages $PYENV_HOME
. $PYENV_HOME/bin/activate
pip install -r requirements.txt
python setup.py develop
nosetests --with-xunit jentest
