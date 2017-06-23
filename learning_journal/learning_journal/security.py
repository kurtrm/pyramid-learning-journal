"""Provide authorization and authentication for learning journal."""
from passlib.apps import custom_app_context as pwd_context
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.security import Allow
from pyramid.security import Everyone, Authenticated
from pyramid.session import SignedCookieSessionFactory
import os


class MyRoot(object):
    """Override the root class in the security file."""

    def __init__(self, request):
        """Init."""
        self.request = request

    __acl__ = [
        (Allow, Everyone, 'view'),
        (Allow, Authenticated, 'secret'),
    ]


def includeme(config):
    """Security related configuration."""
    auth_secret = os.environ.get('AUTH_SECRET', '')
    authn_policy = AuthTktAuthenticationPolicy(
        secret=auth_secret,
        hashalg='sha512'
    )
    config.set_authentication_policy(authn_policy)
    authz_policy = ACLAuthorizationPolicy()
    config.set_authorization_policy(authz_policy)
    config.set_root_factory(MyRoot)

    session_secret = os.environ.get('SESSION_SECRET', "")
    session_factory = SignedCookieSessionFactory(session_secret)
    config.set_session_factory(session_factory)
    config.set_default_csrf_options(require_csrf=True)

def check_credentials(username, password):
    """Check user credentials."""
    stored_username = os.environ.get('AUTH_USERNAME', '')
    stored_password = os.environ.get('AUTH_PASSWORD', '')
    is_authenticated = False
    if stored_username and stored_password:
        if username == stored_username:
            is_authenticated = pwd_context.verify(password, stored_password)
    return is_authenticated
