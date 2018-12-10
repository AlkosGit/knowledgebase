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
        
        Connect to online repository:
            $ git remote add origin https://github.com/AlkosGit/<reponame>.git
            $ git push -u origin master


    Exclude local files and dirs from syncing with online repository:
    At the start of the project one can create a list with files and/or dirs to exclude from commits.
        Edit the file .git/info/exclude:
            /__pycache__
            *.swp
            *.db

        This exclusion config is valid for the local machine only. To make it global (i.e. everyone downloading the repo will 
        have the same exclusion configuration applied), create the file '.gitignore' in the repository.
        The syntax is similar to above.

        Note that files and dirs on this list will be deleted from the online repository.
    
    
    Exclude local files and dirs that already have been commited:
    Instead of permanently excluding files and/or dirs, one can temporarily exclude them from commits. 
        This has the advantage of keeping these in the online repository. Useful for e.g. databases.
        Note that temporarily exluded files and/or dirs should not be on an exclusion list (i.e. not present in 
        .gitignore of .git/info/exclude).
        Disable tracking of file:
            $ git update-index --assume-unchanged <file>

        To resume tracking:
            $ git update-index --no-assume-unchanged <file>


    Force local repository to synchronize with on-online master:
        Warning: this will remove local files not in master.
            $ git fetch --all
            $ git reset --hard origin/master

    """
