# TRIP backend

Need to install [libspatialindex](http://libspatialindex.github.io/)

For Mac, `brew install spatialindex`

Install Python dependencies

```sh
pip install -r requirements.txt
```

For development with hot reload
```sh
sudo FLASK_DEBUG=1 FLASK_APP=run.py flask run --host=0.0.0.0 --port=80
```

For production
```sh
sudo FLASK_APP=run.py flask run --host=0.0.0.0 --port=80
```

then on browser try:

```
http://localhost/v1/search?term=doggo
```
