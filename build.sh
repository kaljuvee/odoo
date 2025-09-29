#!/bin/bash
# Render Build Script for Odoo Custom Helpdesk

set -e

echo "🚀 Starting Odoo Helpdesk build process..."

# Install system dependencies
echo "📦 Installing system dependencies..."
apt-get update
apt-get install -y wkhtmltopdf git

# Install Python dependencies
echo "🐍 Installing Python dependencies..."
pip install -r requirements.txt

# Clone Odoo Community Edition
echo "📥 Downloading Odoo Community Edition..."
if [ ! -d "odoo" ]; then
    git clone https://github.com/odoo/odoo.git --depth 1 --branch 17.0
fi

# Copy custom helpdesk module
echo "📋 Installing custom helpdesk module..."
cp -r custom_helpdesk odoo/addons/

# Create filestore directory
mkdir -p filestore

echo "✅ Build completed successfully!"
echo "Ready for deployment..."
