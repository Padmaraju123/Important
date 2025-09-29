import configparser


def getConfig():
    config_obj = configparser.ConfigParser()
    config_obj.read(r"C:\Users\HP\Documents\API_automation\Utilities\properties.ini")
    return  config_obj
