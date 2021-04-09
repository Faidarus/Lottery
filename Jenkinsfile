pipeline{
        agent any
        environment{
            DATABASE_URI = credentials("DATABASE_URI")
        }
        stages{
        //     stage('Test'){
        //         steps{
        //             sh "bash pytest.sh"
        //             }
        //         }
            stage('Build'){
                steps{
                    sh "docker-compose build"
                    }
                }
            stage('Tag & Push Image'){
                steps{
                       sh 'docker-compose push'
                    }
                }
            stage('Swarm'){
                steps{
                    sh "ansible-playbook -i inventory.yaml playbook.yaml"
                }
            }
            stage('Deploy App'){
                steps{
                    sh "docker stack deploy --compose-file docker-compose.yaml main-services"
                }
            }
        }
}