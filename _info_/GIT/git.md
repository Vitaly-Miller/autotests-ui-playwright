# GIT

---
## Установка
```shell
brew install git
```
Проверка версии
```shell
git --version
```
---

## Основные команды Git

Установка имени пользователя
```shell
git config --global user.name "Ваше Имя"
```

Установка email
```shell
git config --global user.email "ваш@email.com"
```

Проверка текущих настроек
```shell
git config --list
```
---
Инициализация нового репозитория
```shell
git init
```

Клонирование существующего репозитория
```shell
git clone <URL-репозитория>
```

Добавление файлов в индекс
```shell
git add
```

Создание коммита
```shell
git commit -m "Сообщение коммита"
```

Просмотр состояния репозитория
```shell
git status
```

Просмотр истории коммитов
```shell
git log
```
```shell
git log --oneline
```

Сравнение изменений
```shell
git diff
```

Отмена изменений
```shell
git checkout -- <имя_файла>
```

---
Добавляет ссылку на удалённый репозиторий с именем origin
```shell
git remote add origin <URL-репозитория>
```

Добавляет ссылку на удалённый репозиторий с именем origin
```shell
git push origin <ветка>
```

Загружает изменения из указанной ветки удалённого репозитория и объединяет их с текущей веткой
```shell
git pull origin <ветка>
```

---
Создаёт новую ветку
```shell
git branch <имя_ветки>
```

Переключает вас на другую ветку
```shell
git checkout <имя_ветки>
```

Создание + переключение на новую ветку
```shell
git checkout -b <имя_ветки>
```

Объединяет изменения из указанной ветки в текущую ветку
```shell
git merge <имя_ветки>
```

Удаляет локальную ветку
```shell
git branch -d <имя_ветки>
```
---
