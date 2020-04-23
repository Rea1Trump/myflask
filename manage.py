from App import creatApp
from flask_script import Manager


app = creatApp()
manager = Manager(app)
manager.run()
