pipeline {
    agent any

    environment {
        PATH = 'C:\\Users\\himan\\Downloads\\sonar-scanner-cli-6.2.1.4610-windows-x64\\sonar-scanner-6.2.1.4610-windows-x64\\bin;C:\\Windows\\System32;C:\\Users\\himan\\AppData\\Local\\Programs\\Python\\Python313;C:\\Users\\himan\\AppData\\Local\\Programs\\Python\\Python313\\Scripts'
        PYTHON_ENV = 'python'  // 'python' should point to Python 3.x in the PATH on Windows
        COVERAGE_REPORT = 'coverage.xml'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from GitHub
                checkout scm
            }
        }

        stage('Set Up Python Environment') {
            steps {
                // Set up Python environment and install dependencies
                script {
                    bat 'echo %PATH%'
                    bat '''
                    python -m venv venv
                    venv\\Scripts\\activate
                    pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Tests and Coverage') {
            steps {
                // Run the unit tests and collect coverage data
                script {
                    bat '''
                    venv\\Scripts\\activate
                    coverage run -m unittest discover
                    coverage report
                    coverage xml -o ${COVERAGE_REPORT}
                    '''
                }
            }
        }

        stage('Publish Coverage Report') {
            steps {
                // Publish the coverage report to Jenkins
                script {
                    junit '**/coverage.xml'  // Adjust the path if your test results are elsewhere
                }
            }
        }
    }

    post {
        always {
            // Clean up after the pipeline execution
            echo 'Cleaning up...'
            cleanWs()
        }
    }
}
