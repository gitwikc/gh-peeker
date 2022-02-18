import click
from .util.git_info import get_repo_info, get_user_info
from .util.view import view_repo, view_user


@click.command()
@click.option("-u", "--username", help="Username of GitHub user", required=True)
@click.option("-r", "--repo", help="Name of repo", required=True)
def cli(username, repo):
    user = get_user_info(username)
    repo = get_repo_info(username, repo)
    view_user(user)
    view_repo(repo)
