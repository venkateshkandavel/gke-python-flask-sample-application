# Python Flask Dockerized Application #

Build the image using the following command

```bash
$ docker build -t simple-flask-app:latest .
```

<<<<<<< HEAD
Run the Docker container using the command shown below.nov13
=======
Run the Docker container using the command shown below.hihwru
>>>>>>> testing

```bash
$ docker run -d -p 5000:5000 simple-flask-app
```

The application will be accessible at http:127.0.0.1:5000 or if you are using bonot2docker then first find ip address using `$ boot2docker ip` and the use the ip `http://<host_ip>:5000`
