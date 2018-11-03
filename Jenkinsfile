pipeline {
    agent { docker { image 'python:3.5.1' } }

    stage('API CALL') {
        steps {
             sh 'python fetechData.py'
        }
    }
}
