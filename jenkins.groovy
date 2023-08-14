pipeline {
    agent { 
        docker {
            image '${params.artifactory_url}'
            registryUrl 'https://artifactory.jpl.nasa.gov:16003'
            registryCredentialsId  'artifactory_credential_id'
            args '--user 0:0'
            reuseNode true
        } 
    }
    stages {
        stage('Install pynitf') {
            steps {
                sh 'pip install .'
            }
        }
        stage('Run Unit Tests') {
            steps {
                sh 'pytest tests/'
            }
        }
    }
    post {
        failure {
            emailext (
                to: 'hargitay@jpl.nasa.gov',
                subject: 'Build FAILURE in Jenkins: $PROJECT_NAME - #$BUILD_NUMBER',
                body: 'Check console output at $BUILD_URL to view the results. Build has failed.'
            )
        }
        success {
            emailext (
                to: 'hargitay@jpl.nasa.gov',
                subject: 'Build SUCCESS in Jenkins: $PROJECT_NAME - #$BUILD_NUMBER',
                body: 'Check console output at $BUILD_URL to view the results. Build was successful.'
            )
        }
        cleanup {
            cleanWs()
        }
    }
}
