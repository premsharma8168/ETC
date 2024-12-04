import requests
def get_location(ip_address="192.168.137.10"):
    try:
        url = f"http://ipinfo.io/{ip_address}/json"
        response = requests.get(url)
        data = response.json()

        location_info = {
            "IP": data.get("ip"),
            "City": data.get("city"),
            "Region": data.get("region"),
            "Country": data.get("country"),
            "Location": data.get("loc"),  # latitude,longitude
            "Org": data.get("org"),
            "Timezone": data.get("timezone")
        }
        return location_info

    except Exception as e:
        return {"Error": str(e)}

ip_address = "192.168.137.10"  
location = get_location(ip_address)
print(location)