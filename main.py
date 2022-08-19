import threading
import conf
import requests
import json

sandbox = "https://10.10.20.14"
def obtener_token(usuario, clave):
    url = "https://10.10.20.14/api/aaaLogin.json"
    body = {
            "aaaUser": {
                "attributes": {
                    "name": usuario,
                    "pwd": clave
                }
            }
        }
    cabecera = {
            "Content-Type": "Application/json"
        }
    requests.packages.urllib3.disable_warnings()
    respuesta = requests.post(url, headers=cabecera, data=json.dumps(body), verify=False)
    token = respuesta.json()["imdata"][0]["aaaLogin"]["attributes"]["token"]
    return token

def top_system():
    cabecera = {
        "Content-Type": "application/json"
    }
    galleta = {
        "APIC-Cookie": obtener_token(conf.usuario, conf.clave)
    }
    requests.packages.urllib3.disable_warnings()
    respuesta = requests.get(sandbox+"/api/node/mo/topology/pod-1.json?query-target=children&target-subtree-class=fabricNode", headers=cabecera, cookies= galleta, verify=False)
    #print(respuesta.json())
    print("Equipo " + respuesta.json()["imdata"][0]["fabricNode"]['attributes']['name'])
    print("Direccion IP " + respuesta.json()["imdata"][0]["fabricNode"]['attributes']['address'])
    print("Estado " + respuesta.json()["imdata"][0]["fabricNode"]['attributes']['adSt'])
    print()
    print("Equipo " +respuesta.json()["imdata"][1]["fabricNode"]['attributes']['name'])
    print("Direccion IP " + respuesta.json()["imdata"][1]["fabricNode"]['attributes']['address'])
    print("Estado " + respuesta.json()["imdata"][1]["fabricNode"]['attributes']['adSt'])
    print()
    print("Equipo " + respuesta.json()["imdata"][2]["fabricNode"]['attributes']['name'])
    print("Direccion IP " + respuesta.json()["imdata"][2]["fabricNode"]['attributes']['address'])
    print("Estado " + respuesta.json()["imdata"][2]["fabricNode"]['attributes']['adSt'])
    print()
    print("Equipo " + respuesta.json()["imdata"][3]["fabricNode"]['attributes']['name'])
    print("Direccion IP " + respuesta.json()["imdata"][3]["fabricNode"]['attributes']['address'])
    print("Estado " + respuesta.json()["imdata"][3]["fabricNode"]['attributes']['adSt'])
    print()
    t = threading.Timer (300, top_system)
    t.start()
top_system()