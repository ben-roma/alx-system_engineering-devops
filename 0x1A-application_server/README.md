# 0x1A. Application Server

## Project Overview

This project is part of the ALX Africa curriculum, focusing on the setup and configuration of an application server. The main goal is to deploy web applications on a production environment using best practices.

## Tasks

### Task 0: Set up Development Environment

- **Objective**: Prepare a development environment that mirrors the production setup.
- **Tools**: Vagrant, Ubuntu, and necessary dependencies.
- **Outcome**: A fully functional development environment where the application can be developed and tested before deployment.

### Task 1: Configure Application Server

- **Objective**: Configure the application server to serve web applications.
- **Steps**:
  - Install and configure Nginx.
  - Set up Gunicorn to serve the Python application.
  - Adjust firewall settings to allow traffic on the necessary ports.
  - Test the setup to ensure that the application is accessible via the web.

### Task 2: Automate Server Setup

- **Objective**: Create scripts to automate the setup process for the application server.
- **Tools**: Shell scripting, Puppet, or Ansible.
- **Outcome**: Scripts that can quickly set up an application server, ensuring consistency across different environments.

### Task 3: Deploy a Web Application

- **Objective**: Deploy a sample web application to the server.
- **Steps**:
  - Push the application code to the server.
  - Configure Nginx and Gunicorn to serve the application.
  - Ensure the application is running and accessible from the web.

## Usage

To set up the application server and deploy the application, follow these steps:

1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/0x1A-application-server.git

2. Navigate to the project directory:
   ```sh
cd 0x1A-application-server

3. Run the setup script:
   ```sh
./setup_server.sh

4. Deploy the application:
   ```sh
./deploy_application.sh
