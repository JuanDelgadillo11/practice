# This name is defined by default.
from configparser import ConfigParser
config = ConfigParser()

# To read data changing a wrong value like all the path to use a relative one
# config.read("D:\WindRiver\Python\Automation2\Config.cfg") OLD VALUE
# config.read new value raiz .. / folder / file
config.read("./InputFile/Config.cfg")
print(config.get("Section1","username")) # Print the username value