# helm_demo3

#### variables:
```
HOST=0.0.0.0
PORT=8000
DEPLOY_ENV=test
```
### contribute:
#### 1. setup virtual environment for python


```
pip install virtualenv && \
python3 -m venv demo && \
source demo/bin/activate
```

#### 2. install dependencies
```
pip install -r ./app/requirements.txt
```

### 3 spin up application locally

#### 3.1 build docker image
```
docker build -t demo .
```
#### 3.2 start docker container
```
docker run -p 8000:8000 -d --name demo_app demo
```

## Stop project 
### 1. stoip app
```
docker rm --force demo_app
```
### 2. deactivate virtual environment
```
deactivate
```