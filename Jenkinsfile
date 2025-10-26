pipeline {
    agent any

    environment {
        IMAGE = "dodgergo/vue-dashboard"
        DOCKER_CREDENTIALS = credentials('dockerhub-creds')
        NODEJS_TOOL = 'Node18' // Оновлено на Node16
    }

    tools {
        nodejs "${NODEJS_TOOL}"
    }

    stages {
        stage('Checkout') {
            steps {
                echo '🔹 Клонування репозиторію...'
                git branch: 'master', url: 'https://github.com/DodgerGOO/Kostyk_IIC'
            }
        }

        stage('Install & Build') {
            steps {
                echo '🔹 Встановлення залежностей та збірка Vue...'
                sh '''
                    npm install
                    npm run build
                '''
            }
        }

        stage('Docker Build') {
            steps {
                script {
                    // Використовуємо локальне визначення змінної, щоб уникнути warning
                    def COMMIT = sh(script: 'git rev-parse --short HEAD', returnStdout: true).trim()
                    env.IMAGE_TAG = "${IMAGE}:${COMMIT}"
                }
                echo "🔹 Побудова Docker образу з тегом ${env.IMAGE_TAG}"
                sh 'docker build -t ${IMAGE_TAG} .'
            }
        }

        stage('Docker Login & Push') {
            steps {
                echo '🔹 Авторизація в Docker Hub та завантаження образу...'
                sh '''
                    echo "${DOCKER_CREDENTIALS_PSW}" | docker login -u "${DOCKER_CREDENTIALS_USR}" --password-stdin
                    docker push ${IMAGE_TAG}
                '''
            }
        }

        stage('Run Container Test') {
            steps {
                echo '🔹 Тестовий запуск контейнера...'
                sh '''
                    docker run -d --rm --name test_vue -p 8082:80 ${IMAGE_TAG}
                    sleep 15
                    docker ps
                    curl -v http://127.0.0.1:8082 || true
                    docker stop test_vue || true
                '''
            }
        }
    }

    post {
        success {
            echo "✅ Збірка та завантаження успішно завершені!"
        }
        failure {
            echo "❌ Помилка збірки. Перевір логи Jenkins."
        }
    }
}
