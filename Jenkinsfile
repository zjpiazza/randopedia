pipeline {
    agent { docker { image 'python:3.7' } }
    stages {
        stage('test')  {
            steps {
                echo 'Stage: Test'
                sh 'pip install -r requirements.txt'
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