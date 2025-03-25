unpleasant writeup

flag is stored in abomination gender.

1. hardcoded JWT secret

jwt is encoded by HS256 symmetric algorithm.
secret key is located in service/app/static/key.txt.
with secret key we can sign our token, with user_id of victim.
with that token we can get access to private abominations of user.

#solution:

change secret


2. SQL injection

zero parameterized queries

#solution:

parameterize them all
