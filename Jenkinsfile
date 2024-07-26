pipeline {
    agent any

    environment {
        KUBECONFIG = "${env.USERPROFILE}\\.kube\\config" // Path to your kubeconfig file
        MINIKUBE_HOME = "${env.USERPROFILE}\\.minikube" // Path to Minikube home directory
        PATH = "${env.PATH};${env.USERPROFILE}\\.minikube\\bin" // Ensure Minikube binaries are in PATH

    }

        stage('Build') {
            steps {
                script {
                    // Use Windows batch command to install dependencies
                    bat 'pip install -r requirements.txt'
                }
            }
        }
        //stage('Test') {
         //   steps {
                // Use Windows batch command to run tests
         //       bat 'pytest'
         //   }
        //}
        stage('Docker Build') {
            steps {
                script {
                    // Use Windows batch command to build Docker image
                    bat 'docker build .'
                }
            }
        }
        stage('Deploy to Minikube') {
            steps {
                script {
                    // Use Windows batch command to deploy application using kubectl
                    bat 'kubectl apply -f deployment.yaml'
                }
            }
        }
    }
}
