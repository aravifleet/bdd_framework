
FROM jenkins/jenkins:lts

USER root

RUN apt-get update \
    && apt-get install -y python3 python3-pip python3-venv \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install --break-system-packages playwright==1.62.0 \
    && python3 -m playwright install-deps

USER jenkins
