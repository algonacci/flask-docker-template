from dotenv import dotenv_values

config = dotenv_values(".env")

CONFIG = {
    "PROPAGATE_EXCEPTIONS": True,
    "API_TITLE": "REST API Documentation of Rangkuman ML",
    "API_VERSION": "v1",
    "OPENAPI_VERSION": "3.0.3",
    "OPENAPI_URL_PREFIX": "/",
    "OPENAPI_SWAGGER_UI_PATH": "/docs",
    "OPENAPI_SWAGGER_UI_URL": "https://cdn.jsdelivr.net/npm/swagger-ui-dist/",
    "SECRET_KEY": config["SECRET_KEY"],
    "API_SPEC_OPTIONS": {
        "security": [{"bearerAuth": []}],
        "components": {
            "securitySchemes": {
                "bearerAuth": {
                    "type": "http",
                    "scheme": "bearer",
                }
            }
        }
    },
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 300
}
