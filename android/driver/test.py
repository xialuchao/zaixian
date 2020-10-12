import yaml
def initDriver(key):
    driver_data = yaml.load(open("../data/driver.yaml"),Loader=yaml.FullLoader)
    for i in range(driver_data["androidnum"]):
        platform = str(driver_data['platform'])
        server = driver_data[key][i]['server']
        caps = driver_data[key][i]['caps'][platform]
        print("platform: " + platform)
        print("server: " + server)
        print(caps)
    print(driver_data)

initDriver("install_app")