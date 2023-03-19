pipeline {
    agent any

    stages {
        stage('Unittest') {
            steps {
                sh 'pip3 install python-telegram-bot'
                sh 'pip3 install pytest'
                sh 'pip3 install pylint'
                sh 'pip3 install -r requirements.txt'
             withCredentials([file(credentialsId: 'teleToken', variable: '.telegramToken')]) {
                
                sh "export .telegramToken=${.telegramToken}" }
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
