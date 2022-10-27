from cloudops.secret_manager.google import GoogleSecret

from authapi import AuthAPI, AuthData

app_token = GoogleSecret(
    project_id="your-project-id",
    secret_id="your-secret-id",
)


auth_data = AuthData(
    client_id="your-client-id",
    client_secret="your-client-secret",
    authorize_url="https://accounts.google.com/o/oauth2/auth",
    access_token_url="https://accounts.google.com/o/oauth2/token",
    scopes=["openid", "email", "profile"],
)


app = AuthAPI(
    name="Auth API: Google",
    auth_data=auth_data,
    token_secret=app_token,
)

app.debug = True


@app.route("/run", methods=["GET"])
def run():
    return "Hello World!"


if __name__ == "__main__":
    app.run(ssl_context="adhoc")
