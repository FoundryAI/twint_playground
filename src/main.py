"""Main entrypoint"""
from datetime import datetime
import twint
from yaml import safe_load

SEPARATOR = '_'


def main():
    """Main entrypoint"""
    # Import settings
    settings = safe_load(open('config/parameters.yml').read())
    username = settings['username']
    search = settings['search'] or ''
    timestamp = datetime.now().strftime("%Y%m%d%H%M")
    output = 'data/' + timestamp + SEPARATOR + username

    # Configure
    config = twint.Config()
    config.Username = username
    config.Store_csv = True
    config.Hide_output = True
    config.Resume = f"data/{username}.log"

    # Run
    if search == 'profile':
        config.Output = f"{output}_profile.csv"
        twint.run.Profile(config)

    elif search == 'followers':
        config.Output = f"{output}_followers.csv"
        twint.run.Followers(config)

    elif search == 'following':
        config.Output = f"{output}_following.csv"
        twint.run.Following(config)

    else:
        config.Search = search
        config.Output = f"{output}_{search.replace(' ', SEPARATOR)}.csv"
        twint.run.Search(config)


if __name__ == '__main__':
    main()
