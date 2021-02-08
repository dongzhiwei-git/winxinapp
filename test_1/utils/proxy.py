#
# import backend.settings
import backend


def proxy():
    if backend.settings.USE_PROXY:
        # add your proxy here
        return {}
    else:
        return {}