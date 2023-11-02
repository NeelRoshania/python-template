# References
#   - https://www.digitalocean.com/community/tutorials/how-to-install-postgresql-on-ubuntu-22-04-quickstart


# install the following packages
# sudo apt install postgresql-client-common
# sudo apt-get install postgresql-client
sudo apt install postgresql postgresql-contrib    

 
# The Postgres authentication system makes the following assumptions assumptions;
# 1. Postgres uses a concept called “roles” to handle authentication and authorization. 
# 2. Postgres is set up to use ident authentication, meaning that it associates Postgres roles with a matching Unix/Linux system account.
# 3. The installation procedure created a user account called postgres that is associated with the default Postgres role
# 4. For any role used to log in, that role will have a database with the same name which it can access.

# Confirm default user;

# enter postgres client - method 1
sudo -i -u postgres # switch to postgresql
postgres@ip-xxx-xx-xx-xx:~$ psql 
postgres=# \l # check existing databases
postgres=# \q # quit

# enter postgres client - method 2
sudo -u postgres psql

# Define a new user that isn't the default e.g sammy;
sudo -u postgres createuser --interactive

# Define database associate to new user
sudo -u postgres createdb sammy

# Access psql with new user
sudo -u sammy psql
sammy=# \conninfo # confirm connection details
# You are connected to database "sammy" as user "sammy" via socket in "/var/run/postgresql" at port "xxxx".
