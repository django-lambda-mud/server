### Set up your local server
* Set up your virtual environment
  * `pipenv --three`
  * `pipenv install`
  * `pipenv shell`

* Add your secret credentials
  * Create `.env` in the root directory of your project
  * Add your pusher credentials and secret key
    ```
    SECRET_KEY='<your_secret_key>'
    DEBUG=True
    PUSHER_APP_ID=<your_app_id>
    PUSHER_KEY=<your_pusher_key>
    PUSHER_SECRET=<your_pusher_secret>
    PUSHER_CLUSTER=<your_pusher_cluster>
    ```

* Run database migrations
  * `./manage.py makemigrations`
  * `./manage.py migrate`

* Add rooms to your database
  * `./manage.py shell`
  * Copy/paste the contents of `util/create_world.py` into the Python interpreter
  * Exit the interpreter

* Run the server
  * `./manage.py runserver`


