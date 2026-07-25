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


def display_profile(
    profile,
    total_stars,
    total_forks,
    most_starred,
    most_used_language,
    average_stars,
    average_forks,
    newest_repository,
    oldest_repository
):
    
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

        table.add_row(
        "Average Stars",
        str(average_stars)
    )

    table.add_row(
        "Average Forks",
        str(average_forks)
    )

    if newest_repository:
        table.add_row(
            "Newest Repository",
            newest_repository["name"]
        )

    if oldest_repository:
        table.add_row(
            "Oldest Repository",
            oldest_repository["name"]
        )

    console.print(table)


def display_repositories(repositories):

    table = Table(
        title="Repositories",
        show_header=True,
        header_style="bold magenta"
    )

    table.add_column("Repository", style="cyan")
    table.add_column("Stars", justify="right")
    table.add_column("Forks", justify="right")
    table.add_column("Language")

    if not repositories:
        console.print("[red]No repositories found.[/red]")
        return

    for repo in repositories:

        language = repo["language"]

        if language is None:
            language = "-"

        table.add_row(
            repo["name"],
            str(repo["stargazers_count"]),
            str(repo["forks_count"]),
            language
        )

    console.print(table)