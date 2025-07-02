CREATE TABLE legislation (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    type VARCHAR(50) NOT NULL,
    status VARCHAR(50) NOT NULL,
    introduced_date DATE,
    passed_date DATE,
    summary TEXT,
    document_url TEXT
);
