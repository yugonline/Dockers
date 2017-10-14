# Dockers
All Dockerfiles in one place.

Steps to build and edit the Dockerfiles.

You can edit the docker file in any of these dockers. For e.g. changing the docker file of the Bastions-Docker.

		cd Dockers/Bastions

Make changes to the **Dockerfile**. After saving the file. It builds based on the Dockerfile found in the current directory.

		docker build -t bastions .

You can check the docker images using 

		docker images

To push this to hub.docker.com or hub.docker.io, you need to have an account and you can login from commandline using

		docker login
	
After adding your credentials yuo can run the following command to push the docker on the cloud.

		docker push yugshende/bastions:latest
