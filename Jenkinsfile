pipeline {
    agent { docker { image 'python:3.7' } }
    stages {
        stage('test')  {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('build') {
            steps {
                sh 'python setup.py sdist bdist_wheel'
            }
        }
        stage('upload') {
            steps {
                sh 'twine upload --repository testpypi -u __token__ -p $TESTPYPI_API_KEY dist/*'
            }
        }
    }
}