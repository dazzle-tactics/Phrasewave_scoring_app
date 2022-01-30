DROP TABLE IF EXISTS contestants;
DROP TABLE IF EXISTS teams;

CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    name VARCHAR (50),
    points FLOAT
);

CREATE TABLE contestants(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    occupation VARCHAR(50),
    fave_phrase VARCHAR(255),
    team_id INT REFERENCES teams(id)
);