pipeline {
    agent any

    stages {
        stage('Clone Code') {
            steps {
                git 'https://github.com/master-ankitt/flask-fusion-pipeline.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Stop Existing App') {
            steps {
                sh 'fuser -k 5000/tcp || true'
            }
        }

        stage('Run Flask App') {
            steps {
                sh 'nohup python3 app.py &'
            }
        }
    }
}
