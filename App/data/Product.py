from dataclasses import dataclass

@dataclass
class Product:
    title:str | None
    vendor:str | None
    price:str | None
    productKey:int | None