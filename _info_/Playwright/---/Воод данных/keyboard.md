# Имитация клавиатуры в Playwright



### `.keyboard`
- Низкоуровневый API страницы (`page.keyboard`), а не метода локатора — работает с тем элементом, что **сейчас в фокусе**
- ℹ️ Перед использованием нужно вручную сфокусировать элемент через `.click()` или `.focus()`
- ℹ️ Позволяет эмулировать спецклавиши (`Enter`, `Tab`, `Backspace`, комбинации типа `Control+A`), а не только печать текста

```python
email_field.click()                       # фокус на элементе (через .click())
       или
email_field.focus()                       # фокус на элементе (через .focus())

page.keyboard.type('text')                # посимвольная печать
page.keyboard.type('text', delay=50)      # посимвольная печать с задержкой 50 ms между символами
page.keyboard.press('Enter')              # нажатие одной клавиши (Enter)
page.keyboard.press('Control+A')          # нажатие комбинации клавиш (Cntrol+A)
page.keyboard.down('Shift')               # зажать клавишу (Shift)
page.keyboard.up('Shift')                 # отпустить клавишу (Shift)
page.keyboard.insert_text('text')         # вставка текста без эмуляции нажатий (быстро, без событий keydown/keyup)
```

**Когда использовать:** нужно работать не с конкретным полем, а с клавиатурой "вообще" — горячие клавиши, навигация табами, spec-символы, комбинации.

---

### Комбинации клавиш
- ℹ️ Клавиши в комбинации соединяются через `+`, регистр не важен (`Control+A` = `control+a`)
- ℹ️ Модификаторы: `Control` (`Ctrl` на Windows/Linux), `Meta` (`Cmd` на macOS), `Shift`, `Alt`
- ℹ️ Для кроссплатформенных тестов вместо `Control`/`Meta` используй `ControlOrMeta` — Playwright сам подставит нужный модификатор под ОС

```python
page.keyboard.press('Control+A')          # выделить всё
page.keyboard.press('Control+C')          # копировать
page.keyboard.press('Control+V')          # вставить
page.keyboard.press('Control+X')          # вырезать
page.keyboard.press('Control+Z')          # отменить
page.keyboard.press('Control+Shift+Z')    # повторить (redo)
page.keyboard.press('Control+Backspace')  # удалить слово слева
page.keyboard.press('Shift+Home')         # выделить до начала строки
page.keyboard.press('Shift+End')          # выделить до конца строки
page.keyboard.press('Shift+ArrowRight')   # выделить один символ вправо
page.keyboard.press('ControlOrMeta+A')    # выделить всё (кроссплатформенно: Ctrl на Win/Linux, Cmd на macOS)
```

**Ручная эмуляция комбинации через `down`/`up`** (когда нужно удержать клавишу дольше одного действия):
```python
page.keyboard.down('Shift')
page.keyboard.press('ArrowRight')
page.keyboard.press('ArrowRight')         # выделить несколько символов подряд с зажатым Shift
page.keyboard.up('Shift')
```

---
