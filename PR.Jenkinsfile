pipeline {
    agent any

    stages {
        stage('Unittest') {
            steps {
                
                sh 'pip3 install python-telegram-bot'
               // sh 'pip3 install pytest'
                sh 'pip3 install pylint'
              //  sh 'python3 -m pytest --junitxml results.xml tests/*.py'
            }
        }
        stage('Functional test') {
            steps {
                echo "testing"
            }
        }
        stage('pylint') {
            step {
                sh 'python3 -m pylint *.py'
            }
        }

    }
}
