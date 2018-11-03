pipeline {
    agent { docker { image 'python:3.5.1' } }
    stages {
        stage('version call') {
            steps {
                sh 'python --version'
            }
        }
    }
}
