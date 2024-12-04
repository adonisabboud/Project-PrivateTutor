from openapi_server.impl.default_api_impl import DefaultApiImpl
from openapi_server.apis.default_api_base import BaseDefaultApi

# Register the subclass
BaseDefaultApi.subclasses.append(DefaultApiImpl)
