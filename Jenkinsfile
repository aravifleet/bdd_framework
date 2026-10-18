
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'GitHub checkout successful!'
            }
        }

        stage('Install Python') {
            steps {
                sh '''
                    apt-get update
                    apt-get install -y python3 python3-pip python3-venv
                    python3 --version
                '''
            }
        }
    }
}
