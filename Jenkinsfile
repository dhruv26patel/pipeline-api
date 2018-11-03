pipeline {
    agent any
    stages {
        stage('Imports') {
            steps {
                sh 'import pandas as pd'
                sh 'from sodapy import Socrata'
            }
        }
    }
}
