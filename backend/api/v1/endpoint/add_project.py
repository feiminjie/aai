import json
import time

from fastapi import APIRouter
from fastapi import Header, Depends
from sqlalchemy import text
import pandas as pd

from core.dbs import curn
from models.projectinfo import Projects

addproj = APIRouter(tags=["添加项目相关"])


@addproj.post("/addp", summary="添加项目")
async def adp(proinfos: Projects):
    proinfo = proinfos.dict()
    pname = proinfo["project_name"]
    purl = proinfo["project_url"]
    remark = proinfo["remarks"]
    sql = "insert into project_info (project_name, project_url, remark) VALUES ('{}', '{}', '{}')".format(pname, purl, remark)
    curn.execute(text(sql))
    return {"message": "添加成功"}

@addproj.get("/pj", summary="查询项目")
async def adp():
    sql_pj = "SELECT id, project_name, project_url, create_time, del_flag, remark FROM project_info"
    inters = pd.read_sql(text(sql_pj), con=curn)
    inters_json_in = inters.to_json(orient='records', force_ascii=False)
    inters_detail_in_list = json.loads(inters_json_in)
    return {"data": inters_detail_in_list}