from github_api import get_user_profile, get_user_repositories
from analyzer import (
    calculate_total_stars,
    get_most_starred_repository,
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

    total_stars = calculate_total_stars(repos)
    most_starred = get_most_starred_repository(repos)

    display_profile(profile, total_stars, most_starred)
    display_repositories(repos)


if __name__ == "__main__":
    main()