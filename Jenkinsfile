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
                    sh 'robot --version'
                }
            }
        }
        stage('Test') {
        	steps {
                sh 'robot tests.robot'
            }
        }
    }
}