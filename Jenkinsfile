
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'GitHub checkout successful!'
            }
        }

        stage('Verify Workspace') {
            steps {
                sh 'git --version'
                sh 'ls -la'
                sh 'python3 --version'
            }
        }

        stage('Run BDD Tests') {
            steps {
                echo 'BDD tests are passing locally; configuring Jenkins test execution next.'
            }
        }
    }
}
