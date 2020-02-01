BEGIN;
	
CREATE TABLE city (
    id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE road (
    id1 INTEGER,
    id2 INTEGER,
    d FLOAT
);

INSERT INTO city VALUES (1, 'Roma');
INSERT INTO city VALUES (2, 'Berlin');
INSERT INTO city VALUES (3, 'Wien');
INSERT INTO city VALUES (4, 'Bratislava');
INSERT INTO city VALUES (5, 'Praha');
INSERT INTO city VALUES (6, 'Rio de Janeiro');
INSERT INTO city VALUES (7, 'Caracas');
INSERT INTO city VALUES (8, 'Los Angeles');
INSERT INTO city VALUES (9, 'Quebec');
INSERT INTO city VALUES (10, 'Johannesburg');

INSERT INTO road VALUES (1, 3, 765.56);
INSERT INTO road VALUES (2, 5, 279.76);
INSERT INTO road VALUES (3, 5, 252.56);
INSERT INTO road VALUES (3, 4, 54.88);
INSERT INTO road VALUES (6, 7, 4525.34);
INSERT INTO road VALUES (7, 8, 5818.52);
INSERT INTO road VALUES (8, 9, 4155.44);

INSERT INTO road VALUES (SELECT id2, id1, d FROM roads);

COMMIT;
