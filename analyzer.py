from datetime import datetime
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


def sort_repositories_by_stars(repositories):
    """
    Return repositories sorted by stars (highest first).
    """

    return sorted(
        repositories,
        key=lambda repo: repo["stargazers_count"],
        reverse=True
    )

def calculate_average_stars(repositories):
    """
    Calculate the average stars per repository.
    """

    if not repositories:
        return 0

    total_stars = calculate_total_stars(repositories)

    return round(total_stars / len(repositories), 2)

def calculate_average_forks(repositories):
    """
    Calculate the average forks per repository.
    """

    if not repositories:
        return 0

    total_forks = calculate_total_forks(repositories)

    return round(total_forks / len(repositories), 2)

def get_newest_repository(repositories):
    """
    Return the newest repository.
    """

    if not repositories:
        return None

    newest = repositories[0]

    for repo in repositories:

        current_date = datetime.strptime(
            repo["created_at"],
            "%Y-%m-%dT%H:%M:%SZ"
        )

        newest_date = datetime.strptime(
            newest["created_at"],
            "%Y-%m-%dT%H:%M:%SZ"
        )

        if current_date > newest_date:
            newest = repo

    return newest

def get_oldest_repository(repositories):
    """
    Return the oldest repository.
    """

    if not repositories:
        return None

    oldest = repositories[0]

    for repo in repositories:

        current_date = datetime.strptime(
            repo["created_at"],
            "%Y-%m-%dT%H:%M:%SZ"
        )

        oldest_date = datetime.strptime(
            oldest["created_at"],
            "%Y-%m-%dT%H:%M:%SZ"
        )

        if current_date < oldest_date:
            oldest = repo

    return oldest