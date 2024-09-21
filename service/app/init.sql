DROP TABLE IF EXISTS abominations;
DROP TABLE IF EXISTS implants;
DROP TABLE IF EXISTS users;

CREATE TABLE IF NOT EXISTS users(
id SERIAL PRIMARY KEY,
username character varying(128) NOT NULL,
password character varying(128) NOT NULL
);


CREATE TABLE IF NOT EXISTS implants(
bodypart character varying(128) NOT NULL,
name character varying(128) NOT NULL,
id integer NOT NULL
);
    

INSERT INTO implants (bodypart, name, id) VALUES 
('head', 'carbon skull', 1),
('head', 'cosmic antenn', 2),
('head', 'integrated makarov', 3),
('eye', 'laser pointer', 1),
('eye', 'y-ray vision', 2),
('eye', 'x10 zoom', 3),
('body', 'civilian camouflage', 1),
('body', 'visibility suit', 2),
('body', 'nirvana t-shirt', 3),
('arm', 'bazooka', 1),
('arm', 'another bazooka', 2),
('arm', 'can-closer', 3),
('leg', 'six-fingered foot', 1),
('leg', 'small pocket (can fit 0,331% of phone)', 2),
('leg', 'default leg', 3);

CREATE TABLE IF NOT EXISTS abominations(
id SERIAL NOT NULL PRIMARY KEY,
id_owner integer NOT NULL REFERENCES users (id),
name character varying(128) NOT NULL,
gender character varying(128) NOT NULL,
is_private boolean NOT NULL,
head integer NOT NULL,
eye integer NOT NULL,
body integer NOT NULL,
arm integer NOT NULL,
leg integer NOT NULL
);

