# Project Explanation

## IMPORTANT:

Before executing the "make build" command, ensure to check the GID/UID of your user and update the corresponding variables in the /docker/.env file:

- **Get the UID:**
   ```bash
   id -u
   
- **Get the GID:**
   ```bash
   id -g

Additionally I recommend copying the project directory into the home folder of your user before initializing the app to avoid other permission errors.

## 1. Docker

This directory houses the infrastructure files essential for setting up the containers required to run the Django web application.

- **docker-compose.yml:**
  - The central file defining and orchestrating all the containers necessary for the smooth operation of the Django application.

- **requirements.txt:**
  - A concise list of Python packages crucial for running the Django application seamlessly.

- **blogyourstuff:**
  - Inside this directory, you'll find the Dockerfile and the entrypoint.sh script for our Django container. These components facilitate pre-initialization operations, such as uploading sample data or creating a superuser. Check out `entrypoint.sh` for more insights into Django operations.

- **persistent:**
  - This folder is created (if not already present) during the execution of the `make` command. It contains all the persistent files associated with our database.

- **.env:**
  - This file serves as the cornerstone of configuration, housing the environment variables that govern the behavior and operation of our system.
    There is also a sample env file but this is not the one in use. The main env file is in hidden mode because of the dot "." at the beggining of the filename.

## 2. BlogYourStuff

This folder encapsulates all the files pertinent to our Django web application. These files are linked to our Python container, where the application is executed.

- **Project Organization:**
  - The project is thoughtfully organized into two services: `accounts` and `blog`.

- **accounts:**
  - Within this module, you'll discover all the components required to manage user accounts effectively.

- **blog:**
  - This module encompasses all the necessary elements to power the blog section of our web application.



# Requirements

To successfully deploy and run this web application, ensure that your system meets the following prerequisites:

- **Docker Engine:**
  - Install Docker Engine on your system. You can download it from the [official Docker website](https://docs.docker.com/get-docker/).

- **Linux Operating System:**
  - This web application is designed to run on a Linux-based operating system. Ensure you have a compatible Linux distribution installed.

- **Network Connection:**
  - A stable internet connection is required for fetching dependencies, updates, and interacting with external services. Ensure your system is connected to the network.

- **Make Software:**
  - The `make` utility is used for automating build processes. Make sure it is installed on your system. You can typically install it using your system's package manager.

# Run the Django application

To start the application run the following command from the root directory of our project, where you can also find the Makefile:

```bash
make build
```

To restart the app:
```bash
make restart
```

To stop the containers:
```bash
make stop
```

Usually we would be able to find the application running into [localhost:8000](http://localhost:8000) if the environment variables were kept untouched.

# Features:

- User Authentication: Enables users to register, log in, and manage their accounts securely.
- CRUD Functionality: Allows users to create, read, update, and delete blog posts.
- Responsive Design: Ensures optimal viewing across various devices.

# Tech Stack:

- Backend: Django
- Frontend: Django Templates
- Deployment: Docker and Docker Compose


