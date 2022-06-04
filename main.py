from authapi import AuthAPI
from authapi.authdata.google.google import AuthData
from cloudops_google_secretmanager import SecretManager


app_token = SecretManager(
    project_id="sandbox-data-engineering",
    secret_id="test-token-secret",
)


auth_data = AuthData(
    client_id="9831457425-30r1pm7bq343l36rj1d24koov65jliha.apps.googleusercontent.com",
    client_secret="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",
)


app = AuthAPI(
    name="Google Ads",
    auth_data=auth_data,
    token_secret=app_token,
)

app.debug = True


@app.route("/run", methods=["GET", "POST"])
def run():
    return "Hello World!"


if __name__ == "__main__":
    app.run(ssl_context="adhoc")
