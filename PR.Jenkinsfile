pipeline {
    agent any

    stages {
        stage('Unittest') {
            steps {
                sh 'python3 -m pytest --junitxml results.xml tests/*.py'
            }
        }
        stage('Functional test') {
            steps {
                echo "testing"
            }
        }
    }
}
