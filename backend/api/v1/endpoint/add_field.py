import json
import time
from fastapi import APIRouter
from fastapi import Header, Depends
from sqlalchemy import text
import pandas as pd
from core.dbs import curn
from models.projectinfo import Regions, upRegions, AddInRegions, UpInRegions, AddDateRegions, UpDateRegions, AddFileRegions, UpFileRegions, AddKeyRegions, UpKeyRegions

addField = APIRouter(tags=["接口字段相关"])


@addField.post("/addfield", summary="添加正则字段")
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


@addField.post("/upfield", summary="修改正则字段")
async def upi(regi: upRegions):
    regis = regi.dict()
    field_names = regis["field_names"]
    musts = regis["musts"]
    categroys= regis["categroys"]
    inter_format = regis["inter_format"]
    regions = regis["regions"]
    remarks = regis["remarks"]
    id = regis["id"]
    sql = "update inter_detail_region set field_name='{}', musts='{}', categgroy='{}', encry_method ='{}', regin='{}', remark='{}' where id={} ".format(field_names, musts, categroys, inter_format, regions, remarks, id)
    curn.execute(text(sql))
    return {"message": "修改成功"}


@addField.post("/addInfield", summary="添加文本输入框字段")
async def aif(aifg: AddInRegions):
    aifg = aifg.dict()
    field_names = aifg["field_names"]
    musts = aifg["musts"]
    categroys= aifg["categroys"]
    inter_format = aifg["inter_format"]
    longs = aifg["longs"]
    shorts = aifg["shorts"]
    chineses = aifg["chineses"]
    englishs = aifg["englishs"]
    numbers = aifg["numbers"]
    special_char = aifg["special_char"]
    disting = aifg["disting"]
    onlyone = aifg["onlyone"]
    remarks = aifg["remarks"]
    iid = aifg["iid"]
    sql = "insert into inter_detail_in (field_name, musts, categgroy, encry_method, lengths, short, chinese, english, numbers, special_char, disting, onlyone, remark, inters_id) " \
          "VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(field_names, musts, categroys, inter_format, longs, shorts, chineses, englishs, numbers, special_char, disting, onlyone, remarks, iid)
    curn.execute(text(sql))
    return {"message": "添加成功"}


@addField.post("/upInfield", summary="修改文本输入框字段")
async def uif(uifgs: UpInRegions):
    uifg = uifgs.dict()
    field_names = uifg["field_names"]
    musts = uifg["musts"]
    categroys= uifg["categroys"]
    inter_format = uifg["inter_format"]
    longs = uifg["longs"]
    shorts = uifg["shorts"]
    chineses = uifg["chineses"]
    englishs = uifg["englishs"]
    numbers = uifg["numbers"]
    special_char = uifg["special_char"]
    disting = uifg["disting"]
    onlyone = uifg["onlyone"]
    remarks = uifg["remarks"]
    id = uifg["id"]
    sql = "update inter_detail_in set field_name='{}', musts='{}', categgroy='{}', encry_method ='{}', longs='{}', shorts='{}', chineses='{}', englishs='{}', numbers='{}', special_char='{}'," \
          "disting='{}', onlyone='{}', remark='{}' where id={}".format(field_names, musts, categroys, inter_format, longs, shorts, chineses, englishs, numbers, special_char, disting, onlyone, remarks, id)
    curn.execute(text(sql))
    return {"message": "修改成功"}


@addField.post("/addDatefield", summary="添加日期框字段")
async def adf(adrfs: AddDateRegions):
    adrf = adrfs.dict()
    field_names = adrf["field_names"]
    musts = adrf["musts"]
    categroys= adrf["categroys"]
    futher_s = adrf["futher_s"]
    last_s = adrf["last_s"]
    now_s = adrf["now_s"]
    link_date = adrf["link_date"]
    remarks = adrf["remarks"]
    iid = adrf["iid"]
    sql = "insert into inter_detail_date (field_name, musts, categgroy, futher_s, last_s, now_s, link_date, remark, inters_id) VALUES " \
          "('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(field_names, musts, categroys, futher_s, last_s, now_s, link_date, remarks, iid)
    curn.execute(text(sql))
    return {"message": "修改成功"}


@addField.post("/upDatefield", summary="修改日期框字段")
async def udf(udrfs: UpDateRegions):
    udrf = udrfs.dict()
    field_names = udrf["field_names"]
    musts = udrf["musts"]
    categroys= udrf["categroys"]
    futher_s = udrf["futher_s"]
    last_s = udrf["last_s"]
    now_s = udrf["now_s"]
    link_date = udrf["link_date"]
    remarks = udrf["remarks"]
    id = udrf["id"]
    sql = "update inter_detail_date set field_name='{}', musts='{}', categgroy='{}', futher_s ='{}', last_s='{}', now_s='{}', link_date='{}', remark='{}' where id={} ".format(field_names, musts, categroys, futher_s, last_s, now_s, link_date, remarks, id)
    curn.execute(text(sql))
    return {"message": "修改成功"}


