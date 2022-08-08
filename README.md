# work_with_git
a Python wrapper around the github api


# Overview

Build a pip wheel to make an installable wrapper around the github api on two endpoints on the User and Repo APIs
1. For the User, find all user data and search for all public repos belonging to the user
- requires user name and an action_call param that asks for an input of either "DATA" or "REPOS"
2. For the Repositories, create or delete one
- requires user name, github auth_token, repo name, description and True / False (as string input) to state if the repo is private or not.

#  How to use

1. copy the wheel file ```work_with_git-1.0-py3-none-any.whl``` into your repo root.
2. pip install this file from command line with:
```pip install work_with_git-1.0-py3-none-any.whl```
3. add this import to the top of the file you want to use it in
```from work_with_git.main import work_with_git```
4. call the main function with:
```work_with_git()```
5. run the file this function is called in. For example, if the file is main.py, run:
```python main.py```
6. Answer the prompts and use the functionality.



