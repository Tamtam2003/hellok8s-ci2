pipeline {
    agent any

    // 1. מגדירים את הפרמטרים שיופיעו ב-Build with Parameters
    parameters {
        choice(name: 'SERVICE',
               choices: ['notepad-app','hello-world'],
               description: 'Which service to deploy?')
        string(name: 'TAG',
               defaultValue: 'v1',
               description: 'Image tag')
    }

    // 2. בונים משתני סביבה על בסיס הפרמטרים
    environment {
        IMAGE_NAME = "tamarmey/${params.SERVICE}"
        IMAGE_TAG  = "${params.TAG}"
    }

    stages {
        stage('Build Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
            }
        }

        stage('Push Image') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh "echo \$DOCKER_PASS | docker login -u \$DOCKER_USER --password-stdin"
                    sh "docker push ${IMAGE_NAME}:${IMAGE_TAG}"
                }
            }
        }

        stage('Deploy via Ansible') {
            steps {
                sh "ansible-playbook -i inventory deploy-playbook.yml --extra-vars \"service=${params.SERVICE} tag=${params.TAG}\""
            }
        }
    }
}

