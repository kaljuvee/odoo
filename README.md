# Odoo with Custom Helpdesk Module

This project provides a customized Odoo installation featuring a simple, on-premise helpdesk solution built using the Odoo Community Edition. This document outlines the setup, configuration, and usage of this custom helpdesk module.

## Features

The custom helpdesk module includes the following features:

*   **Ticket Management:** Create, manage, and track support tickets.
*   **Team Organization:** Assign tickets to specific teams and users.
*   **Ticket Prioritization:** Set ticket priority (Low, Normal, High, Urgent).
*   **Customizable Stages:** Define and manage ticket stages (e.g., New, In Progress, Solved).
*   **Tagging System:** Categorize tickets using customizable tags.
*   **Customer Portal:** Allow customers to view their tickets and interact with support agents.
*   **Email Integration:** Send and receive ticket updates via email.
*   **Reporting:** Basic reporting and analytics on ticket volume and performance.

## Installation

Follow these steps to set up the Odoo environment and install the custom helpdesk module.

### Prerequisites

*   Ubuntu 22.04 LTS
*   PostgreSQL
*   Python 3.11
*   Git

### 1. Database Setup

This project supports both local and remote PostgreSQL databases.

#### Option A: Remote PostgreSQL (Recommended for Production)

If you have a remote PostgreSQL database (like Render, AWS RDS, etc.), update the `odoo.conf` file with your database credentials:

```bash
# Edit odoo.conf with your database details
db_host = your-postgres-host.com
db_port = 5432
db_user = your_username
db_password = your_password
```

Then run the database setup script:

```bash
python3 setup_database.py
```

#### Option B: Local PostgreSQL (Development)

```bash
sudo apt update
sudo apt install -y postgresql postgresql-contrib
sudo systemctl start postgresql
sudo systemctl enable postgresql
sudo su - postgres -c "createuser -s $USER"
```

### 3. Clone the Odoo Repository

This repository contains the Odoo source code along with the `custom_helpdesk` module.

```bash
git clone https://github.com/kaljuvee/odoo.git /home/ubuntu/odoo-setup/odoo
cd /home/ubuntu/odoo-setup/odoo
```

### 4. Install Python Dependencies

Install the required Python packages using the requirements file:

```bash
pip3 install -r requirements.txt
```

### 5. Install System Dependencies

Install `wkhtmltopdf` for PDF generation and PostgreSQL development headers:

```bash
sudo apt update
sudo apt install -y wkhtmltopdf postgresql postgresql-contrib
```

### 6. Initialize the Odoo Database

Copy the custom helpdesk module and initialize the database:

```bash
cp -r custom_helpdesk odoo/addons/
cd odoo
python3 odoo-bin -c ../odoo.conf --init=custom_helpdesk --stop-after-init
```

### 7. Start the Odoo Server

Run the following command to start the Odoo server:

```bash
python3 odoo-bin -c ../odoo.conf
```

The server will be accessible at `http://localhost:8069`.

## Configuration

After installation, you can configure the helpdesk module from the Odoo interface.

1.  **Log in to Odoo:** Use the default credentials (admin/admin) to log in.
2.  **Navigate to Helpdesk:** Click on the "Helpdesk" menu icon in the main dashboard.
3.  **Configure Teams, Stages, and Tags:**
    *   Go to **Helpdesk > Configuration > Teams** to create and manage support teams.
    *   Go to **Helpdesk > Configuration > Stages** to define the ticket workflow stages.
    *   Go to **Helpdesk > Configuration > Tags** to create tags for categorizing tickets.

## Usage

### Creating a Ticket

*   Navigate to **Helpdesk > Tickets > All Tickets**.
*   Click the "Create" button.
*   Fill in the ticket details, including the customer, subject, description, team, and priority.

### Managing Tickets

*   Use the Kanban view to drag and drop tickets between stages.
*   Assign tickets to specific users within a team.
*   Use the chatter to communicate with customers and internal team members.

### Customer Portal

*   Customers can log in to the portal to view the status of their tickets.
*   They can also create new tickets and communicate with support agents through the portal.

## Deployment to GitHub

To push this project to your GitHub repository, follow these steps:

1.  **Initialize a new Git repository (if you haven't already):**

    ```bash
    git init
    ```

2.  **Add the remote repository:**

    ```bash
    git remote add origin https://github.com/kaljuvee/odoo.git
    ```

3.  **Stage all files:**

    ```bash
    git add .
    ```

4.  **Commit the changes:**

    ```bash
    git commit -m "Initial commit with Odoo and custom helpdesk module"
    ```

5.  **Push to the repository:**

    ```bash
    git push -u origin main
    ```

    You will be prompted for your GitHub username and password (or a personal access token).

## 🚀 Quick Deploy on Render

For instant deployment on Render:

1. **Fork this repository** to your GitHub account
2. **Connect to Render** and create a new Web Service
3. **Set Environment Variables**:
   ```
   DB_HOST=your-postgres-host
   DB_USER=your-username
   DB_PASSWORD=your-password
   DB_NAME=odoo_helpdesk
   ```
4. **Deploy** with these settings:
   - **Build Command**: `./build.sh`
   - **Start Command**: `./start.sh`

See [README_RENDER.md](README_RENDER.md) for detailed deployment instructions.

## License

This project is licensed under the LGPL-3 License. See the `LICENSE` file for more details.

