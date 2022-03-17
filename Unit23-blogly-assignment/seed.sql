DROP DATABASE IF EXISTS blogly;

CREATE DATABASE blogly;

\c blogly;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name = TEXT NOT NULL,
    last_name = VARCHAR(50)
    image_url = TEXT NOT NULL DEFAULT('/default-profile-pic')
);