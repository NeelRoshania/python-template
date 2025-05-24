# python-template
A minimal template for building Python packages with logging, database helpers and example scripts.

## Features

- CSV and text file read/write helpers
- JSON utilities
- PostgreSQL connection helper
- AWS S3 integration (read only)
- Snowflake helper functions
- Logging configured via `conf/logging.conf`
- Example asynchronous HTTP requests
- Invoke tasks for `lint`, `format` and `test`

## Installation guide

### Module setup
1. `python3 -m venv .env` and `pip3 install --upgrade pip`
2. `cd .env/scripts` then `activate`
3. Modify `src/setup.cfg` - change project name
4. `pip3 install -e .`
5. Change `qualname` in `conf/logger.conf`
6. Copy `conf/pipeline.template.conf` to `conf/pipeline.conf` and update credentials

If you run into issues with `psycopg2`, consider the following:
1. `sudo chmod 774 psycopg2_setup.sh`
2. `./psycopg2_setup.sh`
3. `pip3 install psycopg2`

### Using invoke tasks
- `invoke lint` – run flake8
- `invoke format --fix` – apply black formatting
- `invoke test` – run unit tests

## PostgreSQL installation & setup
1. See [Ubuntu PostgreSQL](https://help.ubuntu.com/community/PostgreSQL) for complete guide
2. Run `install_start_server.sh` – this will install and start the service
3. Check that the service is running `[ + ] postgresql`
    - `service --status-all`
4. `sudo service postgresql restart` – restart the service if required

## Jupyter kernel setup
1. `jupyter kernelspec uninstall .example_env` – remove existing kernels called `.example_env`
2. `python -m ipykernel install --user --name=.example_env` – install new kernel

## Testing
1. `pytest -v`

You can also dump the results to a file:
`pytest tests/scripts/test_psqlconnect.py > tests/test_outcomes/010123`

## Repository setup
1. Authenticate with GitHub
    - SSH Agent
        - `eval "$(ssh-agent -s)"` to start agent
        - `ssh-add -l` to check for existing keys
        - `ssh-add ~/.ssh/id_ed25519` to add SSH private key to the agent
    - Test connection & authenticate
        - `ssh -T git@github.com`. See [Github SSH Authentication](https://docs.github.com/en/authentication).
2. Authentication troubleshooting
    - [Permission denied (publickey)](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
3. PostgreSQL commands
    - [Client Applications](https://www.postgresql.org/docs/current/reference-client.html)
        - `ls -al /usr/lib/postgresql/15/bin`
    - Debugging
        ```
        psql: could not connect to server: No such file or directory
              Is the server running locally and accepting connections on Unix domain socket "/tmp/.s.PGSQL.5432"?
        ```
        - Check that the server is running, `service --status-all`.
            - Restart if necessary, `sudo service postgresql restart`
