# Python template
  Click on the *Use This Template* button in the GitHub page above to  create a brand new python project with built in build and unit test system enabled.

## Building and testing
### Prerequisites
* Verify that Python-3 and pip3 should be installed in your system. terminal>`pip3 -V`
* Install pyb:  `pip3 install pybuilder`
* Verify Pyb  installation :`pyb --version`

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

## IDE setup
* [Pycharm/intellij](https://www.jetbrains.com/pycharm/) support is present in source. `.idea` files are avilable when you clone this repo. Just open the folder in pycharm.