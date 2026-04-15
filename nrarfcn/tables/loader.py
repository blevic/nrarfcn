from importlib import import_module
from os.path import dirname
from pkgutil import iter_modules

from nrarfcn.tables.Table import Table


DEFAULT_RELEASE = 17
_RELEASE_PREFIX = 'rel'


def get_supported_releases() -> tuple:
    """Lists releases available under nrarfcn.tables."""
    releases = []

    for _, module_name, is_package in iter_modules([dirname(__file__)]):
        if not is_package or not module_name.startswith(_RELEASE_PREFIX):
            continue

        release = module_name[len(_RELEASE_PREFIX):]
        if release.isdigit():
            releases.append(int(release))

    return tuple(sorted(releases))


def get_table(table_id: str, release_3gpp: int = DEFAULT_RELEASE) -> Table:
    """Loads a 3GPP table by logical table id and release."""
    if not isinstance(release_3gpp, int):
        raise ValueError('3GPP release must be an integer.')

    module_path = 'nrarfcn.tables.rel{}.{}'.format(release_3gpp, table_id)
    factory_name = 'table_{}'.format(table_id)

    try:
        module = import_module(module_path)
    except ImportError as error:
        supported_releases = ', '.join(str(release) for release in get_supported_releases())
        raise ValueError(
            'Could not load table "{}" for 3GPP Rel {}. Supported releases: {}.'.format(
                table_id,
                release_3gpp,
                supported_releases or 'none'
            )
        ) from error

    try:
        table_factory = getattr(module, factory_name)
    except AttributeError as error:
        raise ValueError(
            'Table module "{}" does not expose "{}".'.format(module_path, factory_name)
        ) from error

    return table_factory()
