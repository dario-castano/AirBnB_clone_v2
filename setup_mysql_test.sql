-- SETUP TESTING DB

-- Creates the testing db if not exists
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Creates testing user
CREATE USER IF NOT EXISTS hbnb_test@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Set test user privileges on test DB
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO hbnb_test@'localhost';

-- Set SELECT privilege on performance_schema
GRANT SELECT ON performance_schema.* TO hbnb_test@'localhost';

-- Reload privileges
FLUSH PRIVILEGES;
