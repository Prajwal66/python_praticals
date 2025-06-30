pipeline {
    agent any

    environment {
        VENV = 'venv'
    }

    stages {
        stage('Clone repository') {
            steps {
               echo " cloned "
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                    python3 -m venv ${VENV}
                    . ${VENV}/bin/activate
                    pip install --upgrade pip
                '''
            }
        }


        stage('Run Flask App') {
            steps {
                sh '''
                    . ${VENV}/bin/activate
                    export FLASK_APP=app.py
                    export FLASK_ENV=development
                    nohup flask run --host=0.0.0.0 --port=5000 &
                '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution completed.'
        }
        success {
            echo 'All steps succeeded.'
        }
        failure {
            echo 'Build failed.'
        }
    }
}
