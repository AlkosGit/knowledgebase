# file: git.py
from listprops import ListProps

class Doc(ListProps):
    """
    Create new repository:
    Log in to github.com and create a new repository.
        Initialize local repository:
            $ git init
        
        Add files to index:
            $ git add .
        
        Commit changes:
            $ git commit -m "<description>"

        Push changes to upstream:
            $ git push

        Synchronize with upstream:
            $ git pull
        
        Connect to online repository:
            $ git remote add origin https://github.com/AlkosGit/<reponame>.git
            $ git push -u origin master
    """
