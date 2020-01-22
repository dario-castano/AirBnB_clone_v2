-- SETUP DEVELOPMENT DB

-- Allow remote root (DANGEROUS)
UPDATE mysql.user SET host='%' WHERE user='root';

-- Creates the development db if not exists
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Creates development user
CREATE USER IF NOT EXISTS hbnb_dev@'%' IDENTIFIED BY 'hbnb_dev_pwd';
CREATE USER IF NOT EXISTS hbnb_dev@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
CREATE USER IF NOT EXISTS hbnb_dev@'10.0.2.2' IDENTIFIED BY 'hbnb_dev_pwd';
CREATE USER IF NOT EXISTS hbnb_dev@'' IDENTIFIED BY 'hbnb_dev_pwd';

-- Set dev user privileges on dev DB
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO hbnb_dev@'%';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO hbnb_dev@'localhost';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO hbnb_dev@'10.0.2.2';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO hbnb_dev@'';

-- Set SELECT privilege on performance_schema
GRANT SELECT ON performance_schema.* TO hbnb_dev@'%';
GRANT SELECT ON performance_schema.* TO hbnb_dev@'localhost';
GRANT SELECT ON performance_schema.* TO hbnb_dev@'10.0.2.2';
GRANT SELECT ON performance_schema.* TO hbnb_dev@'';

-- Reload privileges
FLUSH PRIVILEGES;
