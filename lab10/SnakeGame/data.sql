CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE user_scores (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    score INT NOT NULL,
    level INT NOT NULL,
    saved_state BYTEA,  -- optional: to store game state
    created_at TIMESTAMP DEFAULT NOW()
);

