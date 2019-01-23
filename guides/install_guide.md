# Install Guide
Follow these steps to get NGSC App running on your local computer!

See [this PowerPoint](https://docs.google.com/presentation/d/1pAoLLMqqH6JGG9ILwlhKMwVzUVzux9bFmZINPJWeW9Q/edit?usp=sharing) 
for further context on what we're doing, especially why it's necessary for PCs.

## Step 1: Download software required

### Install software on Mac
1. HomeBrew package manager: `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
1. Git: `brew install git`
1. Python 3.7: `brew install python3`
1. Pipenv: `pip3 install pipenv`
1. Node.js: `brew install node`
1. Yarn package manager: `brew install yarn`
1. Heroku: `brew install heroku`

### Install software on PC
1. Git & Git Bash, https://git-scm.com/downloads
    1. Accept every default setting, except for choosing your default text editor:
        1. The default, Vim, is great but confusing if you've never used it.
        1. Recommended to download the app Visual Studio Code and then choose that as your option.
1. Python 3.7, https://www.python.org/downloads/ 
    1. Check on the option to add python.exe to your PATH variable.
1. Pipenv: `pip install pipenv`
1. Node.js, https://nodejs.org/en/ 
    1. Choose the most current version
    1. Accept default settings
1. Yarn, installer from https://yarnpkg.com/en/docs/install
1. Heroku, 64 bit installer from https://devcenter.heroku.com/articles/heroku-cli
    1. Accept defaults

## Step 2: Clone & install the project
This step gets the code actually down to your computer and running.

1. Open up bash
    1. On Mac, this is called Terminal
    1. On PC, this is called Git Bash
1. Navigate to the folder you want to be the root folder, using `cd path/to/folder/you/want`
1. `git clone https://github.com/Eric-Arellano/ngsc-app.git`
1. `cd ngsc-app`
1. `./ngsc install`


## Step 3: Configure PyCharm
PyCharm is the recommended IDE (integrated developer editor, i.e. where you actually write code) for this project.
 
1. Apply for [student program](https://www.jetbrains.com/student/)
1. Download and install [PyCharm Professional](https://www.jetbrains.com/pycharm/)
1. Setup the Python interpreter
    1. main menu -> PyCharm -> Preferences
    1. Select `Project: ngsc-app` -> Project interpreter
    1. Click the small wheel in the top right -> Add
    1. Choose "Select existing environment" -> click the `...` button
    1. In the file selector, find the folder for this current project, then choose `.venv/bin/python`
        1. Click the 3rd icon (the folder) to jump to the current folder
1. Setup JavaScript
1. Change style preferences
    1. main menu -> PyCharm -> Preferences
    1. Select Editor -> Code Style
    1. Select JavaScript
        1. Punctuation:
            1. "Don't use semicolons"
            1. "Use single quotes"
            1. Keep trailing commas
            
(Eric - to finish)
