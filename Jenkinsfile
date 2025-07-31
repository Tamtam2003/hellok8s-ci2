pipeline {
  agent any
  parameters {
    choice(name: 'SERVICE', choices: ['notepad-app','hello-world'], description: 'Which service to deploy?')
    string(name: 'TAG', defaultValue: 'v1', description: 'Image tag')
  }
  environment {
    IMAGE_NAME = "tamarmey/${params.SERVICE}"
  }
  stages {
    stage('Build Image') {
      steps {
        sh "docker build -t ${IMAGE_NAME}:${params.TAG} ."
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
          sh "docker push ${IMAGE_NAME}:${params.TAG}"
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
