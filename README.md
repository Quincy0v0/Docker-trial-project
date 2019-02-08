# Docker-trial-project

Build the react app Docker Image with tag 'react-app'
```
docker build -t react-app .
```
Run a Docker Container.
```
#Map the port 3000 and 3001. 
#Make a volume for the code directory. 
#Tag the Container with 'react'
docker run \
      -p 127.0.0.1:3000:3000 \
      -v ~/reactapp:/usr/src/app/react-app/ \
      -d --name react react-app
```
Setup the react environment
```
docker exec react frontend
```
Setup the express environment
```
docker exec react backend
```
##### now edit the code in ~/reactapp
