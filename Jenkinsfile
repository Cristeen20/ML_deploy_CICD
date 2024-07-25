pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    // Use Windows batch command to install dependencies
                    bat 'pip install -r requirements.txt'
                }
            }
        }
        stage('Test') {
            steps {
                // Use Windows batch command to run tests
                bat 'pytest'
            }
        }
        stage('Docker Build') {
            steps {
                script {
                    // Use Windows batch command to build Docker image
                    bat 'docker build data-analytics-app:latest .'
                }
            }
        }
        stage('Deploy to Minikube') {
            steps {
                script {
                    // Use Windows batch command to deploy application using kubectl
                    bat 'kubectl apply -f k8s/deployment.yaml'
                }
            }
        }
    }
}
