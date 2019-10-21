# CS Build Week 1

For your first CS Build Week, you will be building an interactive ***Multi-User Dungeon (MUD)*** client and server in groups. To succeed with this project, you will be applying knowledge you've learned throughout the first part of CS to this project.

You should treat this like a real-world job assignment with your instructor as the client. Like in the real world, you may not be given all the information you need to complete the assignment up front. It is your responsibility to understand the requirements and ask questions if anything is unclear (Polya) before jumping into the code.

### What is a MUD?
>A MUD...is a multiplayer real-time virtual world, usually text-based. MUDs combine elements of role-playing games, hack and slash, player versus player, interactive fiction, and online chat. Players can read or view descriptions of rooms, objects, other players, non-player characters, and actions performed in the virtual world. Players typically interact with each other and the world by typing commands that resemble a natural language. - Wikipedia

With the adventure game built in previous weeks, you have already created an application containing some of these elements (rooms, descriptions, objects, players, etc.). In this project, we will be expanding these worlds to be more interactive, provide new actions for players, display world info on a professional client site, and run the world's server on a hosted site to allow multi-player functionality.

## Deliverables

Each team is responsible for building and deploying a functional MUD server, migrating a unique world onto that server, and creating a visualization and navigation client interface. We provide starter Django code with much of the server functionality implemented.




### Server

#### 1. Learn Django

In Sprint 1, you learned a new language (Python) and built an interactive world with it. During this project, you will be learning a new web framework (Django) and building a more interesting world.

You may find these resources useful:

