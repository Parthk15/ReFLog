import requests


def get_user_profile(username):
    """
    Fetch a GitHub user's profile.
    """

    url = f"https://api.github.com/users/{username}"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    return None


def get_user_repositories(username):
    """
    Fetch all public repositories for a GitHub user.

    Parameters:
        username (str): GitHub username

    Returns:
        list: Repository data if successful
        None: If the request fails
    """

    url = f"https://api.github.com/users/{username}/repos"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    return None