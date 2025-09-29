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

### 1. Install PostgreSQL

```bash
sudo apt update
sudo apt install -y postgresql
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

### 2. Create a PostgreSQL User for Odoo

```bash
sudo su - postgres -c "createuser -s odoo"
```

### 3. Clone the Odoo Repository

This repository contains the Odoo source code along with the `custom_helpdesk` module.

```bash
git clone https://github.com/kaljuvee/odoo.git /home/ubuntu/odoo-setup/odoo
cd /home/ubuntu/odoo-setup/odoo
```

### 4. Install Dependencies

Install the required Python packages for Odoo:

```bash
pip3 install -r requirements.txt
```

Install `wkhtmltopdf` for printing PDF reports:

```bash
sudo apt install -y wkhtmltopdf
```

### 5. Initialize the Odoo Database

Create the database and initialize it with the base Odoo modules and the custom helpdesk module:

```bash
createdb odoo_helpdesk
python3 odoo-bin --addons-path=addons -d odoo_helpdesk --init=custom_helpdesk --stop-after-init
```

### 6. Start the Odoo Server

Run the following command to start the Odoo server:

```bash
python3 odoo-bin --addons-path=addons -d odoo_helpdesk
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

## License

This project is licensed under the LGPL-3 License. See the `LICENSE` file for more details.

