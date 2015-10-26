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
    inventory="nemo",
    css=[
            # USE Own CSS
            "static/tei.pb.min.css",
            "static/ciham.css"
    ],
    js=[
            # use own js file to load a script to go from normalized edition to diplomatic one.
            "static/ciham.js"
    ],
    transform={
        "urn:cts:froLit:jns915.jns1856.ciham-fro1" : "static/ciham.xslt"
    },
    # We give thee ap object
    #app=app
    chunker={
        # The default chunker takes care of book, poem, lines
        # but it would be cool to have 30 lines group for Nemo
        "urn:cts:froLit:jns915.jns1856.ciham-fro1": lambda text, cb: [(reff.split(":")[-1], reff.split(":")[-1]) for reff in cb(1)],
        "default": Nemo.scheme_chunker  # lambda text, cb: Nemo.line_grouper(text, cb, 50),
    }
)
nemo.init_app(app)
# We register its routes
nemo.register_routes()
# We register its filters
nemo.register_filters()
# app.debug = True
