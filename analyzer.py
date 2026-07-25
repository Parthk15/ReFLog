def calculate_total_stars(repositories):
    """
    Calculate the total number of stars across all repositories.
    """

    total_stars = 0

    for repo in repositories:
        total_stars += repo["stargazers_count"]

    return total_stars


def get_most_starred_repository(repositories):
    """
    Find the repository with the highest number of stars.

    Parameters:
        repositories (list): List of GitHub repositories

    Returns:
        dict: Repository with the most stars
        None: If there are no repositories
    """

    if not repositories:
        return None

    most_starred = repositories[0]

    for repo in repositories:
        if repo["stargazers_count"] > most_starred["stargazers_count"]:
            most_starred = repo

    return most_starred