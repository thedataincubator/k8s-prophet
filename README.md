# k8s-Prophet

This is a very simple flask app which exposes the fbprophet time series package as a (simple) REST API.

It also has a service description for a Kubernetes deployment exposed a service.

Notes: It expects a secret_key environment variable to authenticate requests.

## Deploy Instructions

1. Build Docker image
2. Push to Docker repo (same one specified in deployment
3. With access to cluster run `kubectl apply -f prophet.yaml

TODO:

- Add more options to API
- Test`
