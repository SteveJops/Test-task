
# Test task from Nimble

There are 3 main kinds of tasks here. 
 - creating Data Base(PostgreSQL) creating a new table and inserting data in it. Writing a script which makes request to web api and getting "new" data out there, sorting them out and having this data obtained either inserting it in our previously created table  nor updating depend on status of data.

 - making described above process autonomous and getting it to be runned by schedule(I used celery/redis).

 - making an api with one get request to make query to db and fetch from there data by making a search by a word.


## Installation

- Clone or download the script from github.

- Install python 3.10

- Run python -m pip install -r requirements.txt

- If you`re using linux install redis server (if you have not had it yet)
- If you`re using Windows download and install redis server from github
- Run redis
- Create your own db and make some changes into app
- run and use depends on what you want to use (if celery run celery, if fastapi run it as well) 


```bash
    git clone https://github.com/SteveJops/Test-task

    cd cloned repository
    
    run redis (Check Ping)

    celery -A tasks beat --loglevel=INFO

    uvicorn src.main:app --reload --port 8000
```

- Enter your request in browser

    https://localhost:8000 

Be using the script.
## Usage/Examples

/api/textsearch/{word} - to interact with the api by handing over data from your db
