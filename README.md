# Outfit-Picker

Hack Western 2019

# How to develop locally

1. Open a separate terminal

2. start your local SQL instance with

`./cloud_sql_proxy -instances="lunar-descent-259920:us-central1:closet"=tcp:3306 (Mac)`
`./cloud_sql_proxy_win.exe -instances="lunar-descent-259920:us-central1:closet"=tcp:3306 (Windows)`

3. make sure you're running a virtual env for python

```
source .venv/bin/activate
```

4. cd into the `outfitpicker` directory that has `manage.py`

5. run `python manage.py runserver`

6. go to `http://127.0.0.1:8000/` in the browser to see your django app!!!!
