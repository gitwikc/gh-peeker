from requests import get
from collections import namedtuple


GithubUser = namedtuple('GithubUser', field_names=('id', 'name', 'username', 'twitter', 'public_repos'))
Repository = namedtuple('Repository', field_names=('id', 'name', 'created', 'updated'))


def get_user_info(username: str) -> namedtuple:
    url = f'https://api.github.com/users/{username}'
    res = get(url).json()
    user = GithubUser(
        id=res['id'],
        name=res['name'],
        username=res['login'],
        twitter=res['twitter_username'],
        public_repos=res['public_repos'],
    )
    return user


def get_repo_info(username, repo_name):
    repo_url = f'https://api.github.com/repos/{username}/{repo_name}'
    res = get(repo_url).json()
    repo = Repository(
        id=res['id'],
        name=res['name'],
        created=res['created_at'],
        updated=res['updated_at'],
    )
    return repo
