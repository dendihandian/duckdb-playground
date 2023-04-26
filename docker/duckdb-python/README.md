```
poetry config virtualenvs.in-project true
```

```
poetry run pip freeze > requirements.txt
```

```
poetry export --without-hashes --format=requirements.txt > requirements.txt
```