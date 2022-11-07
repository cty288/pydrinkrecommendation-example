# pydrinkrecommendation Example
This project is an example program showing how to use the APIs of `pydrinkrecommendation` module. Please follow the instructions below to run the project successfully

## Setting up the virtual environment
 
1. Create a `pipenv`-managed virtual environment and install the latest version of your package installed: 
   ```
   python3 -m pipenv install -i https://test.pypi.org/simple/pydrinkmanagment
   ``` 
   (Note that if you've previously created a `pipenv` virtual environment in the same directory, you may have to delete the old one first. Find out where it is located with the `pipenv --venv` command.)
2. Activate the virtual environment and enter the virtual environment's shell:
   ```
   python -m pipenv shell
   ```
3. Find out where your virtual environment is located:
   ```
    python3 -m pipenv --venv
   ``` 
4.  Download this project to your virtual environment
5.  Inside your `pipenv` shell, run the following command to run this project:
    ```
    python3 -m pipenv run python src/__main__.py
    ```