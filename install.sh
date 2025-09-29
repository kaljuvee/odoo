#!/bin/bash

# Odoo Custom Helpdesk Installation Script
# This script installs Odoo Community Edition with the custom helpdesk module

set -e

echo "=== Odoo Custom Helpdesk Installation Script ==="
echo "This script will install Odoo Community Edition with a custom helpdesk module"
echo ""

# Check if running as root
if [[ $EUID -eq 0 ]]; then
   echo "This script should not be run as root for security reasons."
   echo "Please run as a regular user with sudo privileges."
   exit 1
fi

# Update system packages
echo "Updating system packages..."
sudo apt update

# Install PostgreSQL
echo "Installing PostgreSQL..."
sudo apt install -y postgresql postgresql-contrib

# Start and enable PostgreSQL
sudo systemctl start postgresql
sudo systemctl enable postgresql

# Create PostgreSQL user for Odoo
echo "Creating PostgreSQL user for Odoo..."
sudo su - postgres -c "createuser -s $USER" 2>/dev/null || echo "User already exists"

# Install Python dependencies
echo "Installing Python dependencies..."
sudo apt install -y python3-pip python3-dev python3-venv libxml2-dev libxslt1-dev libevent-dev libsasl2-dev libldap2-dev pkg-config libtiff5-dev libjpeg8-dev libopenjp2-7-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev libharfbuzz-dev libfribidi-dev libxcb1-dev

# Install wkhtmltopdf for PDF generation
echo "Installing wkhtmltopdf..."
sudo apt install -y wkhtmltopdf

# Clone Odoo repository
echo "Cloning Odoo repository..."
if [ ! -d "odoo" ]; then
    git clone https://github.com/odoo/odoo.git --depth 1 --branch 17.0
fi

cd odoo

# Install Python requirements
echo "Installing Python requirements..."
pip3 install -r requirements.txt

# Copy custom helpdesk module
echo "Installing custom helpdesk module..."
cp -r ../custom_helpdesk addons/

# Create database
echo "Creating Odoo database..."
createdb odoo_helpdesk 2>/dev/null || echo "Database already exists"

# Initialize database with custom helpdesk module
echo "Initializing database with custom helpdesk module..."
python3 odoo-bin --addons-path=addons -d odoo_helpdesk --init=custom_helpdesk --stop-after-init

echo ""
echo "=== Installation Complete! ==="
echo ""
echo "To start Odoo server, run:"
echo "cd odoo && python3 odoo-bin --addons-path=addons -d odoo_helpdesk"
echo ""
echo "Then open your browser and go to: http://localhost:8069"
echo "Default login: admin / admin"
echo ""
echo "The custom helpdesk module will be available in the main menu."
