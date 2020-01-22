# Steps to run the code:

1. Clone git repo:

    `git clone git@github.com:alexandru-m-g/pycharm-2019.3-bug-test.git`
    
    `cd pycharm-2019.3-bug-test/`

1. Create new virtual env for python 2.7 (assuming virtualenv is installed)

    `virtualenv-2.7 venv`
    
    `source venv/bin/activate`
    
1. Activate namespace package:

    `python setup.py develop`

    `cd src1/`
    
    `python setup.py develop`
    
    `cd ../src2/`
    
    `python setup.py develop`
    
1. Go back to the root of the project. Run the code:

    `cd ..`
    
    `python p/main.py`
    
    Should print: "_func f2: from main function_"
 
    
