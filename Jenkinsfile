pipeline {
    agent any

    stages {
        stage('Clone from GitHub') {
            steps {
                git 'https://github.com/master-ankitt/flask-fusion-pipeline.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Flask App') {
            steps {
                // Kill any running process on port 80 (optional)
                sh 'fuser -k 80/tcp || true'
                sh 'nohup python3 app.py &'
            }
        }
    }
}
