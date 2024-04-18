# FLASK-APPBUILDER-TEST

## flask-appbuilder app with custom auth
Custom auth with login `admin` and password `admin`

## Installation

Prerequisites:
- python
- docker
- git

Clone this repo:
```
git clone https://github.com/faked86/flask-appbuilder-test.git
cd flask-appbuilder-test
```

## Usage

### In Docker:

```
docker build -t flask-appbuilder-test .
docker run --name test -p 5000:5000 --mount source=myvol,target=/usr/src/app flask-appbuilder-test
```
Access site via `http://127.0.0.1:5000/`
