import sentry_sdk
import os
import bottle
from sentry_sdk.integrations.bottle import BottleIntegration


sentry_dns = "https://df02d0130ad74253aeaae3b5975599a9@sentry.io/4568734"
app = bottle.Bottle()

sentry_sdk.init(
	dsn = sentry_dns,
    integrations = [BottleIntegration()]
)

@app.route('/')
def index():
	html = """
<!doctype html>
<html lang="ru">
  <head>
    <title>DZ D2_10</title>
  </head>
  <body>
    <div style="margin:0 30px;text-align:center;">
      <h1 style="font-size:50px;color:green;">
      Проверка ДЗ D2.10
      </h1>
      <p style="font-size:35px;color:blue;">Жмакните на ссылки расположенные ниже,<br \/>
      чтобы посмотреть работу данного сервера совместно с 
      <span style="font-size:45px;color:red;">SENTRY</span>.</p>
      <p style="font-size:50px;">
      <a href="/success">SUCCESS</a> | <a href="/fail">FAIL</a>
      </p>
    </div>
  </body>
</html>
"""
	return html

@app.route('/success')
def success():
	html = """
<!doctype html>
<html lang="ru">
  <head>
    <title>Страница SUCCESS</title>
  </head>
  <body>
    <div style="margin:0 30px;text-align:center;">
      <h1 style="font-size:35px;color:blue;">
      Страница SUCCESS работы сервера с 
      <span style="color:red;">SENTRY</span>!
      </h1>
      <p style="font-size:25px;color:green;">Если вы видите это сообщение, 
      значит данный сервер <br \/> передает журнал на платформу 
      <span style="font-size:45px;color:red;">SENTRY</span>.</p>
    </div>
  </body>
</html>
"""
	return html

@app.route('/fail')
def fail():
    raise RuntimeError("Сообщение об ошибке: RuntimeError")

if os.environ.get('APP_LOCATION') == 'heroku':
    bottle.run(app,
               host="0.0.0.0",
               port=int(os.environ.get("PORT", 5000)))
else:
    bottle.run(app,
               host='localhost',
               port=5000)