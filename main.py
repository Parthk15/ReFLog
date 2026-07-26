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

def display_menu():

    print("\n1. View Repository List")
    print("2. View Repository Details")
    print("3. Analyze Another User")
    print("4. Exit")

    choice = input("\nChoose an option: ")

    return choice

def analyze_user():

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

    return sorted_repositories

def main():
    display_header()

    sorted_repositories = analyze_user()



    while True:

        choice = display_menu()

        if choice == "1":

            display_repositories(sorted_repositories)

        elif choice == "2":

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


        elif choice == "3":

            sorted_repositories = analyze_user()


        elif choice == "4":

            print("\nExiting Reflog...")
            break


        else:

            print("\nInvalid option.")


if __name__ == "__main__":
    main()