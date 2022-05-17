# [Choice] Python version: 3, 3.9, 3.8, 3.7, 3.6
ARG VARIANT="3.8"
FROM mcr.microsoft.com/vscode/devcontainers/python:dev-${VARIANT}-buster

# Install requirements
COPY ["api/requirements.txt", "/tmp/pip-tmp/" ]
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt && rm -rf /tmp/pip-tmp

#install node
# [Choice] Node.js version: none, lts/*, 16, 14, 12, 10
RUN su vscode -c "umask 0002 && . /usr/local/share/nvm/nvm.sh && nvm install lts/*"

# Save command line history
RUN echo "export HISTFILE=$HOME/commandhistory/.bash_history" >> "$HOME/.bashrc" \
    && echo "export PROMPT_COMMAND='history -a'" >> "$HOME/.bashrc" \
    && mkdir -p $HOME/commandhistory \
    && touch $HOME/commandhistory/.bash_history
