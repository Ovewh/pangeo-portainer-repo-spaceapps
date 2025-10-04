FROM jupyterhub/jupyterhub:4.0

# Install dockerspawner for spawning user notebooks in Docker containers
RUN pip install --no-cache-dir \
    dockerspawner \
    jupyterhub-nativeauthenticator \
    oauthenticator

# Install Pangeo-specific packages
RUN pip install --no-cache-dir \
    dask-gateway \
    pangeo-notebook

# Copy the JupyterHub configuration
COPY jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py

# Set working directory
WORKDIR /srv/jupyterhub

# Expose JupyterHub port
EXPOSE 8000

# Start JupyterHub
CMD ["jupyterhub", "-f", "/srv/jupyterhub/jupyterhub_config.py"]
