import { request } from "../utils/reqeusts";


export function addProjects(data) {
  return request({
    url: "/addp",
    method: "POST",
    data
  });
}

export function getPj() {
  return request({
    url: "/pj",
  });
}

export function addInter(data) {
  return request({
    url: "/addI",
    method: "POST",
    data
  });
}

export function getInter(params) {
  return request({
    url: "/gir",
    method: "GET",
    params
  });
}

// export function getInter(id) {
//   return request({
//     url: "/gir/" + id,
//     method: "GET",
//   });
// }

export function addField(data) {
  return request({
    url: "/addfield",
    method: "POST",
    data
  });
}

export function getField(params) {
  return request({
    url: "/getfield",
    method: "GET",
    params
  });
}