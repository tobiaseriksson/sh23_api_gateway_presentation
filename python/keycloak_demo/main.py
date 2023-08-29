
import json
import logging

from flask import Flask, render_template, session
app = Flask(__name__)


from flask_oidc import OpenIDConnect

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.config.update({
    'SECRET_KEY': 'Q6HsCNDZO4BVJj0pSNv3F9ShJBqEHnTK',
    'TESTING': True,
    'DEBUG': True,
    'OIDC_CLIENT_SECRETS': 'client-secrets.json',
    'OIDC_ID_TOKEN_COOKIE_SECURE': False,
    'OIDC_USER_INFO_ENABLED': True,
    'OIDC_OPENID_REALM': 'SH23',
    'OIDC_SCOPES': ['openid', 'email', 'profile', 'typical-user-scope'],
    'OIDC_INTROSPECTION_AUTH_METHOD': 'client_secret_post'
})


oidc = OpenIDConnect(app)

@app.route('/')
def home():
   return render_template('index.html')


@app.route('/loggain')
@oidc.require_login
def kind_of_private():
    if oidc.user_loggedin:
        print("Keys:")
        for k in session.keys():
            print(k+" : "+str(session.get(k)))
        print("- - -")
        return ('Hej, %s, <br><a href="/hemlig">klicka för hemlig info</a> '
                '<br><a href="/logout">Log out</a>') % \
            oidc.user_getfield('preferred_username')
    else:
        return 'Welcome anonymous, <a href="/hemlig">Log in</a>'


@app.route('/hemlig')
@oidc.accept_token(scopes=['typical-user-scope'])
def top_secret():
   return render_template('hemlig.html')

@app.route('/loggaut')
def logout():
    """Performs local logout by removing the session cookie."""

    oidc.logout()
    return 'Hi, you have been logged out! <a href="/">Return</a>'


if __name__ == '__main__':
   app.run()