pipeline {

   agent {
        docker {
            image 'vaporio/jenkins-agent-python38'
            args '--user root -v /var/run/docker.sock:/var/run/docker.sock'
           
        }
    }

    stages {
        stage('requierments') {
            steps {
               
               
                sh 'pip3 install -r requirements.txt'
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
                     withCredentials([file(credentialsId: '.telegramToken', variable: 'TELEGRAM_TOKEN')]){
                        sh "cp ${TELEGRAM_TOKEN} .telegramToken"
                      

                        sh 'python3 -m pytest --junitxml results.xml tests/*.py'
                       }
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
