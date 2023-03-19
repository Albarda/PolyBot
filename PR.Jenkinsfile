pipeline {
    agent any



    stages {

        stage('Unittest') {
            steps {
                
                sh 'pip3 install python-telegram-bot'
                sh 'pip3 install pytest'
                sh 'pip3 install pylint'
                sh 'pip3 install -r requirements.txt'


                } #steps
        } #stage Unittesttte
        stage("parallel stage") {
            when {
                branch 'microservices'
            } #when
            failFast true
            parallel {
                stage('testing') {
            steps {

                sh 'python3 -m pytest --junitxml results.xml tests/*.py'
            } #steps
        } #stage testing
         stage('Functional test') {
            steps {
                echo "testing"
            } #steps
        } #stage Functional test
    } #stage parallel stage





        stage('pylint') {
            steps {
                sh 'python3 -m pylint *.py'
            }#steps
        }#stage pylint

    } #pipeline


