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


class upRegions(BaseModel):
    field_names: str = Field("")
    musts: str
    categroys: str = Field("")
    inter_format: str
    regions: str
    remarks: str = Field("")
    id: str


class AddInRegions(BaseModel):
    field_names: str = Field("")
    musts: str
    categroys: str = Field("")
    inter_format: str
    longs: str
    shorts: str
    chineses: str
    englishs: str
    numbers: str
    special_char: str
    disting: str
    onlyone: str
    remarks: str
    iid: str


class UpInRegions(BaseModel):
    field_names: str = Field("")
    musts: str
    categroys: str = Field("")
    inter_format: str
    longs: str
    shorts: str
    chineses: str
    englishs: str
    numbers: str
    special_char: str
    disting: str
    onlyone: str
    remarks: str
    iid: str


class AddDateRegions(BaseModel):
    field_names: str = Field("")
    musts: str
    categroys: str = Field("")
    futher_s: str
    last_s: str
    now_s: str
    for_mat: str
    link_date: str
    remarks: str
    iid: str


class UpDateRegions(BaseModel):
    field_names: str = Field("")
    musts: str
    categroys: str = Field("")
    futher_s: str
    last_s: str
    now_s: str
    for_mat: str
    link_date: str
    remarks: str
    id: str


class AddFileRegions(BaseModel):
    field_names: str = Field("")
    musts: str
    categroys: str = Field("")
    formats: str
    bigs: str
    numbers: str
    bases: str
    remarks: str
    iid: str


class UpFileRegions(BaseModel):
    field_names: str = Field("")
    musts: str
    categroys: str = Field("")
    formats: str
    bigs: str
    numbers: str
    bases: str
    remarks: str
    id: str


class AddKeyRegions(BaseModel):
    field_names: str = Field("")
    musts: str
    categroys: str = Field("")
    key_dict: str
    remarks: str
    iid: str


class UpKeyRegions(BaseModel):
    field_names: str = Field("")
    musts: str
    categroys: str = Field("")
    key_dict: str
    remarks: str
    id: str