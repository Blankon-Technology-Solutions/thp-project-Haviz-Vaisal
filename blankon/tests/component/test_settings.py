from blankon.settings import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

REST_FRAMEWORK["TEST_REQUEST_DEFAULT_FORMAT"] = "json"
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",
        "TEST_CONFIG": {"expiry": 100500},
    }
}
