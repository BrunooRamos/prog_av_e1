pipeline {
    agent any
    stages {
        stage('Clonar Repositorio') {
            steps {
                git url: 'https://github.com/BrunooRamos/prog_av_e1.git', branch: 'main'
            }
        }
        
        stage('Ejecutar Pruebas') {
            steps {
                sh '/usr/bin/python3 -m unittest discover -s test'
            }
        }
        
        stage('Generar Documentación') {
            steps {
                sh 'sudo mkdir -p /opt/docs && sudo chmod 777 /opt/docs'
                
                // Genera la documentación en formato HTML y la mueve a la carpeta correcta
                sh 'cd src && python3 -m pydoc -w main'
                
                // Mueve el archivo generado a la ubicación final
                sh 'sudo mv src/main.html /var/www/html/documentins/trivia.html'
            }
        }
    }
    
    post {
        success {
            // Envía un correo con el archivo trivia.html adjunto y un mensaje de éxito
            emailext(
                to: 'brunoramos.u@gmail.com',
                subject: 'Generación de Documentación Completada con Éxito',
                body: '''Hola Bruno,

La documentación ha sido generada exitosamente y el archivo trivia.html ha sido generado y movido a la ubicación correspondiente.

Saludos,
Jenkins
                ''',
                attachFiles: '/var/www/html/documentins/trivia.html'
            )
        }
        
        failure {
            // Envía un correo en caso de que ocurra un fallo
            emailext(
                to: 'brunoramos.u@gmail.com',
                subject: 'Error en la Generación de Documentación',
                body: '''Hola Bruno,

Hubo un problema durante la generación de la documentación. Revisa el log de Jenkins para más detalles.

Saludos,
Jenkins
                '''
            )
        }
    }
}
