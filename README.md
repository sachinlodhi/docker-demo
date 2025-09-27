# Docker Flask Demo

Simple Flask app in Docker container.

## Files
- `app.py` - Flask web app
- `Dockerfile` - Container setup
- `requirements.txt` - Python dependencies  
- `build.sh` - Build and run script

## Run

```bash
git clone <your-repo>
cd docker-flask-demo
chmod +x build.sh
./build.sh
```

Visit: http://localhost:8080

## Stop

```bash
docker stop flask-container
docker rm flask-container
```
