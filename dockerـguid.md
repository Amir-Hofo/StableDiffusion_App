# login docker
```bash   
docker login
```

# create image file
```bash
docker build -t stable-diffusion-app .
```

# run container
```bash
docker run -d -p 8000:8000 \
    -v $(pwd)/model/token.txt:/app/model/token.txt \
    -v $(pwd)/output:/app/output \
    --name stable-diffusion-container \
    stable-diffusion-app
```

# Open the app in browser
```bash
http://127.0.0.1:8000
```

# container status
```bash
docker ps
```

# container logs
```bash
docker logs stable-diffusion-container
```

# dockerhub

## tag image
```bash
docker tag stable-diffusion-app amirhofo/stable-diffusion-app:1.0
```
## push
```bash
docker push amirhofo/stable-diffusion-app:1.0
```