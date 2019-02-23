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
                sh 'docker pull busybox'
                sh "echo ${gitCommit}"
            }
        }
        stage('Run kubectl') {
          container('kubectl') {
            sh "kubectl get pods"
            sh "kubectl get svc"
            sh "kubectl get deployments"
            sh "kubectl --record deployment/web set image deployment/web web=sharad23/sharad-nginx:v2"
          }
        }
    }
}