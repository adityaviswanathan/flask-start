# gunicorn -b 127.0.0.1:5000 run:app  

import os
from server import app

def runserver():
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)
	
if __name__ == '__main__':
    runserver()   