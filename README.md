## End to End ML project

import dagshub
dagshub.init(repo_owner='Naman-1274', repo_name='ML-Project', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)