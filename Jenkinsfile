pipeline {
    agent any
    stages {
        stage('Imports') {
            steps {
                sh 'python import pandas as pd'
                sh 'python from sodapy import Socrata'
            }
        }
    }
}
