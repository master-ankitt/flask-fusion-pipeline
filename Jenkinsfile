pipeline {
    agent any

    stages {
        stage('Clone Code') {
            steps {
                git branch: 'main', url: 'https://github.com/master-ankitt/flask-fusion-pipeline.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'sudo pip3 install -r requirements.txt'
            }
        }

        stage('Stop Existing App') {
            steps {
                sh 'sudo fuser -k 5000/tcp || true'
            }
        }

        stage('Run Flask App') {
            steps {
                sh 'sudo python3 app.py '
            }
        }
    }
}
