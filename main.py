from github_api import get_user_profile


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

    print("\n✅ Profile Found!")
    print(f"Name: {profile['name']}")


if __name__ == "__main__":
    main()