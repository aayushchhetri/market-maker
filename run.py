import os
import cf_deployment_tracker

from library._01_root import app

# Emit Bluemix deployment event
cf_deployment_tracker.track()


if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 8080))
    app.run(host=host, port=port)
