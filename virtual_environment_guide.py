'''
-- creates a clone of python interpreter and creates a new environment where we can code
-- sometimes when we code we may use a module of some version say tkinter module version 1.0,.. later, that module's creator decides
    to update it to version 1.1, in which they decide to remove a function which was used in your code. now when you run your code,
    python wont be able to find that function and would throw an error. To avoid this we can create a virtual environment and code in
    it. Now even if the module's creator decides to delete some of the functionality, it wont affect our code. as it will be using the
    older version of module and not the latest version

-- to create a virtual enviroment:
1) go to your project folder
2) create a powershell window there
3) pip install virtualenv
4) virtualenv <environment name>
5) .\<env name>\Scripts\activate ---------> activates the virtual environment
# if step 5 gives error: open powershell in admin mode, and write: set-executionpolicy remotesigned, and then write y and press enter.
-- just write "deactivate" to exit the virtual env.
-- while working with a virtual env, you need to reinstall modules with help of pip.
-To create a virtual environment containing all the modules installed in the original base python interpreter, write:
virtualenv --system-site-packages <env name>
'''

'''
requirements.txt file:
-- contains all the module names and versions used in the virtual environment
pip freeze > requirements.txt
-- if you are given a requirement.txt file, and want to install all modules mentioned in it, write:
pip install -r requirements.txt
'''
