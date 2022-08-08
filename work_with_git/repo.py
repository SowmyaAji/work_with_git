import requests
import json


# The class Repo has a private member function __delete_repo() that deletes a repo
# It takes in a user name, a token, and a repo name and assigns them to the class variables user_name,
# auth_token, and repo_name
class Repo:
    def __init__(self, user_name, token, repo_name):
        """
        This function takes in a user name, a token, and a repo name and assigns them to the class
        variables user_name, auth_token, and repo_name

        :param user_name: The username of the user who owns the repository
        :param token: This is the user's github auth_token
        :param repo_name: The name of the repository you want to create or delete
        """

        self.user_name = user_name
        self.repo_name = repo_name
        self.auth_token = token

    # the delete function is not inherited by any other repo classes. It requires just the basic properties that repo has, so it is not a class by itself
    def __delete_repo(self):
        """
        It deletes a repository
        :return: A dictionary with the message, user name and status of the request.
        """

        url = f"https://api.github.com/repos/{self.user_name}/{self.repo_name}"
        headers = {"Authorization": f"token { self.auth_token }"}
        res = requests.delete(url, headers=headers)
        if "204" in str(res):
            return {
                "msg": f"Repository { self.repo_name } successfully deleted",
                "user": self.user_name,
                "status": res,
            }
        else:
            return {
                "msg": f"Repository { self.repo_name } could not be deleted. Please check user name, repository name and token",
                "user": self.user_name,
                "status": res,
            }

    def repo_main(self):
        return self.__delete_repo()


class CreateRepo(Repo):
    """
    Inherits Repo and adds additional properties needed to create repo
    """

    def __init__(self, user_name, token, repo_name, description, classification):
        """
        The function __init__() is a constructor that initializes the attributes of the class

        :param user_name: The user name of the user who creates the repository
        :param token: The user's github auth_token
        :param repo_name: The name of the repository you want to create
        :param description: A string that describes the repository
        :param classification: The classification of the repository as private or public as a bool gpt the key private. Default is False
        """

        super().__init__(user_name, token, repo_name)
        self.description = description
        self.classification = classification

    def create_repo(self):
        """
        It takes the user's name, the name of the repository, the description of the repository, and the
        classification of the repository (public or private) and creates a repository on GitHub
        :return: A dictionary with the message, user name and status of the request.
        """

        url = "https://api.github.com/user/repos"
        headers = {"Authorization": f"token { self.auth_token }"}
        data = {
            "name": self.repo_name,
            "description": self.description,
            "private": self.classification,
        }
        res = requests.post(url, data=json.dumps(data), headers=headers)
        if "201" in str(res):
            return {
                "msg": f"Repository { self.repo_name } successfully created",
                "user": self.user_name,
                "status": res,
            }
        else:
            return {
                "msg": f"Repository { self.repo_name } could not be created. Please check user name and token",
                "user": self.user_name,
                "status": res,
            }
