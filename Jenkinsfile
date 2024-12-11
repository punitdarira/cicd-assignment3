pipeline {
    agent any
    environment {
        AZURE_CLIENT_ID = credentials('azure-client-id')
        AZURE_CLIENT_SECRET = credentials('azure-client-secret')
        AZURE_TENANT_ID = credentials('azure-tenant-id')
        RESOURCE_GROUP = credentials('resource_group')
        FUNCTION_APP_NAME = credentials('app_name')
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/punitdarira/cicd-assignment3.git'
            }
        }
        stage('Install Azure CLI') {
            steps {
                script {
                    echo 'Installing Azure CLI...'
                    sh '''
                        #!/bin/bash -l
                        if ! command -v az &> /dev/null; then
                            curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
                            export PATH=$PATH:/usr/bin
                        else
                            echo "Azure CLI already installed."
                        fi
                    '''
                }
            }
        }
        stage('Build') {
            steps {
                script {
                    echo 'Building the Python application...'
                    sh '''
                        #!/bin/bash -l
                        pip install -r requirements.txt
                    '''
                }
            }
        }
        stage('Test: Basic Response') {
            steps {
                script {
                    echo 'Running basic response test...'
                    sh '''
                        #!/bin/bash -l
                       python3 -m venv venv
                        . venv/bin/activate
                        pytest test.py
                    '''
                }
            }
        }
        stage('Package Function') {
            steps {
                script {
                    echo 'Packaging the Azure Function...'
                    sh '''
                        #!/bin/bash -l
                        zip -r function.zip *
                    '''
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    echo 'Deploying to Azure...'
                    sh '''
                        #!/bin/bash -l
                        az login --service-principal -u $AZURE_CLIENT_ID -p $AZURE_CLIENT_SECRET --tenant $AZURE_TENANT_ID
                        az functionapp deployment source config-zip --resource-group $RESOURCE_GROUP --name $FUNCTION_APP_NAME --src function.zip
                    '''
                }
            }
        }
    }
    post {
        always {
            script {
                echo 'Cleaning up...'
                sh '''
                    if [ -f function.zip ]; then rm -rf function.zip; fi
                '''
            }
        }
        success {
            script {
                echo 'Deployment successful!'
            }
        }
        failure {
            script {
                echo 'Deployment failed. Please check the logs for details.'
            }
        }
    }
}
