
CREATE TABLE IF NOT EXISTS Sale (
    home_id INTEGER PRIMARY KEY AUTOINCREMENT,
    price INTEGER, 
    address TEXT, 
    beds INTEGER,
    baths INTEGER,
    size INTEGER,
    mortgage INTEGER, 
    agent_id INTEGER, 
    status TEXT  
);


CREATE TABLE IF NOT EXISTS Rent (
    home_id INTEGER PRIMARY KEY AUTOINCREMENT,
    rentprice INTEGER, 
    address TEXT, 
    beds INTEGER,
    baths INTEGER,
    size INTEGER,
    agent_id INTEGER, 
    status TEXT  
);


