from work_with_git.user import User
from work_with_git.repo import Repo, CreateRepo
from pprint import pprint as pp


def work_with_user() -> None:
    """
    It takes in a user name and an action call, creates a User object and calls the user_main method on
    it
    """

    name = input("Please give the name of the user: ").strip().lower()
    action_call = (
        input(
            "Please write whether you want all data of the user or a list of the user's public repos. Type DATA for user data and REPOS for user repos: "
        )
        .strip()
        .upper()
    )
    new_user = User(name, action_call)
    try:
        response = new_user.user_main()
        if response:
            pp(response)
        else:
            # in case the user inputs an erroneous action call or erroneous user name.
            pp({"msg": f"Action { action_call } is not supported for user { name }"})

    except Exception as e:
        print("Exception: ", e)


def get_bool_from_input(classification: str) -> bool:
    """
    > This function takes in a string and returns a boolean
    
    :param classification: The classification of the repository as private or not
    :type classification: str
    :return: A boolean value
    """

    return classification == "TRUE"


def work_with_repo() -> None:
    """
    It takes in a user name, an authentication token, a repository name, an action (create or delete)
    and a description and creates or deletes a repository
    """

    user_name = input("Please give the name of the user: ").strip().lower()
    token = input("Please paste your authentication token for github: ").strip()
    repo_name = input(
        "Please give the name of the repository you want to create or delete: "
    ).strip()
    action = (
        input("Please type C to create a repo and D to delete a repo: ").strip().upper()
    )
    if action:
        if action == "D":
            new_repo = Repo(user_name, token, repo_name)
            try:
                response = new_repo.repo_main()
                pp(response)
            except Exception as e:
                print("Exception: ", e)
        elif action == "C":
            description = input(
                "Please give a short description for the new repository: "
            ).strip()
            classification = (
                input(
                    "Please state if this repo is private or not. If it is private, please type True: "
                )
                .strip()
                .upper()
            )
            private = get_bool_from_input(classification)
            new_repo = CreateRepo(user_name, token, repo_name, description, private)
            try:
                response = new_repo.create_repo()
                pp(response)
            except Exception as e:
                print("Exception: ", e)

    else:
        # in case the user inputs an erroneous action call or erroneous user name.
        pp({"msg": f"Action { action } is not supported for user { user_name }"})
