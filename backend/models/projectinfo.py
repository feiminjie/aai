from typing import Union, Optional
from pydantic import BaseModel, Field


class Projects(BaseModel):
    project_name: str
    project_url: str
    remarks: str = Field("")


class Inters(BaseModel):
    inter_name: str
    inter_url: str
    inter_methods: str
    inter_format: str
    inter_category: str
    inter_token: str
    remarks: str = Field("")
    pid: str

class Regions(BaseModel):
    field_names: str = Field("")
    musts: str
    categroys: str = Field("")
    inter_format: str
    regions: str
    remarks: str = Field("")
    iid: str