# k8s-Prophet

This is a very simple flask app which exposes the fbprophet time series package as a (simple) REST API.

It also has a service description for a Kubernetes deployment exposed a service.

Notes: It expects a secret_key environment variable to authenticate requests.

## Deploy Instructions

1. Build Docker image
2. Push to Docker repo (same one specified in deployment
3. With access to cluster run `kubectl apply -f prophet.yaml -n $NAMESPACE

## Run Locally
1. Build Docker image (use -t option to tag a name, say prophet)
2. Run `docker run -it -p 5000:5000 image_name` 
3. Access on localhost:5000 

TODO:

- Add more options to API
- Test`
