from github_api import get_user_profile, get_user_repositories
from analyzer import (
    calculate_total_stars,
    calculate_total_forks,
    get_repository_with_highest_value,
    count_languages,
    get_most_used_language,
)
from ui import display_profile, display_repositories


def main():
    print("=" * 40)
    print("              REFLOG")
    print("      GitHub Profile Analyzer")
    print("=" * 40)

    username = input("\nEnter a GitHub username: ")

    profile = get_user_profile(username)

    if profile is None:
        print("\n❌ User not found.")
        return

    repos = get_user_repositories(username)
    
    language_count = count_languages(repos)
    print(language_count)

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
        most_used_language
    )

    display_repositories(repos)


if __name__ == "__main__":
    main()