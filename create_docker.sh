#!/bin/bash
dockerPid=`sudo docker ps -a |grep 'cellxgene-gateway' |awk '{print $1}'`;
echo "docker pid " $dockerPid;
sudo docker stop $dockerPid;
sudo docker rm $dockerPid;
dockerImage=`sudo docker images|grep 'cellxgene-gateway'|awk '{print $3}'`;
echo "docker image" $dockerImage;
sudo docker rmi $dockerImage;
sudo docker build -t cellxgene-gateway:v1.0 .
sudo docker run -dti -v /data/cellxgene-data:/cellxgene-data -p 5005:5005 --restart=always --name cellxgene-gateway cellxgene-gateway:v1.0
