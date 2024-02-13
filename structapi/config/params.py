from typing import Optional
from pydantic import BaseModel, ValidationError


class Item(BaseModel):
    title: str
    description: str | None = None
    price: float


class HyperParameter(BaseModel):
    """
    Hyper parameters for the training of Deep learning model
    """

    # -------------------------------------------------- Dataset
    path: str
    root_dir: str
    img_size: tuple[int, int]
    batch_size: int
    num_workers: int
    split_size: float
    mean: tuple[float, float, float]
    std: tuple[float, float, float]

    # -------------------------------------------------- Model
    model: str
    pretrained: Optional[str]
    ckpt: Optional[str]
    conf_thresh: float
    iou_thresh: float

    # -------------------------------------------------- Solver
    optimizer: str
    scheduler: str
    lr: float
    weight_decay: float


def get_config(**kwargs):
    try:
        return HyperParameter(**kwargs)
    except ValidationError as e:
        print(e)
