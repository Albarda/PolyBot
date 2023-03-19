pipeline {
    agent any



    stages {
        withCredentials([usernamePassword(credentialsId: 'git-hub-ron', passwordVariable: 'pass', usernameVariable: 'user')])
        stage('Unittest') {
            steps {
                
                sh 'pip3 install python-telegram-bot'
                sh 'pip3 install pytest'
                sh 'pip3 install pylint'

                }
        }
        stage("parallel stage") {
            when {
                branch 'microservices'
            }
            failFast true
            parallel {
                stage('testing') {
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




        stage('pylint') {
            steps {
                sh 'python3 -m pylint *.py'
            }
        }

    }
}
