def display_profile(profile, total_stars, total_forks, most_starred, most_used_language):
    print("\n✅ Profile Found!\n")

    print(f"Name         : {profile['name']}")
    print(f"Username     : {profile['login']}")
    print(f"Followers    : {profile['followers']}")
    print(f"Following    : {profile['following']}")
    print(f"Public Repos : {profile['public_repos']}")
    print(f"Total Stars  : {total_stars}")
    print(f"Total Forks  : {total_forks}")

    if most_starred:
        print(f"Top Repository : {most_starred['name']}")
        print(f"Top Repo Stars : {most_starred['stargazers_count']}")

    if most_used_language:
        language, count = most_used_language
        print(f"Most Used Language : {language}")
        print(f"Repositories Using : {count}")


def display_repositories(repositories):
    print("\nRepositories")
    print("-" * 20)

    if not repositories:
        print("No repositories found.")
        return

    for repo in repositories:
        print(f"- {repo['name']}")