from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def display_header():
    panel = Panel(
        "[bold cyan]REFLOG[/bold cyan]\nGitHub Profile Analyzer",
        title="Welcome",
        border_style="cyan",
    )

    console.print(panel)


def display_profile(profile, total_stars, total_forks, most_starred, most_used_language):

    table = Table(
        title="GitHub Profile",
        show_header=True,
        header_style="bold cyan"
    )

    table.add_column("Property", style="green")
    table.add_column("Value", style="white")

    table.add_row("Name", str(profile["name"]))
    table.add_row("Username", profile["login"])
    table.add_row("Followers", str(profile["followers"]))
    table.add_row("Following", str(profile["following"]))
    table.add_row("Public Repositories", str(profile["public_repos"]))
    table.add_row("Total Stars", str(total_stars))
    table.add_row("Total Forks", str(total_forks))

    if most_starred:
        table.add_row(
            "Top Repository",
            f"{most_starred['name']} ⭐ {most_starred['stargazers_count']}"
        )

    if most_used_language:
        language, count = most_used_language
        table.add_row(
            "Most Used Language",
            f"{language} ({count})"
        )

    console.print(table)


def display_repositories(repositories):
    print("\nRepositories")
    print("-" * 20)

    if not repositories:
        print("No repositories found.")
        return

    for repo in repositories:
        print(f"- {repo['name']}")