# FLASK-APPBUILDER-TEST

## flask-appbuilder app with github auth
Custom auth is in the different branch.

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

Create `.env` file:
```
CLIENT_ID=GITHUB_CLIENT_ID
CLIENT_SECRET=GITHUB_CLIENT_SECRET
```

## Usage

### In Docker:

```
docker build -t flask-appbuilder-test .
docker run --name test -p 5000:5000 --mount source=myvol,target=/usr/src/app flask-appbuilder-test
```
Access site via `http://127.0.0.1:5000/`
