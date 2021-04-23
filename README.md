# Python template
  * Click on [this link / Use This Template](https://github.com/aicore/Template-PythonProject/generate) button in the GitHub page above to  create a brand new python project with built in build and unit test system enabled.
  * **TODO**: Edit this file for each project you create.

## Building and testing
### Prerequisites
* Verify that Python-3 and pip3 should be installed in your system. terminal>`pip3 -V`
* Install pyb:  `pip3 install pybuilder`
* Verify Pyb  installation :`pyb --version`
```shell
# If pyb command is not found, you will have to add pyb to path.
# follow these instructions to add pyb to path.

# for ubuntu/bash:
> echo 'export PATH=$PATH:/<path/to/pyb/bin>' >> ~/.bashrc
# this is usually /home/<home folder>/.local/bin 
> source ~/.bashrc
```

### To build,clean and run tests, use the following command:
#### Build and test
```shell
pyb install_dependencies 
# Pyb should work without pyb install_dependencies, but unfortunately it doesnt.
# See details: here https://github.com/pybuilder/pybuilder/issues/727 
pyb -v
```
* That's all you need to build the project.
* Details about Test failures if any can be found in file `target\reports\unittest`
* The binary artifacts will be available in the target folder.
#### Clean builds :
* > pyb clean
  
#### Reset environment :
* > pyb clean && rm -rf .pybuilder

### working with the build system
* Tutorial: https://pybuilder.io/documentation/tutorial
* To make changes to build scripts see this: https://pythonhosted.org/pybuilder/walkthrough-new.html

## IDE/Editor setup
### [Pycharm/intellij](https://www.jetbrains.com/pycharm/) 
 Support is present in source. `.idea` files are avilable when you clone this repo. Just open the folder in pycharm.
### Vim
* Vim's config file is usually located in `~/.vimrc` . Locate the Vim rc file.
* create/Append the file with this [config file](https://github.com/aicore/Template-PythonProject/blob/main/ideconfig/vimrc).

## Project structure
* Use `src/main/python/<module>` to add your python module.
* Write unit tests in `src/unittest/` directory mirroring the same module structure in `src/main` directory.
* The build artifacts can be found in `target` directory.

## Adding dependencies
* Dependencies are managed through the build.py file.
* Refer https://pybuilder.io/documentation/plugins#installing-dependencies to see how this can be done.
* After updating dependencies, run the following command.
```shell
 pyb install_dependencies
```

## Writing tests
* Write unit tests in `src/unittest/` directory mirroring the same module structure in `src/main` directory.
* Use One of the two below supported testing suites.
  - Python unit test framework : https://docs.python.org/3/library/unittest.html
  - Mockito spying framewrk, see docs: https://mockito-python.readthedocs.io/en/latest/

Follow the above two links on details on how to write tests.

### Running tests with coverage
* `pyb -v` runs unit tests as part of every build
* Default coverage is set to 70%. To change the defaults, see https://pybuilder.io/documentation/plugins#measuring-unittest-coverage 

