from .CommonDto import CommonDto


class CompletedTaskDto(metaclass=CommonDto):
    csv_path: str
    img_base64: str
