from authapi import authdata


class AuthData(authdata.AuthData):
    authorize_url: str = "https://www.facebook.com/dialog/oauth"
    access_token_url: str = "https://graph.facebook.com/oauth/access_token"
    scopes: list[str] = [
        "email",
        "public_profile",
    ]
