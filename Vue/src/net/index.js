import {request} from "@/net/request";

export function login(formData) {

    return request({
        method: "POST",
        url: '/login/',
        data: formData
    })
}

export function getMenus() {

    return request({
        method: "GET",
        url: '/menus/'
    })
}
