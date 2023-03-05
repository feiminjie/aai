from fastapi import APIRouter
from fastapi import Header, Depends
from sqlalchemy import text

from core.dbs import curn
from models.projectinfo import Projects

addproj = APIRouter(tags=["添加项目相关"])


@addproj.post("/addp", summary="添加项目接口")
async def adp(proinfos: Projects):
    proinfo = proinfos.dict()
    pname = proinfo["project_name"]
    purl = proinfo["project_url"]
    remark = proinfo["remark"]
    sql = "insert into project_info (project_name, project_url, remark) VALUES ('{}', '{}', '{}')".format(pname, purl, remark)
    curn.execute(text(sql))
    curn.commit()
    return {"message": "添加成功"}
