def calculate_total_stars(repositories):
    """
    Calculate the total number of stars across all repositories.
    """

    total_stars = 0

    for repo in repositories:
        total_stars += repo["stargazers_count"]

    return total_stars


def calculate_total_forks(repositories):
    """
    Calculate the total number of forks across all repositories.
    """

    total_forks = 0

    for repo in repositories:
        total_forks += repo["forks_count"]

    return total_forks


def get_repository_with_highest_value(repositories, key):
    """
    Find the repository with the highest value for the given key.

    Parameters:
        repositories (list): List of repositories
        key (str): Dictionary key to compare

    Returns:
        dict | None
    """

    if not repositories:
        return None

    highest = repositories[0]

    for repo in repositories:
        if repo[key] > highest[key]:
            highest = repo

    return highest

def count_languages(repositories):
    """
    Count how many repositories use each programming language.

    Parameters:
        repositories (list): List of GitHub repositories

    Returns:
        dict: Language counts
    """

    language_count = {}

    for repo in repositories:

        language = repo["language"]

        if language is None:
            continue

        if language in language_count:
            language_count[language] += 1
        else:
            language_count[language] = 1

    return language_count

def get_most_used_language(language_count):
    """
    Return the most frequently used programming language.

    Parameters:
        language_count (dict): Dictionary of language counts

    Returns:
        tuple | None:
            (language_name, count)
    """

    if not language_count:
        return None

    language = max(language_count, key=language_count.get)

    return language, language_count[language]