@addField.post("/addfilefield", summary="添加文件字段")
async def aff(afris: AddFileRegions):
    afri = afris.dict()
    field_names = afri["field_names"]
    musts = afri["musts"]
    categroys= afri["categroys"]
    formats = afri["formats"]
    bigs = afri["bigs"]
    numbers = afri["numbers"]
    bases = afri["bases"]
    remarks = afri["remarks"]
    iid = afri["iid"]
    sql = "insert into inter_detail_file (field_name, musts, categgroy, futher_s, last_s, now_s, link_date, remark, inters_id) VALUES " \
          "('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(field_names, musts, categroys, formats, bigs, numbers, bases, remarks, iid)
    curn.execute(text(sql))
    return {"message": "修改成功"}


@addField.post("/upfilefield", summary="修改文件字段")
async def uff(ufris: UpFileRegions):
    ufri = ufris.dict()
    field_names = ufri["field_names"]
    musts = ufri["musts"]
    categroys= ufri["categroys"]
    formats = ufri["formats"]
    bigs = ufri["bigs"]
    numbers = ufri["numbers"]
    bases = ufri["bases"]
    remarks = ufri["remarks"]
    id = ufri["id"]
    sql = "update inter_detail_file set field_name='{}', musts='{}', categgroy='{}', formats ='{}', bigs='{}', numbers='{}', bases='{}', remark='{}' where id={} ".format(field_names, musts, categroys, formats, bigs, numbers, bases, remarks, id)
    curn.execute(text(sql))
    return {"message": "修改成功"}


@addField.post("/addkeyfield", summary="添加字典字段")
async def akf(regi: upRegions):
    regis = regi.dict()
    field_names = regis["field_names"]
    musts = regis["musts"]
    categroys= regis["categroys"]
    inter_format = regis["inter_format"]
    regions = regis["regions"]
    remarks = regis["remarks"]
    id = regis["id"]
    sql = "update inter_detail_region set field_name='{}', musts='{}', categgroy='{}', encry_method ='{}', regin='{}', remark='{}' where id={} ".format(field_names, musts, categroys, inter_format, regions, remarks, id)
    curn.execute(text(sql))
    return {"message": "修改成功"}


@addField.post("/upkeyfield", summary="修改字典字段")
async def ukf(regi: upRegions):
    regis = regi.dict()
    field_names = regis["field_names"]
    musts = regis["musts"]
    categroys= regis["categroys"]
    inter_format = regis["inter_format"]
    regions = regis["regions"]
    remarks = regis["remarks"]
    id = regis["id"]
    sql = "update inter_detail_region set field_name='{}', musts='{}', categgroy='{}', encry_method ='{}', regin='{}', remark='{}' where id={} ".format(field_names, musts, categroys, inter_format, regions, remarks, id)
    curn.execute(text(sql))
    return {"message": "修改成功"}


@addField.post("/addlinkfield", summary="添加关联字段")
async def alf(regi: upRegions):
    regis = regi.dict()
    field_names = regis["field_names"]
    musts = regis["musts"]
    categroys= regis["categroys"]
    inter_format = regis["inter_format"]
    regions = regis["regions"]
    remarks = regis["remarks"]
    id = regis["id"]
    sql = "update inter_detail_region set field_name='{}', musts='{}', categgroy='{}', encry_method ='{}', regin='{}', remark='{}' where id={} ".format(field_names, musts, categroys, inter_format, regions, remarks, id)
    curn.execute(text(sql))
    return {"message": "修改成功"}


@addField.post("/uplinkfield", summary="修改关联字段")
async def ulf(regi: upRegions):
    regis = regi.dict()
    field_names = regis["field_names"]
    musts = regis["musts"]
    categroys= regis["categroys"]
    inter_format = regis["inter_format"]
    regions = regis["regions"]
    remarks = regis["remarks"]
    id = regis["id"]
    sql = "update inter_detail_region set field_name='{}', musts='{}', categgroy='{}', encry_method ='{}', regin='{}', remark='{}' where id={} ".format(field_names, musts, categroys, inter_format, regions, remarks, id)
    curn.execute(text(sql))
    return {"message": "修改成功"}


@addField.post("/addmathfield", summary="添加数字输入框字段")
async def amf(regi: upRegions):
    regis = regi.dict()
    field_names = regis["field_names"]
    musts = regis["musts"]
    categroys= regis["categroys"]
    inter_format = regis["inter_format"]
    regions = regis["regions"]
    remarks = regis["remarks"]
    id = regis["id"]
    sql = "update inter_detail_region set field_name='{}', musts='{}', categgroy='{}', encry_method ='{}', regin='{}', remark='{}' where id={} ".format(field_names, musts, categroys, inter_format, regions, remarks, id)
    curn.execute(text(sql))
    return {"message": "修改成功"}


@addField.post("/upmathfield", summary="修改数字输入框字段")
async def umf(regi: upRegions):
    regis = regi.dict()
    field_names = regis["field_names"]
    musts = regis["musts"]
    categroys= regis["categroys"]
    inter_format = regis["inter_format"]
    regions = regis["regions"]
    remarks = regis["remarks"]
    id = regis["id"]
    sql = "update inter_detail_region set field_name='{}', musts='{}', categgroy='{}', encry_method ='{}', regin='{}', remark='{}' where id={} ".format(field_names, musts, categroys, inter_format, regions, remarks, id)
    curn.execute(text(sql))
    return {"message": "修改成功"}