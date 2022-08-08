import requests

"""
    Class user that make all the requests for the user category
"""


# The User class is used to get the data for a given user. It has two methods, one to get the user
# data and the other to get the list of repos for the user.
class User:
    def __init__(self, name, action_call):
        """
        The function __init__() is a special function in Python classes. It is run as soon as an object
        of a class is instantiated. The method __init__() is similar to constructors in C++ and Java

        :param name: The name of the user
        :param action_call: "DATA" or "REPO"
        """

        self.name = name
        self.action_call = action_call

    def __get_user_data(self):
        """
        This function takes in a user's name and returns a url that will be used to grab the user's
        public data.
        :return: The url to the github api to grab public user data.
        """

        # github api url to grab public user data
        url = f"https://api.github.com/users/{self.name}"
        return url

    def __get_user_repos(self):
        """
        This function takes in a github username and returns a list of all the repos for that user
        :return: the url
        """

        # github api url to grab the list of repos for the user given. An additional param of  page is given as the github search api returns only 30 results per page. This query will return up to 1000 results
        url = f"https://api.github.com/users/{ self.name }/repos?page=1&per_page=1000"
        return url

    def __str__(self):
        """
        The `__str__` function is a special function that is called when we try to print an object
        :return: The name of the user.
        """

        # if we ever need to return the user as a string
        return f"{ self.name }"

    def user_main(self):
        """
        The function takes in the name of the user and the action to be performed on the user. It then
        calls the appropriate function to get the url for the API call. It then makes the API call and
        returns the response
        :return: a json object that contains the user's data or the user's repositories.
        """

        # the main function that is exposed to be called from main.py
        url = ""
        try:
            if self.action_call == "DATA":
                url = self.__get_user_data()
                response = requests.get(url)
                return response.json()

            elif self.action_call == "REPOS":
                url = self.__get_user_repos()
                response = requests.get(url)
                data = response.json()
                repos = []
                # we are getting only the names of the repos and not all the details for each repo. If we want more details, we just change the code below to accommodate that
                for res in data:
                    repos.append(res["name"])
                return {
                    "user": self.name,
                    "repositories": repos,
                    "number_of_repositories": len(repos),
                }

        except Exception as e:
            return e
