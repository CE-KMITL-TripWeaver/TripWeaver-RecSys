pipeline {
    agent any

    stages {

        stage('Setup Safe Directory') {
            script {
                steps {
                    sh 'git config --global --add safe.directory /var/jenkins_home/workspace'
                }
            }
        }

        stage("Clear Running Tripweaver Containers") {
            steps {
                script {
                    def containerIds = sh(script: 'docker ps -a --filter "ancestor=tripweaver-image" -q', returnStdout: true).trim()

                    if (containerIds) {
                        sh "docker stop ${containerIds}"
                        sh "docker rm ${containerIds}"
                    } else {
                        echo "No containers with the image 'tripweaver-image' found."
                    }
                }
            }
        }

        stage("Clear Running Recsys API Containers") {
            steps {
                script {
                    def containerIds = sh(script: 'docker ps -a --filter "ancestor=tripweaver-recsys-recommender_api" -q', returnStdout: true).trim()

                    if (containerIds) {
                        sh "docker stop ${containerIds}"
                        sh "docker rm ${containerIds}"
                    } else {
                        echo "No containers with the image 'tripweaver-recsys-recommender_api' found."
                    }
                }
            }
        }

        stage("Remove Old Recsys API Images") {
            steps {
                script {
                    def imageIds = sh(script: 'docker images --filter "reference=tripweaver-recsys-recommender_api" -q', returnStdout: true).trim()

                    if (imageIds) {
                        sh "docker rmi ${imageIds}"
                    } else {
                        echo "No images with the name 'tripweaver-recsys-recommender_api' found."
                    }
                }
            }
        }

        stage("Deploy"){
            steps {
                script{
                    sh "docker compose up"
                }
            }
        }
    }
}
