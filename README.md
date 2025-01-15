
# Streamlit Tool


#### Установка зависимостей
```bash
pip install pdm
pdm install
```


Активация окружения
```bash
source .venv/bin/activate
```


Запуск на своей машине
```bash
python -m src.server
```


## Запуск через Docker

```bash
docker build -t streamlit_tool .
```

## Компиляция перевода 
### Пример
Написан новый код к примеру:
```asciidoc
some_info_text = 'Привет Мир!'
```
Для реализации перевода переходим в
```
src/ui/pages/locale/en/LC_MESSAGES/messages.po
```
Вставляем ключ и значение перевода

```asciidoc
msgid "Привет Мир!"
msgstr "Hello World!"
```

Компилируем изменения перевода запустив в терминале команду

```asciidoc
msginit -l en -i src/ui/pages/locale/messages.pot -o src/ui/pages/locale/en/LC_MESSAGES/messages.po

```

Изменяем наш код на
```asciidoc
some_info_text = _('Привет Мир!')

```
Теперь при выбора языка будет осуществлен перевод

### Более подробно о настройке мультиязычности 
https://chatgpt.com/share/678363ec-0a50-8001-9d7b-bbb2a8e8bd2f