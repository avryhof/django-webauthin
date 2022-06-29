from base64 import b64decode

from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site

from webauthn import verify_authentication_response
from webauthn.helpers.exceptions import InvalidAuthenticationResponse
from webauthn.helpers.structs import AuthenticationCredential


from .models import AuthData


class WebAuthinBackend:
    def get_user(self, user_id):
        """Get a user by their primary key."""
        User = get_user_model()
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    def authenticate(self, request, credential: AuthenticationCredential):
        """Authenticate a user given a signed token."""
        encoded_challenge = request.session.get("challenge")
        if not encoded_challenge:
            return None

        challenge = b64decode(encoded_challenge)

        auth_data = AuthData.objects.filter(credential_id=credential.id).first()
        if not auth_data:
            return None

        site = get_current_site(request)
        hostname = site.domain.split(":")[0]

        try:
            authentication_verification = verify_authentication_response(
                credential=credential,
                expected_challenge=challenge,
                expected_rp_id=hostname,
                expected_origin=f"https://{site.domain}",
                credential_public_key=auth_data.public_key,
                credential_current_sign_count=auth_data.sign_count,
                require_user_verification=True,
            )
        except InvalidAuthenticationResponse:
            return None

        auth_data.set_sign_count(authentication_verification.new_sign_count)
        return auth_data.user
