# Cup a Code: 
#### PyPi Package 
    Use tests/test_basic/more/even_more.py (3 files) to get feel for Doc2Vec, BERT, NNetworks, Word Embedding Models, compressing, and using

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

**_DUMP OF NOTES:_**

    praw subreddit comment attributes: 
        author: The author of the comment
        body: The body of the comment
        body_html: The body of the comment, as HTML.        
        created_utc: Time the comment was created, represented in Unix Time.        
        distinguished: Whether or not the comment is distinguished.        
        edited: Whether or not the comment has been edited.       
        id: The ID of the comment.     
        is_submitter: Whether or not the comment author is also the author of the submission.       
        link_id: The submission ID that the comment belongs to.       
        parent_id: The ID of the parent comment (prefixed with t1_). If it is a top-level comment, this returns the submission ID instead (prefixed with t3_).       
        permalink: A permalink for the comment. Comment objects from the inbox have a context attribute instead.       
        replies: Provides an instance of CommentForest.      
        saved: Whether or not the comment is saved.
        score: The number of up-votes for the comment.
        stickied: Whether or not the comment is stickied.
        submission: Provides an instance of Submission. The submission that the comment belongs to.
        subreddit: Provides an instance of Subreddit. The subreddit that the comment belongs to.
        subreddit_id: The subreddit ID that the comment belongs to.

**Author:**

    > Luke Sprangers
