# AuthAPI

A Simple Python API for Authenticated Operations.

![landing_img](./docs/img/landing.png)

## Quickstart:

Let's assume you want to interact with Google Ads API.

1. Create a `app_secret.json` with the following information:

```json
{
    "client_id": "...",
    "client_secret": "..."
}
```

2. Upload `app_secret.json` to your Secret Manager. Let's assume it's Google Cloud's Secret Manager.

3. Create a `main.py` script and paste the following content.

```python
from authapi import AuthAPI
from authapi.providers.google.ads import AuthData
from cloudops_google_secretmanager import SecretManager


app_secret = SecretManager(
    project_id="...",
    secret_id="...",
)

app_token = SecretManager(
    project_id="...",
    secret_id="...",
)


auth_data = AuthData(**app_secret.pull())


app = AuthAPI(
    name="Auth API: Google",
    auth_data=auth_data,
    token_secret=app_token,
)

app.debug = True


@app.route("/run", methods=["GET", "POST"])
def run():
    token = app.get_token()
    # Do your stuff here
    return "Done!"


if __name__ == "__main__":
    app.run(ssl_context="adhoc")
```

4. Visit [https://127.0.0.1:5000/](https://127.0.0.1:5000/) to start the authentication process.

