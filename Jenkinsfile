pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh 'whereis python'
                // sh 'pip install requests'
                sh 'python fetchData.py'
            }
        }
    }
}