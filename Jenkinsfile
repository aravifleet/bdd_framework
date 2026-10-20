
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'GitHub checkout successful!'
            }
        }

        stage('Verify Environment') {
            steps {
                sh 'git --version'
                sh 'python3 --version'
                sh 'echo "Browser path: $PLAYWRIGHT_BROWSERS_PATH"'
                sh 'ls -la "$PLAYWRIGHT_BROWSERS_PATH"'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv .venv'
                sh '.venv/bin/python -m pip install --upgrade pip'
                sh '.venv/bin/python -m pip install -r requirements.txt'
            }
        }

        stage('Discover Tests') {
            steps {
                sh '.venv/bin/python -m pytest --collect-only -q'
            }
        }
    }
}
