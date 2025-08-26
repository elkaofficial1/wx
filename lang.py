
def Lang_create(langt, com):
    langCommand = {"RU": "Команда", "EN": "Command"}
    langDescription = {"RU": "Описание", "EN": "Description"}
    langWeather = {"RU": "Погода", "EN": "Weather"}
    langWeatherCH = {"RU": "Узнать погоду", "EN": "Check the weather"}

    if langt == "EN":
        if com == "command":
            out = langCommand["EN"]
            
        elif com == "desc":
            out = langDescription["EN"]

        elif com == "weather":
            out = langWeather["EN"]

        elif com == "weatherCH":
            out = langWeatherCH["EN"]

    if langt == "RU":
        if com == "command":
            out = langCommand["RU"]
            
        elif com == "desc":
            out = langDescription["RU"]

        elif com == "weather":
            out = langWeather["RU"]

    return out
