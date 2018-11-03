pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'brew install python3'
                sh 'python3 --version'
                sh 'whereis python3'
                sh 'pip3 install requests'
                sh 'python3 fetchData.py'
            }
        }
    }
}