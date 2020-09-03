pipeline {
    agent {
        docker {
            image 'python:3.7'
        }
    }
    environment {
        TESTPYPI_API_KEY = credentials('testpypi-api-key')
    }
    stages {
        stage('test')  {
            steps {
                echo 'Stage: Test'
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pip install -r requirements.txt --user --no-cache-dir'
                    sh 'pip install twine --user --no-cache-dir'
                }
            }
        }
        stage('build') {
            steps {
                echo 'Stage: Build'
                sh 'python setup.py sdist bdist_wheel'
            }
        }
        stage('upload') {
            steps {
                echo 'Stage: Upload'
                sh 'twine upload --repository testpypi -u __token__ -p $TESTPYPI_API_KEY dist/*'
            }
        }
    }
}