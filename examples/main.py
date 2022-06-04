from authapi import AuthAPI, AuthData
from cloudops_google_secretmanager import SecretManager


app_token = SecretManager(
    project_id="your-project-id",
    secret_id="your-secret-id",
)


auth_data = AuthData(
    client_id="your-client-id",
    client_secret="your-client-secret",
)


app = AuthAPI(
    name="Google Ads",
    auth_data=auth_data,
    token_secret=app_token,
)

app.debug = True


@app.route("/run", methods=["GET"])
def run():
    return "Hello World!"


if __name__ == "__main__":
    app.run(ssl_context="adhoc")
