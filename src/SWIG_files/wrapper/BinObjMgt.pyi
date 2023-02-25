from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TColStd import *
from OCC.Core.TCollection import *
from OCC.Core.TDF import *
from OCC.Core.Storage import *

BinObjMgt_PByte = NewType('BinObjMgt_PByte', Standard_Byte)
BinObjMgt_PChar = NewType('BinObjMgt_PChar', str)
BinObjMgt_PExtChar = NewType('BinObjMgt_PExtChar', str)
BinObjMgt_PInteger = NewType('BinObjMgt_PInteger', Standard_Integer)
BinObjMgt_PReal = NewType('BinObjMgt_PReal', Standard_Real)
BinObjMgt_PShortReal = NewType('BinObjMgt_PShortReal', Standard_ShortReal)
BinObjMgt_SRelocationTable = NewType('BinObjMgt_SRelocationTable', TColStd_IndexedMapOfTransient)

class BinObjMgt_Persistent:
    @overload
    def __init__(self) -> None: ...
    def Destroy(self) -> None: ...
    def GetAsciiString(self, theValue: TCollection_AsciiString) -> BinObjMgt_Persistent: ...
    def GetBoolean(self) -> Tuple[BinObjMgt_Persistent, bool]: ...
    def GetByte(self, theValue: str) -> BinObjMgt_Persistent: ...
    def GetByteArray(self, theArray: BinObjMgt_PByte, theLength: int) -> BinObjMgt_Persistent: ...
    def GetCharArray(self, theArray: BinObjMgt_PChar, theLength: int) -> BinObjMgt_Persistent: ...
    def GetCharacter(self, theValue: str) -> BinObjMgt_Persistent: ...
    def GetExtCharArray(self, theArray: BinObjMgt_PExtChar, theLength: int) -> BinObjMgt_Persistent: ...
    def GetExtCharacter(self, theValue: Standard_ExtCharacter) -> BinObjMgt_Persistent: ...
    def GetExtendedString(self, theValue: TCollection_ExtendedString) -> BinObjMgt_Persistent: ...
    def GetGUID(self, theValue: Standard_GUID) -> BinObjMgt_Persistent: ...
    def GetIStream(self) -> False: ...
    def GetIntArray(self, theArray: BinObjMgt_PInteger, theLength: int) -> BinObjMgt_Persistent: ...
    def GetInteger(self) -> Tuple[BinObjMgt_Persistent, int]: ...
    def GetLabel(self, theDS: TDF_Data, theValue: TDF_Label) -> BinObjMgt_Persistent: ...
    def GetOStream(self) -> False: ...
    def GetReal(self) -> Tuple[BinObjMgt_Persistent, float]: ...
    def GetRealArray(self, theArray: BinObjMgt_PReal, theLength: int) -> BinObjMgt_Persistent: ...
    def GetShortReal(self, theValue: float) -> BinObjMgt_Persistent: ...
    def GetShortRealArray(self, theArray: BinObjMgt_PShortReal, theLength: int) -> BinObjMgt_Persistent: ...
    def Id(self) -> int: ...
    def Init(self) -> None: ...
    def IsDirect(self) -> bool: ...
    def IsError(self) -> bool: ...
    def IsOK(self) -> bool: ...
    def Length(self) -> int: ...
    def Position(self) -> int: ...
    def PutAsciiString(self, theValue: TCollection_AsciiString) -> BinObjMgt_Persistent: ...
    def PutBoolean(self, theValue: bool) -> BinObjMgt_Persistent: ...
    def PutByte(self, theValue: str) -> BinObjMgt_Persistent: ...
    def PutByteArray(self, theArray: BinObjMgt_PByte, theLength: int) -> BinObjMgt_Persistent: ...
    def PutCString(self, theValue: str) -> BinObjMgt_Persistent: ...
    def PutCharArray(self, theArray: BinObjMgt_PChar, theLength: int) -> BinObjMgt_Persistent: ...
    def PutCharacter(self, theValue: str) -> BinObjMgt_Persistent: ...
    def PutExtCharArray(self, theArray: BinObjMgt_PExtChar, theLength: int) -> BinObjMgt_Persistent: ...
    def PutExtCharacter(self, theValue: Standard_ExtCharacter) -> BinObjMgt_Persistent: ...
    def PutExtendedString(self, theValue: TCollection_ExtendedString) -> BinObjMgt_Persistent: ...
    def PutGUID(self, theValue: Standard_GUID) -> BinObjMgt_Persistent: ...
    def PutIntArray(self, theArray: BinObjMgt_PInteger, theLength: int) -> BinObjMgt_Persistent: ...
    def PutInteger(self, theValue: int) -> BinObjMgt_Persistent: ...
    def PutLabel(self, theValue: TDF_Label) -> BinObjMgt_Persistent: ...
    def PutReal(self, theValue: float) -> BinObjMgt_Persistent: ...
    def PutRealArray(self, theArray: BinObjMgt_PReal, theLength: int) -> BinObjMgt_Persistent: ...
    def PutShortReal(self, theValue: float) -> BinObjMgt_Persistent: ...
    def PutShortRealArray(self, theArray: BinObjMgt_PShortReal, theLength: int) -> BinObjMgt_Persistent: ...
    def SetId(self, theId: int) -> None: ...
    def SetPosition(self, thePos: int) -> bool: ...
    def SetTypeId(self, theId: int) -> None: ...
    def StreamStart(self) -> BinObjMgt_Position: ...
    def Truncate(self) -> None: ...
    def TypeId(self) -> int: ...

class BinObjMgt_RRelocationTable(TColStd_DataMapOfIntegerTransient):
    def Clear(self, doReleaseMemory: Optional[bool] = True) -> None: ...
    def GetHeaderData(self) -> Storage_HeaderData: ...
    def SetHeaderData(self, theHeaderData: Storage_HeaderData) -> None: ...

#classnotwrapped
class BinObjMgt_Position: ...

# harray1 classes
# harray2 classes
# hsequence classes

