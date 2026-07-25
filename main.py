from github_api import get_user_profile, get_user_repositories
from analyzer import (
    calculate_total_stars,
    get_most_starred_repository,
)


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

    print("\n✅ Profile Found!\n")

    print(f"Name         : {profile['name']}")
    print(f"Username     : {profile['login']}")
    print(f"Followers    : {profile['followers']}")
    print(f"Following    : {profile['following']}")
    print(f"Public Repos : {profile['public_repos']}")

    total_stars = calculate_total_stars(repos)
    print(f"Total Stars  : {total_stars}")

    most_starred = get_most_starred_repository(repos)

    if most_starred:
        print(f"Top Repository : {most_starred['name']}")
        print(f"Top Repo Stars : {most_starred['stargazers_count']}")

    print("\nRepositories")
    print("-" * 20)

    if repos:
        for repo in repos:
            print(f"- {repo['name']}")
    else:
        print("No repositories found.")


if __name__ == "__main__":
    main()