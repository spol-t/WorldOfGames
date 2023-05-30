pipeline {
    agent any

    stages {
        stage('checkout') {
            steps {
                git 'https://github.com/spol-t/WorldOfGames.git'
            }
        }
        stage('Build') {
            steps {
                sh 'docker-compose build'
            }
        }
        stage('Run Docker') {
            steps {
                sh 'docker run -d -p 8777:8777 --name worldofgames wog'
            }
        }
        stage('test') {
            steps {
                sh 'python3 e2e.py'
            }
        }
        stage('finelize') {
            steps {
                sh 'docker stop worldofgames'
                sh 'docker rm worldofgames'
                sh 'docker login'
                sh 'docker tag worldofgames tomerspol/worldofgames:latest'
                sh 'docker push tomerspol/worldofgames'
            }
        }

    }
}
