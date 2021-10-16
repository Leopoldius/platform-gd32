from typing import List

class DatasheetPageParsingQuirk:
    pass

class OverwritePinAlternateInfoQuirk(DatasheetPageParsingQuirk):
    def __init__(self, pin_name:str, alternate_funcs: List[str]) -> None:
        super().__init__()
        self.pin_name = pin_name
        self.alternate_funcs = alternate_funcs

class OverwritePinAdditionalInfoQuirk(DatasheetPageParsingQuirk):
    def __init__(self, pin_name:str, additional_funcs_str: str) -> None:
        super().__init__()
        self.pin_name = pin_name
        self.additional_funcs_str = additional_funcs_str

class ParseUsingAreaQuirk(DatasheetPageParsingQuirk):
    def __init__(self, area) -> None:
        super().__init__()
        self.area = area
