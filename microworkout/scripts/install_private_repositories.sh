#!/bin/bash

# gula-python-common
poetry config repositories.commons-package https://rudoapps@bitbucket.org/rudoapps/gula-python-common.git
poetry config http-basic.commons-package x-token-auth ${COMMONS_ACCESS_TOKEN}
poetry add git+https://bitbucket.org/rudoapps/gula-python-common.git

# chat-ia-python
# poetry config repositories.chatbot-package https://rudoapps@bitbucket.org/rudoapps/chat-ia-python.git
# poetry config http-basic.chatbot-package x-token-auth ${CHATBOT_ACCESS_TOKEN}
# poetry add git+https://bitbucket.org/rudoapps/chat-ia-python.git#develop

# gula-python-notifications
# poetry config repositories.fcm-package https://rudoapps@bitbucket.org/rudoapps/gula-python-notifications.git
# poetry config http-basic.fcm-package x-token-auth ${FCM_ACCESS_TOKEN}
# poetry add git+https://bitbucket.org/rudoapps/gula-python-notifications.git#develop
