[![Test Multiple Python Versions](https://github.com/sotc/devops-conductor/actions/workflows/main.yml/badge.svg)](https://github.com/sotc/devops-conductor/actions/workflows/main.yml)

![AWS CodeBuild](https://codebuild.us-west-2.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiRzZ4UFhOcWRnMWIwek0zYkR6YUdCYmlyVVhaSDNaQnVwdEcyZ1ZDUm40S1VDSzN0RjZwaEJRNTh6aUo0YlJvTHhxa2o3TUFBNEIrY3EyQkQ1d1ArTzlZPSIsIml2UGFyYW1ldGVyU3BlYyI6Im5ZQ3Y0c1N3WHo2ZEdOTkciLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)



# devops-conductor
Port and deploy web app service


### Initial Setup
1. make setup
2. source ~/.conductordevops/bin/activate
3. make install

### Containerized app
1. `docker build -t conductor-app:latest .`
2. `docker run -d --env-file ./jwtSecret.env -p 3001:3000 conductor-app`

### Test the app locally
1. `curl -v  http://127.0.0.1:3000/`
2. ` curl -v -H "Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYmYiOjE1NTQ3NTU1NTUsImV4cCI6MjU1NDc1NTUwMCwiaWF0IjoxNTU0NzU1NTAwLCJqdGkiOiI5ZmRmMGE2Ni00YzllLTRlOTktODc4MC05YjdlOTNlMjFlMjciLCJ1c2VyX2lkIjoiMTA1YjM1MTgtNjQ2ZC00NjNlLWFkZGEtZDJiOTM5YzJkMDZkIiwidXNlcl9mdWxsX25hbWUiOiJCZXJ0cmFtIEdpbGZveWxlIiwidXNlcl9lbWFpbCI6Im51bGxAcGllZHBpcGVyLmNvbSJ9.-A8Gx18iTikKpedcxDlgcc7D8GMWFix0709Vfpbo1SI" 127.0.0.1:3001/v1/user/ `
3. `curl -v  http://127.0.0.1:3001/healthz/`
4. Open a web browser: `http://127.0.0.1:3001/docs`


### Option 1. Quick and low-code, fully managed. AWS App Runner Deployment into cloud.
1. Elastic Container Registery
2. `aws ecr get-login-password --region region | docker login --username AWS --password-stdin aws_account_id.dkr.ecr.region.amazonaws.com`
3. docker build -t devops-conductor .
4. docker tag devops-conductor:latest `<ecr endpoint>`/devops-conductor:latest
5. docker push `<ecr endpoint>`/devops-conductor:latest
6. Create AppRunner via webconsole or IaC
7. You can now use the curl commands on the endpoint provided by AppRunner

### Option 2. Using IaC to deploy into aws. APIGatewa, Lambda, 
### CI
github Actions to format, test, and lint

### IAC
CDK Fastapi deployment to Fargate sitting behind ALB for load balancing. This porject assumes aws cli installed and account environment variables are already setup
1. cd conductorapi/cdk
2. cdk deploy
3. After the deploy completes, you will see the endpoint printed out the terminal
4. curl -v https://<myendpoint>.elb.amazonaws.com/
 
### Tear down infrastructure
  * cdk destory
  * cdk diff
  
### Overview of app load balancing
  
  ![alb_diagram 001](https://user-images.githubusercontent.com/512362/175837475-681a0488-e743-45b8-b737-e108f98e5aec.jpeg)

  
  
