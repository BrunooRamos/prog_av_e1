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
                // Crear la carpeta /opt/docs si no existe
                sh 'sudo mkdir -p /opt/docs && sudo chmod 777 /opt/docs'
                
                // Generar la documentación HTML con pydoc
                sh 'python3 -m pydoc -w main'
                
                // Mover el archivo HTML generado a la carpeta /opt/docs
                sh 'sudo mv documentacion.html /opt/docs/trivia.html'
            }
        }
    }
}

