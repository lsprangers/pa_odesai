# Cup a Code: 
#### PyPi Package *testing only

## Using this package:
* Created to show necessary structure for creating a PyPi package
* Side try - create easy to use tool for personal analytics for normal people

### _Creating a virtual environment_
    > Currently, there are three common tools for creating
        Conda (Anaconda) - suggested

        > docs: https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html

        Python virtual environments:

        > venv is available by default in Python 3.3 and later, and 
            installs pip and setuptools into created virtual 
            environments in Python 3.4 and later.
    
        > virtualenv needs to be installed separately, but supports 
            Python 2.7+ and Python 3.3+, and pip, setuptools and wheel 
            are always installed into created virtual 
            environments by default (regardless of Python version).
    
    > The basic usage is like so:
    
        > venv:
    
            python3 -m venv <DIR>
            source <DIR>/bin/activate
    
        > virtualenv:
    
            virtualenv <DIR>
            source <DIR>/bin/activate

# ONLY AFTER CREATING A VIRTUAL ENV

**Why? Base compute without a venv allows imports/other things to spread across computer without being contained under a specified location**

### _Installing required packages_
    > Install a list of requirements specified in a Requirements File.

        python -m pip install -r requirements.txt

    
    > Installing from VCS
        Install a project from VCS in “editable” mode.
        For a full breakdown of the syntax, see pip’s 
        section on VCS Support.

        python -m pip install -e git+https://git.repo/some_pkg.git#egg=SomeProject          # from git
        python -m pip install -e hg+https://hg.repo/some_pkg#egg=SomeProject                # from mercurial
        python -m pip install -e svn+svn://svn.repo/some_pkg/trunk/#egg=SomeProject         # from svn
        python -m pip install -e git+https://git.repo/some_pkg.git@feature#egg=SomeProject  # from a branch

    > Installing from other Indexes

        python -m pip install --index-url http://my.package.repo/simple/ SomeProject

**_Requirements - Packages_**

    bert-tensorflow        >= 1.0.4
    
    gensim                 == 4.0.0b0
    
    numpy                  >= 1.19.2
    
    pandas                 >= 1.2.3
    
    praw                   == 7. 2.1.dev0
    
    python-dotenv          >= 0.15.0
    
    tensorflow             >= 2.4.1
    
    tensorflow-addons      >= 0.12.1
    
    tensorflow-datasets    >= 4.2.0
    
    tensorflow-estimator   >= 2.4.0
    
    tensorflow-hub         >= 0.11.0
    
    tensorflow-metadata    >= 0.28.0
    
    tensorflow-text        >= 2.4.3
    
    tf-models-official     >= 2.4.0
    
    tensorflow-model-optimization >= 0.5.0

**_Requirements - NonPackages:_**

    * for these files ensure you do "chmod 600 ~/cup_a_code/.pyirc" to stop others
            from viewing your credentials

    > computer
    
    > python & virtual environment for it
        
    > * reddit developer account credentials in a .env 
        file (not uploaded to repo)
        
    > * pypi account credentials in .pyirc file 
        (not uploaded to repo)

**_Notes:_**

    > As of 2021-03-20 this is cloneable via git - 
        venv / condavenv create from setup or 
        conda_environment.yml file worked on my mac. 

**Author:**

    > Luke Sprangers
