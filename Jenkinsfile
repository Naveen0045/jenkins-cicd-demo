pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/Naveen0045/jenkins-cicd-demo.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh '''
                docker stop flask-app || true
                docker rm flask-app || true
                '''
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d --name flask-app -p 5000:5000 flask-app'
            }
        }
    }
}
