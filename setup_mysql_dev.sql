-- SETUP DEVELOPMENT DB

-- Creates the development db if not exists
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Creates development user
CREATE USER IF NOT EXISTS hbnb_dev@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Set dev user privileges on dev DB
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO hbnb_dev@'localhost';

-- Set SELECT privilege on performance_schema
GRANT SELECT ON performance_schema.* TO hbnb_dev@'localhost';

-- Reload privileges
FLUSH PRIVILEGES;