* [Intro to Django github repo](https://github.com/LambdaSchool/Intro-Django)
* [CS12: Intro to Django: Setup, Models, and Migrations](https://www.youtube.com/watch?v=5rfCWD0jB9U)
* [CS12: Intro to Django: GraphQL and Graphene](https://www.youtube.com/watch?v=0qsOwWTo2wc)
* [CS12: Intro to Django: REST and Users](https://www.youtube.com/watch?v=yMGUq3i1qBY)
* [CS12: Intro to Django: Token Auth, GraphQL Mutations](https://www.youtube.com/watch?v=_8nTE2NE5tg)
* [The official documentation](https://docs.djangoproject.com/en/2.2/intro/)

#### 2. Deploy a LambdaMUD server using Django

* Use the [sprint challenge instructions for Intro to Django](https://github.com/LambdaSchool/Sprint-Challenge--Django-I).
* Add environment variables to heroku using `heroku config:set KEY=VALUE`
  * It is recommended that if you are having trouble (e.g. 500 server errors) to set
    ```
    DEBUG=TRUE
    ```
    to get more information.
* Run the code in create_world.py on your heroku server (`heroku run python manage.py shell`)

You can consider Pusher websocket integration to be a stretch goal. Your server should interact with your team's client.

#### 3. Create an interesting world on the server

To create your world, you will need to [add rooms](https://github.com/LambdaSchool/CS-Build-Week-1/blob/master/util/create_world.py) to your server. You will need to create more rooms and descriptions to build a unique, traversable world that your client apps can interact with via REST API calls.

Your world should contain a MINIMUM of 100 connected rooms.

You will also need to implement a GET `rooms` API endpoint for clients to fetch all rooms to display a map on the frontend.

#### 4. STRETCH: Implement server push alerts and chat using the Pusher websocket library

More on Pusher below.

### Client

#### 1. Deploy a LambdaMUD client that connects to the test server

While your backend developers are implementing your production server, you may test your endpoints on the test server hosted at `https://lambda-mud-test.herokuapp.com/`. You can use this to test your interface for account registration, login, movement and map display. (See sample API commands below.) Your app should store the user's auth token upon successful registration/authentication and use it to authenticate subsequent API requests.

#### 2. Connect your LambdaMUD client to the production server

Once your backend is up and running, you should be able to swap out the test host URL for your production URL and interact with your production server.

#### 3. Display a visual map of the world

Your backend should implement a `rooms` endpoint which will return data for every room in your world. Your job will be to build a map to display a map of those rooms, along with relevant information, like marking which room the player is currently in.

#### 4. STRETCH: Implement client "hearing" (Brady walks in from the north) and chat using the Pusher websocket library.

More on Pusher below.


## API Requirements

These are implemented on the test server: `https://lambda-mud-test.herokuapp.com/`.

### Registration
* `curl -X POST -H "Content-Type: application/json" -d '{"username":"testuser", "password1":"testpassword", "password2":"testpassword"}' localhost:8000/api/registration/`
* Response:
  * `{"key":"6b7b9d0f33bd76e75b0a52433f268d3037e42e66"}`

### Login
* Request:
  * `curl -X POST -H "Content-Type: application/json" -d '{"username":"testuser", "password":"testpassword"}' localhost:8000/api/login/`
* Response:
  * `{"key":"6b7b9d0f33bd76e75b0a52433f268d3037e42e66"}`

### Initialize
* Request:  (Replace token string with logged in user's auth token)
  * `curl -X GET -H 'Authorization: Token 6b7b9d0f33bd76e75b0a52433f268d3037e42e66' localhost:8000/api/adv/init/`
* Response:
  * `{"uuid": "c3ee7f04-5137-427e-8591-7fcf0557dd7b", "name": "testuser", "title": "Outside Cave Entrance", "description": "North of you, the cave mount beckons", "players": []}`

### Move
* Request:  (Replace token string with logged in user's auth token)
  * `curl -X POST -H 'Authorization: Token 6b7b9d0f33bd76e75b0a52433f268d3037e42e66' -H "Content-Type: application/json" -d '{"direction":"n"}' localhost:8000/api/adv/move/`
* Response:
  * `{"name": "testuser", "title": "Foyer", "description": "Dim light filters in from the south. Dusty\npassages run north and east.", "players": [], "error_msg": ""}`
* Pusher broadcast (stretch):
  * Players in previous room receive a message: `<name> has walked north.`
  * Players in next room receive a message: `<name> has entered from the south.`

### Say (stretch)
* Request:  (Replace token string with logged in user's auth token)
  * `curl -X POST -H 'Authorization: Token 6b7b9d0f33bd76e75b0a52433f268d3037e42e66' -H "Content-Type: application/json" -d '{"message":"Hello, world!"}' localhost:8000/api/adv/say/`
* Pusher broadcast:
  * Players in current room receive a message: `<name> says "Hello, world!"`

## Pusher

WebSocket is a computer communications protocol, providing full-duplex communication channels over a single TCP connection. You may use the Pusher service to handle the WebSocket connections as a stretch goal for your project. You can read more about them [here](https://pusher.com/websockets).


## Loading the server

Note that all the Pusher parts are stretch.

### Set up a Pusher account
* Sign up for a free account on pusher.com
* Create a new app
* Take note of your credentials
  * app_id, key, secret, cluster
* Look through the provided sample code and documentation


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

## FAQs and Troubleshooting

### 1. Can you show me an example of a map visualization?

Here's a sample project created by [a team in CSPT2](https://confident-wright-ca0176.netlify.com): 

![Lambda MUD 1](img/pt2_lambdamud.png)

And here's [a FT team](https://lambdaschool.com/lab-demos/lambda-mud) that went above and beyond with their use of graphics:

![Lambda MUD 2](img/ex_lambdamud.png)

And here's an example on iOS:

![Lambda MUD Mobile](img/ios_lambdamud.jpg)

### 2. How do I build something like that?

Think about the algorithm to draw your map. It will probably be something like this:

```
def draw_map():
    # Get all rooms
    # For each room in rooms...
        # Draw the room
        # Draw each exit
```

What data do you need to implement this? A list of rooms, their exits, maybe their positions? The server should return all the information you need from the `rooms` endpoint. Note that backend developers may need to define some fields in the `Room` model that do not exist yet.

### 3. How do I "create an interesting world"?

I'll leave that to you to determine.


### 4. What is Pusher?

Pusher is a cross-platform websocket library. This will allow you to turn your app into a real MUD with live push notifications to your client. You can consider integration to be a stretch goal but it's worth the effort if you have the time: websockets are powerful!


### 5. What will the `rooms` API endpoint look like?

It's up to you what data the request will return but the API request should be something like this:

```
curl -X GET -H 'Authorization: Token cc504e88ef659843b858d61c101ca9d4f0edf979' http://lambda-mud-test.herokuapp.com/api/adv/rooms/
```

