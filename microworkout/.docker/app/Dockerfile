FROM rudodeveloper/python:3.12.0


RUN mkdir -p /code/
WORKDIR /code/
ADD . /code/

# Access tokens to authorize the repo installation
ARG COMMONS_ACCESS_TOKEN
ARG CHATBOT_ACCESS_TOKEN
ARG FCM_ACCESS_TOKEN

# Poetry configuration to allow repositories installation using a repo-level access token
RUN poetry config repositories.commons-package https://rudoapps@bitbucket.org/rudoapps/gula-python-common.git && \
    poetry config http-basic.commons-package x-token-auth ${COMMONS_ACCESS_TOKEN} && \
    poetry config repositories.chatbot-package https://rudoapps@bitbucket.org/rudoapps/chat-ia-python.git && \
    poetry config http-basic.chatbot-package x-token-auth ${CHATBOT_ACCESS_TOKEN} && \
    poetry config repositories.fcm-package https://rudoapps@bitbucket.org/rudoapps/gula-python-notifications.git && \
    poetry config http-basic.fcm-package x-token-auth ${FCM_ACCESS_TOKEN}

# Allows poetry to install packages right to the system
RUN poetry config virtualenvs.create false && \
    poetry install --no-root

EXPOSE 8000
