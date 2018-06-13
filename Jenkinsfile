// Openshift project
OPENSHIFT_SERVICE_ACCOUNT = 'jenkins'
DOCKER_REPO_URL = 'docker-registry.default.svc.cluster.local:5000'
CI_NAMESPACE= env.CI_PIPELINE_NAMESPACE ?: 'ai-coe'
CI_TEST_NAMESPACE = env.CI_THOTH_TEST_NAMESPACE ?: CI_NAMESPACE

// IRC properties
IRC_NICK = "aicoe-bot"
IRC_CHANNEL = "#thoth-station"


tokens = "${env.JOB_NAME}".tokenize('/')
org = tokens[tokens.size()-3]
repo = tokens[tokens.size()-2]
branch = tokens[tokens.size()-1]


properties(
    [
        buildDiscarder(logRotator(artifactDaysToKeepStr: '30', artifactNumToKeepStr: '', daysToKeepStr: '90', numToKeepStr: '')),
        disableConcurrentBuilds(),
    ]
)


pipeline {
    agent {
        kubernetes {
            cloud 'openshift'
            label 'thoth'
            serviceAccount OPENSHIFT_SERVICE_ACCOUNT
            containerTemplate {
                name 'jnlp'
                args '${computer.jnlpmac} ${computer.name}'
                image DOCKER_REPO_URL + '/'+ CI_NAMESPACE +'/jenkins-aicoe-slave:latest'
                ttyEnabled false
                command ''
            }
        }
    }
    stages {
        stage("Setup BuildConfig") {
            steps {
                script {                    
                    env.TAG = "test"
                    env.REF = "master"

                    // TODO check if this works with branches that are not included in a PR
                    if (env.BRANCH_NAME != 'master') {
                        env.TAG = env.BRANCH_NAME.replace("/", "-")

                        if (env.Tag.startsWith("PR")) {
                            env.REF = "refs/pull/${env.CHANGE_ID}/head"
                        } else {
                            env.REF = branch.replace("%2F", "/")
                        }
                    }

                    openshift.withCluster() {
                        openshift.withProject(CI_TEST_NAMESPACE) {
                            if (!openshift.selector("template/core-e2e-test-buildconfig").exists()) {
                                openshift.apply(readFile('openshift/buildConfig-e2e-test-template.yaml'))
                                echo "BuildConfig Template created!"
                            }

                            /* Process the template and return the Map of the result */
                            def model = openshift.process('core-e2e-test-buildconfig',
                                    "-p", 
                                    "IMAGE_STREAM_TAG=${env.TAG}",
                                    "GITHUB_REF=${env.REF}")

                            echo "BuildConfig Model from Template"
                            echo "${model}"

                            echo "Updating BuildConfig from model..."
                            createdObjects = openshift.apply(model)
                        }
                    }
                }
            } // steps
        } // stage
        stage("Get Changelog") {
            steps {
                node('master') {
                    script {
                        env.changeLogStr = pipelineUtils.getChangeLogFromCurrentBuild()
                        echo env.changeLogStr
                    }
                    writeFile file: 'changelog.txt', text: env.changeLogStr
                    archiveArtifacts allowEmptyArchive: true, artifacts: 'changelog.txt'
                } // node: master
            } // steps
        } // stage
        stage("Build Container Images") {
            parallel {
                stage("End-to-End Tests") {
                    steps {
                        echo "Building Thoth End-to-End Tests container image..."
                        script {
                            tagMap['user-api'] = aIStacksPipelineUtils.buildImageWithTag(CI_TEST_NAMESPACE, "core-e2e-test", "${env.TAG}")
                        }

                    } // steps
                } // stage
            } // 
        } // stage
    } // stages
    post {
        success {
            echo "All Systems GO!"
        }
        failure {
            script {
                mattermostSend channel: "#thoth-station", 
                    icon: 'https://avatars1.githubusercontent.com/u/33906690', 
                    message: "${JOB_NAME} #${BUILD_NUMBER}: ${currentBuild.currentResult}: ${BUILD_URL}"

                error "BREAK BREAK BREAK - build failed!"
            }
        }
    }
}
