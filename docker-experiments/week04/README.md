# Week04 — Containerization practice

Задача: изучить и расширить `docker-experiments/hello_app`.

Шаги:
- собрать образ: `docker build -t hello-app docker-experiments/hello_app`
- запустить: `docker run --rm -p 8080:8080 hello-app`
- добавить health endpoint `/health` в `hello_app` и проверить.
