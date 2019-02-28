def label = "mypod-${UUID.randomUUID().toString()}"
podTemplate(label: label, containers: [
    containerTemplate(name: 'docker', image: 'docker', command: 'cat', ttyEnabled: true),
    containerTemplate(name: 'kubectl', image: 'lachlanevenson/k8s-kubectl:v1.8.8', command: 'cat', ttyEnabled: true)
    ],
    volumes: [
    hostPathVolume(mountPath: '/var/run/docker.sock', hostPath: '/var/run/docker.sock')
    ]) {
    node(label) {
        def myRepo = checkout scm
        def gitCommit = myRepo.GIT_COMMIT
        def gitBranch = myRepo.GIT_BRANCH

        stage('Run shell') {
            sh 'echo hello world'

        }
        stage('push to docker hub'){
            container('docker'){
                 withCredentials([[$class: 'UsernamePasswordMultiBinding',
                  credentialsId: 'dockerhub',
                  usernameVariable: 'DOCKER_HUB_USER',
                  passwordVariable: 'DOCKER_HUB_PASSWORD']]) {
                  sh """
                    ls -ls
                    docker login -u ${DOCKER_HUB_USER} -p ${DOCKER_HUB_PASSWORD}
                    docker build -t sharad23/django-k8:v4 .
                    docker push sharad23/django-k8:v4
                    """
                }
            }
        }
        stage('Run kubectl') {
          container('kubectl') {
            sh "kubectl get pods"
            sh "kubectl get svc"
            sh "kubectl get deployments"
            // sh "kubectl --record deployment/web set image deployment/web web=sharad23/sharad-nginx:v2"
          }
        }
    }
}
