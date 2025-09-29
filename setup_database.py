#!/usr/bin/env python3
"""
Odoo Database Setup Script for Remote PostgreSQL
This script sets up the Odoo database on a remote PostgreSQL server.
"""

import os
import sys
import psycopg2
from urllib.parse import urlparse

# Database connection details
DATABASE_URL = "postgresql://mmg_golive_user:8djDD6dvpudjEoTN9Pga7f3YyTpbeEvC@dpg-d2ebacvdiees73flvqhg-a.frankfurt-postgres.render.com/mmg_golive_f4ch_zn6i_p6yr"
ODOO_DB_NAME = "odoo_helpdesk"

def parse_database_url(url):
    """Parse the database URL and return connection parameters."""
    parsed = urlparse(url)
    return {
        'host': parsed.hostname,
        'port': parsed.port or 5432,
        'user': parsed.username,
        'password': parsed.password,
        'database': parsed.path[1:]  # Remove leading slash
    }

def check_database_connection():
    """Test the database connection."""
    try:
        conn_params = parse_database_url(DATABASE_URL)
        conn = psycopg2.connect(**conn_params)
        cursor = conn.cursor()
        cursor.execute("SELECT version();")
        version = cursor.fetchone()
        print(f"✅ Database connection successful!")
        print(f"PostgreSQL version: {version[0]}")
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        return False

def create_odoo_database():
    """Create the Odoo database if it doesn't exist."""
    try:
        conn_params = parse_database_url(DATABASE_URL)
        # Connect to the default database to create new one
        conn = psycopg2.connect(**conn_params)
        conn.autocommit = True
        cursor = conn.cursor()
        
        # Check if database exists
        cursor.execute("SELECT 1 FROM pg_database WHERE datname = %s", (ODOO_DB_NAME,))
        exists = cursor.fetchone()
        
        if not exists:
            cursor.execute(f'CREATE DATABASE "{ODOO_DB_NAME}"')
            print(f"✅ Created database: {ODOO_DB_NAME}")
        else:
            print(f"ℹ️  Database {ODOO_DB_NAME} already exists")
        
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        print(f"❌ Failed to create database: {e}")
        return False

def main():
    """Main setup function."""
    print("🚀 Starting Odoo Database Setup...")
    print(f"Target database: {ODOO_DB_NAME}")
    print(f"Remote PostgreSQL server: {parse_database_url(DATABASE_URL)['host']}")
    print()
    
    # Test connection
    if not check_database_connection():
        sys.exit(1)
    
    # Create Odoo database
    if not create_odoo_database():
        sys.exit(1)
    
    print()
    print("✅ Database setup completed successfully!")
    print()
    print("Next steps:")
    print("1. Clone Odoo: git clone https://github.com/odoo/odoo.git --depth 1 --branch 17.0")
    print("2. Copy module: cp -r custom_helpdesk odoo/addons/")
    print("3. Initialize: cd odoo && python3 odoo-bin -c ../odoo.conf --init=custom_helpdesk --stop-after-init")
    print("4. Start server: python3 odoo-bin -c ../odoo.conf")

if __name__ == "__main__":
    main()
