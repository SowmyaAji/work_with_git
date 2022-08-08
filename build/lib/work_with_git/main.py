from pprint import pprint as pp
from work_with_git.user_interface import work_with_repo, work_with_user


def work_with_git() -> None:
    """The function work_with_git() is the main function that will be called to start the program. It will ask the user to input a category to work with. If the user inputs U, then the function work_with_user() will be called. If the user inputs R, then the function work_with_repo() will be called. If the user inputs E, then the program will exit

    """

    # first interface with users
    category = ""

    while category != "E":
        category = (
            input(
                "What category do you want to work with? Type U for User or R for Repository or E to Exit this program: "
            )
            .strip()
            .upper()
        )
        if category:
            if category == "U":
                work_with_user()
            elif category == "R":
                work_with_repo()
            elif category == "E":
                pp({"msg": f"Thanks for using work with git"})
            else:
                pp(
                    {
                        "msg": f"Category { category } is not inputted correctly. Please type U for User or R for Repo"
                    }
                )

        else:
            pp(
                {
                    "msg": f"Category { category } is not inputted correctly. Please type U for User or R for Repo"
                }
            )


if __name__ == "__main__":
    work_with_git()
