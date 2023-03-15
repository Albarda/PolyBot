pipeline {
    agent any

    stages {
        stage('Unittest') {
            steps {
                sh 'pip install python-telegram-bot'

                sh 'python3 -m pytest --junitxml results.xml tests/*.py'
            }
        }
        stage('Functional test') {
            steps {
                echo "testing"
            }
        }
    }
post {
    always {
        junit allowEmptyResults: true, testResults: 'results.xml'
    }
}

    
}
