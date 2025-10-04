# pangeo-portainer-repo-spaceapps

Pangeo JupyterHub deployment for SpaceApps using Portainer.

## Overview

This repository contains the configuration files needed to deploy a Pangeo JupyterHub instance using Docker and Portainer. Pangeo is a community platform for Big Data geoscience, providing JupyterHub with pre-configured scientific Python packages for data analysis.

## Structure

```
Pantalaimon/SpaceApps/
├── docker-compose.yml          # Docker Compose configuration
└── hub/
    ├── Dockerfile              # JupyterHub container image
    └── jupyterhub_config.py    # JupyterHub configuration
```

## Deployment with Portainer

1. In Portainer, navigate to **Stacks** → **Add stack**
2. Choose **Repository** as the build method
3. Enter the repository URL: `https://github.com/Ovewh/pangeo-portainer-repo-spaceapps`
4. Set the **Compose path** to: `Pantalaimon/SpaceApps/docker-compose.yml`
5. Add the following environment variables:
   - `COMPOSE_PROJECT_NAME`: `pangeo-spaceapps` (or your preferred name)
   - `JUPYTERHUB_CRYPT_KEY`: Generate using `openssl rand -hex 32`
6. Click **Deploy the stack**

## Manual Deployment

If deploying manually with Docker Compose:

```bash
cd Pantalaimon/SpaceApps/

# Generate a cryptographic key for JupyterHub
export JUPYTERHUB_CRYPT_KEY=$(openssl rand -hex 32)
export COMPOSE_PROJECT_NAME=pangeo-spaceapps

# Start the services
docker-compose up -d
```

## Accessing JupyterHub

Once deployed, access JupyterHub at:
- URL: `http://your-server:8000`
- Default admin user: `admin` (create this user on first signup)

## Features

- **Pangeo Notebook Environment**: Pre-configured with scientific Python packages (xarray, dask, pandas, etc.)
- **Docker Spawner**: Each user gets their own containerized notebook environment
- **Persistent Storage**: User data is stored in Docker volumes
- **Native Authentication**: Built-in user management with signup capability
- **Idle Culler**: Automatically stops idle notebook servers after 1 hour

## Configuration

Edit `hub/jupyterhub_config.py` to customize:
- Admin users
- Notebook image version
- Resource limits
- Authentication settings
- Idle timeout settings

## Requirements

- Docker Engine 20.10+
- Docker Compose 2.0+ or Portainer
- At least 2GB RAM recommended

## License

This project is open source and available under the MIT License.