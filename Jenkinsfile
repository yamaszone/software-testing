pipeline {
  agent {
    docker {
      image 'ubuntu:14.04'
    }
    
  }
  stages {
    stage('A') {
      steps {
        sh '''#!/bin/bash
        ./install'''
      }
    }
  }
}