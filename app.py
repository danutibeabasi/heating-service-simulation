from flask import Flask
from service_one_2000watts.api import create_routes as create_routes_2000watts
from service_two_750watts.api import create_routes as create_routes_750watts
from service_one_2000watts.controller import HeatingController as HeatingController2000Watts
from service_two_750watts.controller import HeatingController as HeatingController750Watts

app = Flask(__name__)

controller_2000watts = HeatingController2000Watts()
controller_750watts = HeatingController750Watts()

create_routes_2000watts(app, controller_2000watts)
create_routes_750watts(app, controller_750watts)

if __name__ == '__main__':
    app.run(debug=True)
