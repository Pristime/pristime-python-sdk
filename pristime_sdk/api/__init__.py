# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from pristime_sdk.api.health_api import HealthApi
    from pristime_sdk.api.workforce_scheduling_api import WorkforceSchedulingApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from pristime_sdk.api.health_api import HealthApi
from pristime_sdk.api.workforce_scheduling_api import WorkforceSchedulingApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
