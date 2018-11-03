pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh 'whereis python'
                sh 'python fetchData.py'
            }
        }
    }
}