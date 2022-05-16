# Breathe

## Developer documentation

### Dev container

Breathe uses VSCode and dev containers.

To start your dev container, in VSCode click on green icon in the bottom left, then click "Reopen in Container"

### Running API

Once in a dev container, in Terminal, you can run

```cmd
python3 -m uvicorn api.main:app
```

Once it's up, you can navigate to [http://localhost:8000/api/docs](http://localhost:8000/api/docs)
and use Swagger UI.

### Using Swagger UI

Swagger UI allows to debug Rest API from a browser.
Select an API endpoint, click "Try out", then click "Execute".

### Debugging API

In VSCode, go to "Run and Debug" panel, then select "API". This will launch Fast API server, and you
can use breakpoints in API methods for debugging.