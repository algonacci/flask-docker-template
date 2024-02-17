from flask_caching import Cache

cache = Cache()


def init_cache_app(app):
    cache.init_app(app, config={
        'CACHE_TYPE': app.config.get('CACHE_TYPE', 'SimpleCache'),
        'CACHE_DEFAULT_TIMEOUT': app.config.get('CACHE_DEFAULT_TIMEOUT', 300),
    })
