MOOC software testing by TUDelft in Python with pytest
==============================

Implementation of the course in Python

# Instructions
The $ sign indicated operation from the terminal as a non-root user.

## Software requirements
1. Lunix style terminal, either Linux native OS, Git bash, or [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install)
2. Python >= 3.8

## Installation
1. Clone the repo:  
`$ git clone your-repo`

2. Set-up a virtual environment to isolate the project:
`$ python3 -m venv ~/.path-to-your-repo`  
`$ source ~/.path-to-your-repo/bin/activate`

3. install requirements
$ make requirements

**NOTE:** If new packages are added during development, add them with a pinned version to _requirements.in_.  
For example:  
numpy==1.22.2

4. Lint you code to adhere to style guides.
`$ make lint`

5. Clean formatting
`$ make format`

## Security checks, unit tests and license checks during development
### Security checks
To perform a static security lint step run in the terminal:
`$ bandit -r src tests -n 3 --severity-level high --confidence-level medium`

To perform a dynamic scan of the package container, first install [trivy v0.28.0](https://aquasecurity.github.io/trivy/v0.28.0/) from a bash terminal:  
`$ sudo apt install -y rpm`  
`$ wget https://github.com/aquasecurity/trivy/releases/download/v0.28.0/trivy_0.28.0_Linux-64bit.deb`  
`$ sudo dpkg -i trivy_0.28.0_Linux-64bit.deb`  
`$ trivy -v`  

Next run a scan of an image from a repository, for example:
`$ trivy image path-to-your-image`

### Unit Tests
To run pytest from the project root, run in the terminal:  
`$ pytest tests -v`

To run a specific test:  
`$ pytest tests/test.py::test_name -v`

To run a set of tests identified by a marker:  
`$ pytest tests/test.py -m -v marker`

To generate coverage report when running pytest from the terminal you need to run `pytest` with `coverage`:  
`$ coverage run -m pytest /tests/test.py --cov=src/ --cov-report=xml` 

In addition you can install [Coverage Gutters](https://marketplace.visualstudio.com/items?itemName=ryanluker.vscode-coverage-gutters). This will reveal uncovered lines in your source code after the test has been run.  


### Software license check
`$ pip-licenses --format=markdown --with-urls  --output-file=./licenses.md`


--------


<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
