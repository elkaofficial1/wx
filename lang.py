def Lang_create(langt, com):
    langCommand = {"RU": "Команда", "EN": "Command"}
    langDescription = {"RU": "Описание", "EN": "Description"}
    langWeather = {"RU": "Погода", "EN": "Weather"}
    langWeatherCH = {"RU": "Узнать погоду", "EN": "Check the weather"}
    langO = {"RU": "Выбранна команда:", "EN": "Selected command:"}

    if langt == "EN":
        if com == "command":
            out = langCommand.get(langt, "")
        elif com == "desc":
            out = langDescription.get(langt, "")
        elif com == "weather":
            out = langWeather.get(langt, "")
        elif com == "weatherCH":
            out = langWeatherCH.get(langt, "")
        elif com == "O":
            out = langO.get(langt, "")
        else:
            out = ""

    if langt == "RU":
        if com == "command":
            out = langCommand.get(langt, "")
        elif com == "desc":
            out = langDescription.get(langt, "")
        elif com == "weather":
            out = langWeather.get(langt, "")
        elif com == "weatherCH":
            out = langWeatherCH.get(langt, "")
        elif com == "out":
            out = langO.get(langt, "")
        else:
            out = ""

    return out
