import json
import time
from fastapi import APIRouter
from fastapi import Header, Depends
from sqlalchemy import text
import pandas as pd
from core.dbs import curn
from models.projectinfo import Regions

addField = APIRouter(tags=["接口字段相关"])


@addField.post("/addfield", summary="添加接口字段")
async def adi(regi: Regions):
    regis = regi.dict()
    field_names = regis["field_names"]
    musts = regis["musts"]
    categroys= regis["categroys"]
    inter_format = regis["inter_format"]
    regions = regis["regions"]
    remarks = regis["remarks"]
    iid = regis["iid"]
    sql = "insert into inter_detail_region (field_name, musts, categgroy, encry_method, regin, remark, inters_id) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(field_names, musts, categroys, inter_format, regions, remarks, iid)
    curn.execute(text(sql))
    return {"message": "添加成功"}


@addField.get("/getfield", summary="查询接口字段列表")
async def gtia(id: int):
    field_list = []
    sql_pj = "SELECT id, create_time, del_flag, field_name, musts, categgroy, encry_method, regin, remark FROM inter_detail_region where inters_id={}".format(id)
    inters = pd.read_sql(text(sql_pj), con=curn)
    inters_json_region = inters.to_json(orient='records', force_ascii=False)
    inters_json_region_list = json.loads(inters_json_region)
    for ijrl in inters_json_region_list:
        field_dict = {}
        field_dict["field_name"] = ijrl["field_name"]
        field_dict["categroys"] = ijrl["categgroy"]
        field_dict["remarks"] = ijrl["remark"]
        field_dict["id"] = ijrl["id"]
        field_dict["regions"] = ijrl["regin"]
        if ijrl["musts"] == "1":
            field_dict["musts"] = "必填"
        if ijrl["musts"] == "2":
            field_dict["musts"] = "非必填"
        if ijrl["encry_method"] == "无":
            field_dict["encry_method"] = "无需加密"
        field_dict["desc"] = "该参数加密方式为{},需符合{}正则".format(field_dict["encry_method"], ijrl["regin"])
        field_list.append(field_dict)
    return {"data": field_list}