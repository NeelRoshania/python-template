# python-template
Boiler plate scripted implementation for python modules

Features
- csv and text file read/write python implementation
- PostgreSQL integration
- aws integration
    - s3 read only

### References

### Installation guide

**Module setup**
1. `python3 -m venv .env` and `pip3 install --upgrade pip` 
2. `cd .env/scripts ` then `activate`
3. Modify `setup.cfg` and `src`
4. `pip3 install -e .`

If you run into issues with `psycopg2`, consider the following;
1. `sudo chmod 774 psycopg2_setup.sh`
2. `./psycopg2_setup.sh`
3. `pip3 install psycopg2`

**PostgreSQL installation & setup**
1. See (Ubuntu PostgreSQL)[https://help.ubuntu.com/community/PostgreSQL] for complete guide
2. Run `install_start_server.sh` - this will install and start the service
3. Check that the service is running `[ + ]  postgresql`
    - `service --status-all`
3. `sudo service postgresql restart` - to restart the service if required

**Jupyter kernel setup**
1. `jupyter kernelspec uninstall .example_env` - remove existing kernels called .example_env
2. `python -m ipykernel install --user --name=.example_env`- install new kernel

**Testing**
1. `pytest -v`

**Environment & application setup**
1. `pytest -v`
2. `pytest tests/scripts/test_psqlconnect.py > tests/test_outcomes/010123` to dump results to file. Use `grep` to search through dump

### Repository setup
1. Authenticate with github 
    - SSH Agent
        - `eval "$(ssh-agent -s)"` to start agent 
        - `ssh-add -l` to check for existing keys
        - `ssh-add ~/.ssh/id_ed25519` to add SSH private key to ssh-agen
    - Test connection & authenticate, 
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
            - Restart if neccesary, `sudo service postgresql restart`
