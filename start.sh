#!/bin/bash
# Render Start Script for Odoo Custom Helpdesk

set -e

echo "🚀 Starting Odoo Helpdesk server..."

# Change to odoo directory
cd odoo

# Check if database needs initialization
echo "🔍 Checking database status..."
python3 -c "
import psycopg2
import sys
try:
    conn = psycopg2.connect(
        host='$DB_HOST',
        port='$DB_PORT',
        user='$DB_USER',
        password='$DB_PASSWORD',
        database='$DB_NAME'
    )
    cur = conn.cursor()
    cur.execute(\"SELECT 1 FROM information_schema.tables WHERE table_name='ir_module_module'\")
    if cur.fetchone():
        print('Database already initialized')
        sys.exit(0)
    else:
        print('Database needs initialization')
        sys.exit(1)
    conn.close()
except:
    print('Database needs initialization')
    sys.exit(1)
"

# Initialize database if needed
if [ $? -eq 1 ]; then
    echo "🔧 Initializing database with custom helpdesk module..."
    python3 odoo-bin \
        --db_host="$DB_HOST" \
        --db_port="$DB_PORT" \
        --db_user="$DB_USER" \
        --db_password="$DB_PASSWORD" \
        --database="$DB_NAME" \
        --addons-path=addons \
        --init=custom_helpdesk \
        --stop-after-init \
        --without-demo=False
fi

echo "🌟 Starting Odoo server..."
exec python3 odoo-bin \
    --db_host="$DB_HOST" \
    --db_port="$DB_PORT" \
    --db_user="$DB_USER" \
    --db_password="$DB_PASSWORD" \
    --database="$DB_NAME" \
    --addons-path=addons \
    --xmlrpc-port="$PORT" \
    --xmlrpc-interface=0.0.0.0 \
    --workers=1 \
    --max-cron-threads=1 \
    --log-level=info
