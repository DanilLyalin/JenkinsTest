pipeline {
    agent {
            docker {
                image 'python:3.5.1'
            }
        }
    stages {
        stage('Build') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pip3 install --user robotframework'
                    sh 'python3 --version'
                }
            }
        }
        stage('Test') {
        	steps {
                sh 'python3 ./.local/lib/python3.5/site-packages/robot tests.robot'
            }
        }
    }
}