import requests


def get_user_profile(username):
    """
    Fetch a GitHub user's profile.

    Parameters:
        username (str): GitHub username

    Returns:
        dict: Profile data if successful
        None: If the user is not found
    """

    url = f"https://api.github.com/users/{username}"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    return None