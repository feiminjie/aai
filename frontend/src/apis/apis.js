import { request } from "../utils/reqeusts";


export function addProjects(data) {
  return request({
    url: "/addp",
    methods: "POST",
    data: data
  });
}

export function getPj() {
  return request({
    url: "/ptj",
  });
}