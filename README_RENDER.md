# Deploy Odoo Custom Helpdesk on Render

This guide shows you how to deploy the Odoo Custom Helpdesk module on Render with just a few clicks.

## 🚀 One-Click Render Deployment

### Method 1: Using Render Dashboard

1. **Fork this repository** to your GitHub account
2. **Connect to Render**:
   - Go to [Render Dashboard](https://dashboard.render.com)
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
3. **Configure the service**:
   - **Name**: `odoo-helpdesk`
   - **Runtime**: `Python 3`
   - **Build Command**: `./build.sh`
   - **Start Command**: `./start.sh`
4. **Set Environment Variables**:
   ```
   DB_HOST=dpg-d2ebacvdiees73flvqhg-a.frankfurt-postgres.render.com
   DB_PORT=5432
   DB_USER=mmg_golive_user
   DB_PASSWORD=8djDD6dvpudjEoTN9Pga7f3YyTpbeEvC
   DB_NAME=odoo_helpdesk
   PYTHONUNBUFFERED=1
   ```
5. **Deploy**: Click "Create Web Service"

### Method 2: Using render.yaml (Recommended)

1. **Fork this repository**
2. **Deploy with render.yaml**:
   - The `render.yaml` file contains all configuration
   - Render will automatically detect and use it
   - Just connect your repository and deploy!

### Method 3: Using Python Main Script

If you prefer a pure Python approach:

1. **Set Start Command to**: `python3 main.py`
2. **Set Build Command to**: `pip install -r requirements.txt`
3. **Add the same environment variables as above**

## 🔧 Environment Variables

The following environment variables are required:

| Variable | Value | Description |
|----------|-------|-------------|
| `DB_HOST` | `dpg-d2ebacvdiees73flvqhg-a.frankfurt-postgres.render.com` | PostgreSQL host |
| `DB_PORT` | `5432` | PostgreSQL port |
| `DB_USER` | `mmg_golive_user` | Database username |
| `DB_PASSWORD` | `8djDD6dvpudjEoTN9Pga7f3YyTpbeEvC` | Database password |
| `DB_NAME` | `odoo_helpdesk` | Database name |
| `PYTHONUNBUFFERED` | `1` | Python output buffering |

## 📋 What Happens During Deployment

1. **Build Phase** (`build.sh`):
   - Installs system dependencies (wkhtmltopdf, git)
   - Installs Python dependencies from requirements.txt
   - Downloads Odoo Community Edition
   - Copies custom helpdesk module to Odoo addons

2. **Start Phase** (`start.sh` or `main.py`):
   - Checks if database is initialized
   - Initializes database with custom helpdesk module (if needed)
   - Starts Odoo server with proper configuration

## 🌐 Access Your Application

After deployment:
- Your Odoo instance will be available at your Render URL
- Login with: `admin` / `admin`
- Navigate to the Helpdesk menu to start using the system

## 🔍 Troubleshooting

### Common Issues

1. **Build Fails**: Check that all environment variables are set correctly
2. **Database Connection**: Verify database credentials and network access
3. **Module Not Found**: Ensure the custom_helpdesk module is properly copied

### Logs

Check Render logs for detailed error messages:
- Go to your service dashboard
- Click on "Logs" tab
- Look for error messages during build or runtime

### Health Check

The application includes a health check endpoint at `/web/health`

## 🔒 Security Notes

- Change the default admin password after first login
- Consider using environment variables for sensitive data
- Enable HTTPS in production (Render provides this automatically)

## 📞 Support

For deployment issues:
1. Check the Render logs
2. Verify environment variables
3. Ensure database connectivity
4. Review the build and start scripts

The deployment is designed to be fully automated - just set the environment variables and deploy!
