def display_profile(profile, total_stars, most_starred):
    print("\n✅ Profile Found!\n")

    print(f"Name         : {profile['name']}")
    print(f"Username     : {profile['login']}")
    print(f"Followers    : {profile['followers']}")
    print(f"Following    : {profile['following']}")
    print(f"Public Repos : {profile['public_repos']}")
    print(f"Total Stars  : {total_stars}")

    if most_starred:
        print(f"Top Repository : {most_starred['name']}")
        print(f"Top Repo Stars : {most_starred['stargazers_count']}")


def display_repositories(repositories):
    print("\nRepositories")
    print("-" * 20)

    if not repositories:
        print("No repositories found.")
        return

    for repo in repositories:
        print(f"- {repo['name']}")