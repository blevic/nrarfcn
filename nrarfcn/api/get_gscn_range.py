from typing import Union
from nrarfcn.tables.applicable_ss_raster_fr1 import table_applicable_ss_raster_fr1
from nrarfcn.tables.applicable_ss_raster_fr2 import table_applicable_ss_raster_fr2


def get_gscn_range(band: Union[str, int]) -> tuple:
    table_fr1 = table_applicable_ss_raster_fr1()
    table_fr2 = table_applicable_ss_raster_fr2()

    return 0, 0
