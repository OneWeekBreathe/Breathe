# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.166.1/containers/python-3/.devcontainer/base.Dockerfile

# [Choice] Python version: 3, 3.9, 3.8, 3.7, 3.6
ARG VARIANT="3.8"
FROM mcr.microsoft.com/vscode/devcontainers/python:dev-${VARIANT}-buster

# This will be set to true when running in VSCode
ARG INTERACTIVE="false"

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Set up non-root user
COPY .devcontainer/scripts/non-root-user.sh /tmp/
RUN bash /tmp/non-root-user.sh "${USERNAME}" "${USER_UID}" "${USER_GID}"

# Set env for tracking that we're running in a devcontainer
ENV DEVCONTAINER=true

ARG DOCKER_GROUP_ID
COPY .devcontainer/scripts/docker-client.sh /tmp/
RUN /tmp/docker-client.sh $USERNAME

# Install Docker
RUN apt-get update && sudo apt-get install -y apt-transport-https ca-certificates curl gnupg lsb-release \
    && curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg \
    && echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" \
    | tee /etc/apt/sources.list.d/docker.list > /dev/null \
    && apt-get update && apt-get install -y docker-ce docker-ce-cli containerd.io \
    && apt-get clean -y && rm -rf /var/lib/apt/lists/*

ENV PATH ${PORTER_HOME}:$PATH

# Install requirements
COPY ["api/requirements.txt", "/tmp/pip-tmp/" ]
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt && rm -rf /tmp/pip-tmp

USER $USERNAME

# Save command line history
RUN echo "export HISTFILE=$HOME/commandhistory/.bash_history" >> "$HOME/.bashrc" \
    && echo "export PROMPT_COMMAND='history -a'" >> "$HOME/.bashrc" \
    && mkdir -p $HOME/commandhistory \
    && touch $HOME/commandhistory/.bash_history
