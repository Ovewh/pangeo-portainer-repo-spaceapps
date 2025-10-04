FROM jupyterhub/jupyterhub:latest

# Install dockerspawner for spawning user notebooks in Docker containers
RUN pip install --no-cache-dir \
    dockerspawner \
    jupyterhub-nativeauthenticator \
    oauthenticator
# Start JupyterHub
CMD ["jupyterhub", "-f", "/srv/jupyterhub/jupyterhub_config.py"]

FROM pangeo/ml-notebook:091714e

# Install JupyterHub and dependencies
RUN mamba install -y -c conda-forge \
    jupyterhub \
    dockerspawner \
    jupyterhub-nativeauthenticator \
    oauthenticator && \
    mamba clean --all

# Copy your JupyterHub config
COPY jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py

WORKDIR /srv/jupyterhub
EXPOSE 8000
CMD ["jupyterhub", "-f", "/srv/jupyterhub/jupyterhub_config.py"]
