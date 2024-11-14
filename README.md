## Introduction
 `django_demo_starter` is a dockerized python webapp with simple html pages based on the Tech With Tim - Django in 20 minutes. 
 
## Usage 
 To run the application, make sure to have the prerequesit installed: 
    - Docker    
 
# Development

 To build a development Docker Image:
```
docker build -t 'django_starter:dev'  .   
```

 Running develpment image on local volume: 
```
docker run -it -p 8000:8000 -v $(pwd)/src:/usr/share/src django_starter:dev sh
```

Run server (container broadcast to localhost:8000)
```
python manage.py runserver 0.0.0.0:8000
```
Access on browser via: http://localhost:8000/

Admin Panel: http://localhost:8000/admin

Admin credentials: root 123123

# References 

 [Django in 20 minutes](https://www.youtube.com/watch?v=nGIg40xs9e4)
