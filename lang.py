def Lang_create(langt, com):
    langCommand = {"RU": "Команда", "EN": "Command"}
    langDescription = {"RU": "Описание", "EN": "Description"}
    langWeather = {"RU": "Погода", "EN": "Weather"}
    langWeatherCH = {"RU": "Узнать погоду", "EN": "Check the weather"}
    langO = {"RU": "Выбранна команда:", "EN": "Selected command:"}
    langfullscreen = {"RU": "Полный экран", "EN": "Fullscreen"}
    langfullscreendesc = {"RU": "Открыть в полный экран", "EN": "Fullscreen"}
    
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
        elif com == "fullscreen":
            out = langfullscreen.get(langt, "")
        elif com == "fullscreendesc":
            out = langfullscreendesc.get(langt, "")
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
        elif com == "fullscreen":
            out = langfullscreen.get(langt, "")
        elif com == "fullscreendesc":
            out = langfullscreendesc.get(langt, "")
        else:
            out = ""

    return out
