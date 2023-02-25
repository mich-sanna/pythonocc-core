from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.Geom import *
from OCC.Core.Geom2d import *
from OCC.Core.Message import *


class geomtools:
    @staticmethod
    def GetUndefinedTypeHandler() -> GeomTools_UndefinedTypeHandler: ...
    @staticmethod
    def SetUndefinedTypeHandler(aHandler: GeomTools_UndefinedTypeHandler) -> None: ...

class GeomTools_Curve2dSet:
    def __init__(self) -> None: ...
    def Add(self, C: Geom2d_Curve) -> int: ...
    def Clear(self) -> None: ...
    def Curve2d(self, I: int) -> Geom2d_Curve: ...
    def Index(self, C: Geom2d_Curve) -> int: ...

class GeomTools_CurveSet:
    def __init__(self) -> None: ...
    def Add(self, C: Geom_Curve) -> int: ...
    def Clear(self) -> None: ...
    def Curve(self, I: int) -> Geom_Curve: ...
    def Index(self, C: Geom_Curve) -> int: ...

class GeomTools_SurfaceSet:
    def __init__(self) -> None: ...
    def Add(self, S: Geom_Surface) -> int: ...
    def Clear(self) -> None: ...
    def Index(self, S: Geom_Surface) -> int: ...
    def Surface(self, I: int) -> Geom_Surface: ...

class GeomTools_UndefinedTypeHandler(Standard_Transient):
    def __init__(self) -> None: ...

# harray1 classes
# harray2 classes
# hsequence classes

geomtools_Dump = geomtools.Dump
geomtools_Dump = geomtools.Dump
geomtools_Dump = geomtools.Dump
geomtools_GetReal = geomtools.GetReal
geomtools_GetUndefinedTypeHandler = geomtools.GetUndefinedTypeHandler
geomtools_Read = geomtools.Read
geomtools_Read = geomtools.Read
geomtools_Read = geomtools.Read
geomtools_SetUndefinedTypeHandler = geomtools.SetUndefinedTypeHandler
geomtools_Write = geomtools.Write
geomtools_Write = geomtools.Write
geomtools_Write = geomtools.Write
GeomTools_Curve2dSet_PrintCurve2d = GeomTools_Curve2dSet.PrintCurve2d
GeomTools_Curve2dSet_ReadCurve2d = GeomTools_Curve2dSet.ReadCurve2d
GeomTools_CurveSet_PrintCurve = GeomTools_CurveSet.PrintCurve
GeomTools_CurveSet_ReadCurve = GeomTools_CurveSet.ReadCurve
GeomTools_SurfaceSet_PrintSurface = GeomTools_SurfaceSet.PrintSurface
GeomTools_SurfaceSet_ReadSurface = GeomTools_SurfaceSet.ReadSurface
