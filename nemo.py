# We import Flask
from flask import Flask
# We import Nemo
from flask.ext.nemo import Nemo
# We create an application. You can simply use your own
app = Flask(
    __name__
)
# We register a Nemo object with the minimal settings
nemo = Nemo(
    # API URL is the URL of your endpoint.
    api_url="http://services2.perseids.org/exist/restxq/cts",
    # We set up the base url to be empty. If you want nemo to be on a
    # subpath called "cts", you would have
    # base_url="cts",
    base_url="",
    name="nemo",
    # In our case, we have an inventory named "nemo"
    inventory="nemo"#,
    # We give thee ap object
    #app=app
)
nemo.init_app(app)
# We register its routes
nemo.register_routes()
# We register its filters
nemo.register_filters()
# app.debug = True
