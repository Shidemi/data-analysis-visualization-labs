# Технологии анализа и визуализации данных

| Работа | Тема | Основная среда | Датасеты |
| --- | --- | --- | --- |
| 1 | Настройка среды разработки и управление виртуальными окружениями | Anaconda Jupyter Notebook | Iris, Wine |
| 2 | Разведочный анализ данных | Anaconda Jupyter Notebook | Auto MPG, Palmer Penguins |

## Лабораторная работа 1

- [Отчёт для защиты](lab1/report.docx) — версия с титульным листом БГУ ФПМИ, результатами аудита, снимками и графиками.
- [Блокнот Anaconda](lab1/lab1_anaconda.ipynb) — исходные результаты работы с таблицами pandas, два графика и контрольное обучение модели.
- [HTML-экспорт](lab1/lab1_anaconda.html) — копия блокнота для просмотра в браузере.
- [CSV](lab1/data), [графики](lab1/figures) и [вывод команд](lab1/outputs), включая [список пакетов conda](lab1/outputs/03_conda_list_lab1_terminal.txt).
- [Блокнот Colab](lab1/lab1_colab.ipynb) — фактические версии пакетов и диагностика двух облачных сеансов.
- [Снимки экрана](lab1/screenshots) — Anaconda Navigator, версии библиотек, выбор среды и результаты GPU и TPU.

В сеансе Tesla T4 проверены пять библиотек и видеопамять 15 360 МиБ. В отдельном сеансе TPU v5e-1 JAX обнаружил одно устройство TPU v5 lite. Для проверки Navigator отдельно создано и активировано окружение `dp2_lab01_gui`. В нём через Navigator установлены seaborn и scikit-learn вместе с numpy, pandas и matplotlib-base.

### Запуск блокнота Anaconda

```bash
conda create -n lab1_terminal python=3.11 numpy pandas matplotlib seaborn scikit-learn notebook ipykernel
conda activate lab1_terminal
python -m ipykernel install --user --name lab1_terminal --display-name 'Python (lab1_terminal)'
cd lab1
jupyter notebook
```

Откройте `lab1_anaconda.ipynb` и выберите ядро **Python (lab1_terminal)**. Если окружение уже есть, начните с его активации. Для повторения облачной проверки загрузите `lab1_colab.ipynb` в Google Colab и запустите ячейки аудита в соответствующих сеансах GPU и TPU.

## Лабораторная работа 2

- [Отчёт для защиты](lab2/report.docx) — подробный разбор каждого этапа работы с кодом ячеек, фактическим выводом, снимками Jupyter, таблицами результатов и пояснениями к девяти графикам.
- [Блокнот Anaconda](lab2/lab2_anaconda.ipynb) — аудит, очистка, распределения, выбросы и корреляции. Выводы ячеек и графики сохранены в блокноте.
- [Исходные данные](lab2/data) — Auto MPG, R. Quinlan ([UCI, CC BY 4.0](https://doi.org/10.24432/C5859H)), и Palmer Penguins, A. M. Horst, A. P. Hill, K. B. Gorman ([palmerpenguins, CC0](https://allisonhorst.github.io/palmerpenguins/)).
- [Графики](lab2/figures) — распределения, диаграммы размаха, тепловые карты и диаграммы рассеяния.
- [Снимки экрана](lab2/screenshots) — ядро и версии библиотек, первичный аудит обоих наборов, очистка и сохранение результатов в Jupyter Notebook.
- [Таблицы результатов](lab2/outputs) — очищенные данные, матрицы корреляций Пирсона, границы и число выбросов по правилу IQR.

В Auto MPG шесть пропусков мощности заполнены медианой **93,5 л. с.** Сохранились все 398 строк, из которых 18 содержат статистические выбросы. В Palmer Penguins после удаления 11 неполных строк осталось 333 наблюдения. По общим границам IQR выбросов нет. Наиболее сильная связь в этом наборе — между длиной ласта и массой пингвина (**r = 0,873**).

### Запуск блокнота Anaconda

Используйте окружение `lab1_terminal` из первой работы. Если его ещё нет, создайте и зарегистрируйте ядро по инструкции выше. Затем из корня проекта выполните:

```bash
conda activate lab1_terminal
cd lab2
jupyter notebook
```

Откройте `lab2_anaconda.ipynb`, выберите **Python (lab1_terminal)** и выполните все ячейки. Блокнот загружает данные из локальных файлов и обновляет `figures/` и `outputs/`.

[Условия курса](AGENTS.md). Следующие работы размещаются в папках `lab3/`, `lab4/` и далее.
