# Deployment Guide - Remote PostgreSQL

This guide explains how to deploy the Odoo Custom Helpdesk module with a remote PostgreSQL database.

## Remote Database Configuration

### Supported Database Providers

- **Render PostgreSQL**
- **AWS RDS PostgreSQL**
- **Google Cloud SQL**
- **Azure Database for PostgreSQL**
- **DigitalOcean Managed Databases**
- **Heroku Postgres**

### Database URL Format

The database connection string should follow this format:
```
postgresql://username:password@host:port/database_name
```

Example:
```
postgresql://mmg_golive_user:8djDD6dvpudjEoTN9Pga7f3YyTpbeEvC@dpg-d2ebacvdiees73flvqhg-a.frankfurt-postgres.render.com/mmg_golive_f4ch_zn6i_p6yr
```

## Quick Deployment Steps

### 1. Clone and Setup

```bash
# Clone the repository
git clone https://github.com/kaljuvee/odoo.git
cd odoo

# Install Python dependencies
pip3 install -r requirements.txt

# Install system dependencies
sudo apt update
sudo apt install -y wkhtmltopdf
```

### 2. Configure Database Connection

Edit the `odoo.conf` file with your database credentials:

```ini
[options]
db_host = your-database-host.com
db_port = 5432
db_user = your_username
db_password = your_password
db_name = odoo_helpdesk
```

### 3. Setup Database

Run the database setup script:

```bash
python3 setup_database.py
```

This script will:
- Test the database connection
- Create the Odoo database if it doesn't exist
- Provide next steps for initialization

### 4. Initialize Odoo

```bash
# Clone Odoo Community Edition
git clone https://github.com/odoo/odoo.git --depth 1 --branch 17.0

# Copy custom helpdesk module
cp -r custom_helpdesk odoo/addons/

# Initialize database with custom module
cd odoo
python3 odoo-bin -c ../odoo.conf --init=custom_helpdesk --stop-after-init
```

### 5. Start the Server

```bash
python3 odoo-bin -c ../odoo.conf
```

## Production Deployment

### Environment Variables

For production, use environment variables instead of hardcoded values:

```bash
export DB_HOST="your-host.com"
export DB_USER="your-username"
export DB_PASSWORD="your-password"
export DB_NAME="odoo_helpdesk"
```

### Security Considerations

1. **Database Security**
   - Use SSL connections for remote databases
   - Restrict database access by IP if possible
   - Use strong passwords and rotate them regularly

2. **Odoo Security**
   - Change the default admin password
   - Set a master password for database operations
   - Use HTTPS in production

3. **Network Security**
   - Configure firewall rules
   - Use VPN for database access if required
   - Monitor database connections

### Performance Optimization

1. **Database Optimization**
   - Use connection pooling
   - Configure appropriate database parameters
   - Monitor query performance

2. **Odoo Configuration**
   - Set appropriate worker processes
   - Configure memory limits
   - Use proxy server (nginx/apache) for static files

### Monitoring and Maintenance

1. **Database Monitoring**
   - Monitor connection counts
   - Track query performance
   - Set up alerts for high resource usage

2. **Application Monitoring**
   - Monitor Odoo logs
   - Track response times
   - Set up health checks

3. **Backup Strategy**
   - Regular database backups
   - Test backup restoration
   - Store backups securely

## Troubleshooting

### Common Issues

1. **Connection Timeout**
   - Check network connectivity
   - Verify firewall rules
   - Increase connection timeout in odoo.conf

2. **Authentication Failed**
   - Verify username and password
   - Check database user permissions
   - Ensure database exists

3. **SSL Connection Issues**
   - Add `sslmode=require` to connection string
   - Verify SSL certificate validity

### Debug Mode

Enable debug mode for troubleshooting:

```bash
python3 odoo-bin -c ../odoo.conf --log-level=debug
```

### Database Connection Test

Use the setup script to test connectivity:

```bash
python3 setup_database.py
```

## Support

For deployment issues:
1. Check the logs for error messages
2. Verify database connectivity
3. Ensure all dependencies are installed
4. Review the configuration file syntax

For production deployments, consider consulting with a DevOps specialist or Odoo implementation partner.
