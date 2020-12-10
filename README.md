# Documentation of pizza

#### To set up the environment (Python3)

- Check that python 3 is installed:

```bash
python --v
>> Python 3.8.6
```

- Create virtual environment and activate it

```bash
$ python -m venv pizza_venv
$ source pizza_venv/bin/activate
```

- Install dependencies:

```bash
$ pip install - r requirements.txt
```

- Configuring environment variables
    - create a file named `dev.env` on the root directory
    - Copy content on `env.sample` to `dev.env` and edit whatever variable you want

#### To setup database

- if you have `psql` installed on the terminal run

 ```bash
$ createdb pizza_db  # to create database
$ dropdb pizza_db  # to delete database
```

- No psql to create the database you use any database client e.g `pgAdmin` or `DBeaver`

- After, you have created the database run the db upgrade command to create the tables

```buildoutcfg
$ flask db upgrade
```

- To update table columns or add new tables you can run

```buildoutcfg
$ flask db migrate
# Then
$ flask db upgrade
```

### To run the application

```buildoutcfg
$ flask run
```

### API Documentation

[Postman](https://documenter.getpostman.com/view/4000258/TVmV5DtS)

### Possible improvements

- Add tests
- Build a simple frontend
- Use of json data format instead of text data
- Add authentication
