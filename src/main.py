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
    search = settings['search']
    timestamp = datetime.now().strftime("%Y%m%d%H%M")
    output = timestamp + SEPARATOR + username

    if search:
        output = output + SEPARATOR + search.replace(' ', SEPARATOR)

    # Configure
    config = twint.Config()
    config.Username = username
    config.Search = search
    config.Store_csv = True
    config.Output = f"data/{output}.csv"

    # Run
    twint.run.Search(config)


if __name__ == '__main__':
    main()
