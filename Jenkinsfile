pipeline {
    agent any

    environment {
        PATH = 'C:\\Users\\himan\\Downloads\\sonar-scanner-cli-6.2.1.4610-windows-x64\\sonar-scanner-6.2.1.4610-windows-x64\\bin;C:\\Windows\\System32;C:\\Users\\himan\\AppData\\Local\\Programs\\Python\\Python313;C:\\Users\\himan\\AppData\\Local\\Programs\\Python\\Python313\\Scripts'
        PYTHON_ENV = 'python'  // Python 3.x should be in the PATH on Windows
        COVERAGE_REPORT = 'coverage.xml'
        SONARQUBE_SERVER = 'sonarqube-server'  // Name of SonarQube server configured in Jenkins
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

        stage('SonarQube Analysis') {
            steps {
                script {
                    // Run SonarQube scanner
                    withSonarQubeEnv(SONARQUBE_SERVER) {
                        bat '''
                        sonar-scanner -Dsonar.projectKey=sonar-coverage-jenkins ^
                        -Dsonar.projectName=sonar-coverage-jenkins ^
                        -Dsonar.sources=. ^
                        -Dsonar.python.coverage.reportPaths=coverage.xml ^
                        -Dsonar.host.url=http://localhost:9000 ^
                        -Dsonar.token=sqp_6d69898c79fd92cc902f17dc10ab54f5305fddc4
                        
                        '''
                    }
                }
            }
        }

        stage('Publish Coverage Report') {
            steps {
                // Ensure the coverage report exists before publishing
                bat 'dir ${COVERAGE_REPORT}'

                // Publish the coverage report using the SonarQube plugin (already handled in the SonarQube stage)
                // If you wish to publish using other methods like Cobertura or JaCoCo, you can use:
                // publishCoverage adapters: [jacocoAdapter('coverage.xml')]
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
