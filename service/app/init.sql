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
('head', 'the pot', 4),
('head', 'time decelerator', 5),
('head', 'seer power', 6),
('head', 'radar like on ship', 7),
('head', 'arbuz', 8),
('eye', 'laser pointer', 1),
('eye', 'y-ray vision', 2),
('eye', 'x10 zoom', 3),
('eye', 'kaleidoscopes', 4),
('eye', 'cat eye', 5),
('eye', 'cool glasses', 6),
('eye', 'third eye', 7),
('eye', '20/20', 8),
('body', 'civilian camouflage', 1),
('body', 'visibility suit', 2),
('body', 'nirvana t-shirt', 3),
('body', 'turtle shell', 4),
('body', 'kebab spit', 5),
('body', 'typhoon deus ex', 6),
('body', 'holo cloak', 7),
('body', 'nanomachines', 8),
('arm', 'bazooka', 1),
('arm', 'another bazooka', 2),
('arm', 'can-closer', 3),
('arm', 'comically large pencil', 4),
('arm', 'kebab knife (oldschool)', 5),
('arm', 'gorilla arm', 6),
('arm', 'kebab knife (newschool)', 7),
('arm', 'very fast finger', 8),
('leg', 'six-fingered foot', 1),
('leg', 'small pocket (can fit 0,331% of phone)', 2),
('leg', 'default leg', 3),
('leg', 'springs', 4),
('leg', 'monowheel', 5),
('leg', 'wide jeans', 6),
('leg', 'batin botinok', 7),
('leg', 'long fall boots', 8);

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

