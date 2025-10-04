import os

# JupyterHub configuration for Pangeo

# Network configuration
c.JupyterHub.hub_ip = '0.0.0.0'
c.JupyterHub.port = 8000

# Use DockerSpawner to spawn user notebooks
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'

# Docker network name
c.DockerSpawner.network_name = os.environ.get('DOCKER_NETWORK_NAME', 'bridge')

# Use the Pangeo notebook image for user notebooks
c.DockerSpawner.image = 'pangeo/pangeo-notebook:latest'

# Remove containers when they are stopped
c.DockerSpawner.remove = True

# Mount volumes for persistent user data
c.DockerSpawner.volumes = {
    'jupyterhub-user-{username}': '/home/jovyan/work'
}

# Set environment variables for user notebooks
c.DockerSpawner.environment = {
    'GRANT_SUDO': 'yes',
}

# Admin users - add usernames here
c.Authenticator.admin_users = {'admin'}

# Use NativeAuthenticator for local user management
c.JupyterHub.authenticator_class = 'nativeauthenticator.NativeAuthenticator'

# Allow users to sign up
c.NativeAuthenticator.open_signup = True

# Require admin approval for new users (set to False for open signup)
c.NativeAuthenticator.ask_email_on_signup = True

# Minimum password length
c.NativeAuthenticator.minimum_password_length = 8

# Services - for admin panel
c.JupyterHub.load_roles = [
    {
        'name': 'user',
        'scopes': ['self'],
    },
]

# Shutdown idle servers after this many seconds (1 hour)
c.JupyterHub.services = [
    {
        'name': 'idle-culler',
        'admin': True,
        'command': [
            'python3', '-m', 'jupyterhub_idle_culler',
            '--timeout=3600'
        ],
    }
]

# Cookie secret for security
c.JupyterHub.cookie_secret_file = '/srv/jupyterhub/jupyterhub_cookie_secret'

# Database configuration
c.JupyterHub.db_url = 'sqlite:////srv/jupyterhub/jupyterhub.sqlite'

# Logging
c.JupyterHub.log_level = 'INFO'
c.Spawner.debug = True
