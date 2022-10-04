# flaskuserapp
This application is to showcase the integration of Flask with Postgres.

<br>We have dockerized the application
<br>And we have added the graph-ql dashboard for the data query.

**Commands that have been used in the Demo:<br>**
docker build -t flaskapp .
docker images 
docker run flaskapp 
docker compose up -d
docker ps -al
docker compose ps 
docker compose logs flaskapp
docker inspect flaskpostgresapp_flaskapp_1
docker exec -it flaskpostgresapp_flaskapp_1 /bin/sh
docker image tag flaskapp flaskapp:1.0
docker system prune
docker container prune
docker volume prune

**<br>Configure AWS Credential:<br>**
aws configure

**<br>Login to AWS ECR:<br>**
aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin 0785XXXX1519.dkr.ecr.ap-south-1.amazonaws.com

**<br>Create ECR Repository:<br>**
aws ecr create-repository --repository-name Pythoholic --image-scanning-configuration scanOnPush=true --region ap-south-1

**<br>Tagging Docker Image:<br>**
docker tag flaskapp:1.0 0785XXXX1519.dkr.ecr.ap-south-1.amazonaws.com/pythoholic:1.0

**<br>Pushing Docker Image:<br>**
docker push 0785XXXX1519.dkr.ecr.ap-south-1.amazonaws.com/pythoholic:1.0

**<br>Removing Docker Image:<br>**
docker image rm 0785XXXX1519.dkr.ecr.ap-south-1.amazonaws.com/pythoholic:1.0

**<br>Pulling Docker Image:<br>**
docker pull 0785XXXX1519.dkr.ecr.ap-south-1.amazonaws.com/pythoholic:1.0

**<br>I have used a free template for UI from :<br>**
https://startbootstrap.com/template/sb-admin
