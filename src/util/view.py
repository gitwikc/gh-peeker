from datetime import datetime as dt
from colorama import Fore


def view_user(user):
    print(f"{Fore.GREEN}{user.username :^30}")
    print(f"{Fore.MAGENTA}ID\t\t{Fore.WHITE}{user.id}")
    print(f"{Fore.MAGENTA}Author\t\t{Fore.CYAN}{user.name}")
    print(f"{Fore.MAGENTA}Twitter\t\t{Fore.WHITE}{'@{user.twitter}' if user.twitter else '-'}")
    print(f"{Fore.MAGENTA}Repos\t\t{Fore.WHITE}{user.public_repos}")
    print('-' * 40)


def view_repo(repo):
    print(f"{Fore.MAGENTA}ID\t\t{Fore.WHITE}{repo.id}")
    print(f"{Fore.MAGENTA}Repo\t\t{Fore.CYAN}{repo.name}")
    print(f"{Fore.MAGENTA}Created\t\t{Fore.WHITE}{dt.strftime(dt.fromisoformat(repo.created[:-1]), '%a %d %b,%Y')}")
    print(f"{Fore.MAGENTA}Updated\t\t{Fore.WHITE}{dt.strftime(dt.fromisoformat(repo.updated[:-1]), '%a %d %b,%Y')}")
    print('=' * 40)
