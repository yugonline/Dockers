# Dockers
All Dockerfiles in one place.

Steps to build and edit the Dockerfiles.

You can edit the docker file in any of these dockers. For e.g. changing the docker file of the Bastions-Docker.

		cd Dockers/Bastions

Make changes to the **Dockerfile**. After saving the file. It builds based on the Dockerfile found in the current directory. The -t parameter is used for **tagname**. The tagname can be changed upto your desire. Genji(here)

		docker build -t username/genji .

You can check the docker images using 

		docker images
		
You can see the following output : 

		username/genji            latest              12344d913742        About a minute ago   1.24GB

To push this to hub.docker.com , you need to have an account and you can login from commandline using

		docker login
	
After adding your credentials yuo can run the following command to push the docker on the cloud.

		docker push username/genji:latest

To run the docker file use the following command. Specially for the tensorflow version.

		docker run -it -p 8888:8888 -p 0.0.0.0:7007:6006 username/genji:latest	(For Mac)
		docker run -it -p 8888:8888 -p 7007:6006 bombear/bastions:latest	(For Linux)

To run a volume which is synced with your host and your docker

		docker run -it -p 8888:8888 -p 7007:6006 -v /home/bombear/workspace/Dockers/Bastions/:/notebooks/ bombear/bastions:latest

To commit a docker container(could be running) to the existing image of it using the docker ps id.

		docker commmit -m "Auto Commit" skjfnwdkfndk bombear/bastions:latest

