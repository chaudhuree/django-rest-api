### initiate a project
```
uv init dj-project --python 3.12
```

 ### install django and django-extensions
```
uv add django django-extensions djangorestframework
```

### create django project
```
uv run django-admin startproject myproject .
```
### start server
```
uv run manage.py runserver
```

### create new app
```
uv run manage.py startapp myapp
```

### create migrations
```
uv run manage.py makemigrations
```

```
uv run manage.py migrate
```

### add dev dependencies
```
uv add --dev black
```

### after deleting or cloning env or repo install all but not dependencies
```
uv sync --no-dev
```

### add packages with a group name
```
uv add --group prod uvicorn whitenoise gunicorn
```

### insall all packages and exclude dev group
```
uv sync --no-group dev --group prod
```