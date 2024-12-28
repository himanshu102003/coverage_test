pipeline {
    agent any

    environment {
        PATH = 'C:\\Users\\himan\\Downloads\\sonar-scanner-cli-6.2.1.4610-windows-x64\\sonar-scanner-6.2.1.4610-windows-x64\\bin;C:\\Windows\\System32;C:\\Users\\himan\\AppData\\Local\\Programs\\Python\\Python313;C:\\Users\\himan\\AppData\\Local\\Programs\\Python\\Python313\\Scripts'
        PYTHON_ENV = 'python'  // Python 3.x should be in the PATH on Windows
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
                    bat 'echo %PATH%' // Print the PATH for verification
                    bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate
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
                    call venv\\Scripts\\activate
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
                junit '**/coverage.xml'  // Adjust the path if your test results are elsewhere
            }
        }
    }

   post {
        success {
            echo 'Pipeline completed successfully'
        }
        failure {
            echo 'Pipeline failed'
        }
        always {
            echo 'This runs regardless of the result.'
        }
    }
}
