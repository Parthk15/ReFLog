from github_api import get_user_profile, get_user_repositories
from analyzer import (
    calculate_total_stars,
    calculate_total_forks,
    calculate_average_stars,
    calculate_average_forks,
    get_repository_details,
    get_repository_with_highest_value,
    count_languages,
    get_most_used_language,
    sort_repositories_by_stars,
    get_newest_repository,
    get_oldest_repository,
    find_repository,
    
)
from ui import (
    display_header,
    display_profile,
    display_repositories,
    display_repository_details,
)

def main():
    display_header()

    username = input("\nEnter a GitHub username: ")

    profile = get_user_profile(username)

    if profile is None:
        print("\n❌ User not found.")
        return

    repos = get_user_repositories(username)

    sorted_repositories = sort_repositories_by_stars(repos)

    average_stars = calculate_average_stars(repos)

    average_forks = calculate_average_forks(repos)

    newest_repository = get_newest_repository(repos)

    oldest_repository = get_oldest_repository(repos)
        
    language_count = count_languages(repos)

    

    language_count = count_languages(repos)
    most_used_language = get_most_used_language(language_count)

    total_stars = calculate_total_stars(repos)
    total_forks = calculate_total_forks(repos)

    most_starred = get_repository_with_highest_value(
        repos,
        "stargazers_count"
    )

    display_profile(
    profile,
    total_stars,
    total_forks,
    most_starred,
    most_used_language,
    average_stars,
    average_forks,
    newest_repository,
    oldest_repository,
)

    display_repositories(sorted_repositories)
    repo_name = input("\nEnter repository name to view details: ")

    repo = find_repository(
        sorted_repositories,
        repo_name
    )

    if repo:
        details = get_repository_details(repo)
        display_repository_details(details)
    else:
        print("Repository not found")


if __name__ == "__main__":
    main()