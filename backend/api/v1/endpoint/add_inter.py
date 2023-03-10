import json
import time
from fastapi import APIRouter
from fastapi import Header, Depends
from sqlalchemy import text
import pandas as pd

from core.dbs import curn
from models.projectinfo import Inters

addInter = APIRouter(tags=["项目接口相关"])


@addInter.post("/addI", summary="添加接口")
async def adi(Inter: Inters):
    Inter = Inter.dict()
    Iname = Inter["inter_name"]
    Iurl = Inter["inter_url"]
    Iformat= Inter["inter_format"]
    Imethod = Inter["inter_methods"]
    Icate = Inter["inter_category"]
    Itoken = Inter["inter_token"]
    remark = Inter["remarks"]
    pid = Inter["pid"]
    sql = "insert into inters (inter_name, inter_url, request_method, request_form, inter_category, inter_token, remark, prj_id) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(Iname, Iurl, Imethod, Iformat, Icate, Itoken, remark, pid)
    curn.execute(text(sql))
    return {"message": "添加成功"}

@addInter.get("/gir", summary="查询接口列表")
async def gtia(id: int):
    sql_pj = "SELECT id, create_time, del_flag, inter_url, request_method, inter_name, inter_category, request_form, inter_token, remark FROM inters where prj_id={}".format(id)
    inters = pd.read_sql(text(sql_pj), con=curn)
    inters.loc[inters['inter_token'] == 1, 'inter_token'] = "是"
    inters.loc[inters['inter_token'] == 2, 'inter_token'] = "否"
    inters_json_in = inters.to_json(orient='records', force_ascii=False)
    inters_detail_in_list = json.loads(inters_json_in)
    return {"data": inters_detail_in_list}