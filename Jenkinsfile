pipeline {
    agent {
        docker {
            image 'python:3.7'
            args '-u root:root'
        }
    }
    environment {
        TESTPYPI_API_KEY = credentials('testpypi-api-key')
    }
    stages {
        stage('Setup') {
            steps {
                echo 'Stage: Setup'
                sh 'pip install -r requirements.txt --user --no-cache-dir'
            }
        }
        stage('Test')  {
            steps {
                echo 'Stage: Test'
                sh 'python -m pytest'
            }
        }
        stage('Build') {
            steps {
                echo 'Stage: Build'
                sh 'python setup.py sdist bdist_wheel'
            }
        }
        stage('Upload') {
            steps {
                echo 'Stage: Upload'
                sh 'python -m twine upload --repository testpypi -u __token__ -p $TESTPYPI_API_KEY dist/* --skip-existing'
            }
        }
    }
}