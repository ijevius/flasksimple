pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh '''#!/bin/bash
        # Check if port 4567 is in use
if lsof -Pi :4567 -sTCP:LISTEN -t >/dev/null ; then
    echo "Port 4567 is in use. Killing process..."
    # Get the PID of the process using port 4567
    pid=$(lsof -Pi :4567 -sTCP:LISTEN -t)
    # Kill the process
    kill $pid
    echo "Process $pid killed."
else
    echo "Port 4567 is not in use."
fi
        '''
      }
    }
    stage('hello') {
      steps {
        sh 'python3 server.py'
      }
    }
  }
}
