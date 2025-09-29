#!/usr/bin/env python3
"""
Odoo Custom Helpdesk - Main Application Entry Point
Simplified deployment for Render and other Python hosting platforms
"""

import os
import sys
import subprocess
import psycopg2
from pathlib import Path

def setup_odoo():
    """Setup Odoo if not already done"""
    if not Path("odoo").exists():
        print("📥 Downloading Odoo Community Edition...")
        subprocess.run([
            "git", "clone", 
            "https://github.com/odoo/odoo.git", 
            "--depth", "1", 
            "--branch", "17.0"
        ], check=True)
        
        print("📋 Installing custom helpdesk module...")
        subprocess.run(["cp", "-r", "custom_helpdesk", "odoo/addons/"], check=True)

def check_database():
    """Check if database is initialized"""
    try:
        conn = psycopg2.connect(
            host=os.environ.get('DB_HOST'),
            port=os.environ.get('DB_PORT', 5432),
            user=os.environ.get('DB_USER'),
            password=os.environ.get('DB_PASSWORD'),
            database=os.environ.get('DB_NAME')
        )
        cur = conn.cursor()
        cur.execute("SELECT 1 FROM information_schema.tables WHERE table_name='ir_module_module'")
        result = cur.fetchone()
        conn.close()
        return result is not None
    except:
        return False

def initialize_database():
    """Initialize Odoo database with custom helpdesk module"""
    print("🔧 Initializing database with custom helpdesk module...")
    
    cmd = [
        "python3", "odoo/odoo-bin",
        f"--db_host={os.environ.get('DB_HOST')}",
        f"--db_port={os.environ.get('DB_PORT', 5432)}",
        f"--db_user={os.environ.get('DB_USER')}",
        f"--db_password={os.environ.get('DB_PASSWORD')}",
        f"--database={os.environ.get('DB_NAME')}",
        "--addons-path=odoo/addons",
        "--init=custom_helpdesk",
        "--stop-after-init",
        "--without-demo=False"
    ]
    
    subprocess.run(cmd, check=True)

def start_odoo():
    """Start Odoo server"""
    print("🌟 Starting Odoo server...")
    
    cmd = [
        "python3", "odoo/odoo-bin",
        f"--db_host={os.environ.get('DB_HOST')}",
        f"--db_port={os.environ.get('DB_PORT', 5432)}",
        f"--db_user={os.environ.get('DB_USER')}",
        f"--db_password={os.environ.get('DB_PASSWORD')}",
        f"--database={os.environ.get('DB_NAME')}",
        "--addons-path=odoo/addons",
        f"--xmlrpc-port={os.environ.get('PORT', 8069)}",
        "--xmlrpc-interface=0.0.0.0",
        "--workers=1",
        "--max-cron-threads=1",
        "--log-level=info"
    ]
    
    # Use exec to replace the current process
    os.execvp("python3", cmd)

def main():
    """Main application entry point"""
    print("🚀 Starting Odoo Custom Helpdesk...")
    
    # Setup Odoo if needed
    setup_odoo()
    
    # Check and initialize database if needed
    if not check_database():
        initialize_database()
    
    # Start Odoo server
    start_odoo()

if __name__ == "__main__":
    main()
