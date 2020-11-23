# Welltory
Welltory.Тестовое задание

Скрипт выполняет анализ event-файлов на предмет соответсвия их структуры структуре соотвествующей schem'е.

Работа скрипта полностью автоматизирована.Для каждого event подбирается соотвествующий schema-файл.

Результаты работы ищите в log.txt

Закидывайте schema-файлы(.schema) в папку schemas. 

Закидывайте event-файлы(.json) в папку events.

##Примерный результат имеет вид:  

{'event': 'events/1eba2aa1-2acf-460d-91e6-55a8c3e3b7a3.json', 'schema': 'schemas/label_selected.schema', 'результат валидации': False, 'ошибки': "'id' is a required property"}

{'event': 'events/297e4dc6-07d1-420d-a5ae-e4aff3aedc19.json', 'schema': 'schemas/sleep_created.schema', 'результат валидации': False, 'ошибки': "'source' is a required property"}

У events/29f0bfa7-bd51-4d45-93be-f6ead1ae0b96.json нет параметра event

Нету schema для events/2e8ffd3c-dbda-42df-9901-b7a30869511a.json ( event type: meditation_created)

{'event': 'events/2e8ffd3c-dbda-42df-9901-b7a30869511a.json', 'schema': 'schemas/meditation_created.schema', 'результат валидации': False, 'ошибки': 'No such file or directory'}

{'event': 'events/3b4088ef-7521-4114-ac56-57c68632d431.json', 'schema': 'schemas/cmarker_created.schema', 'результат валидации': False, 'ошибки': "'cmarkers' is a required property"}

Нету schema для events/6b1984e5-4092-4279-9dce-bdaa831c7932.json ( event type: meditation_created)

{'event': 'events/6b1984e5-4092-4279-9dce-bdaa831c7932.json', 'schema': 'schemas/meditation_created.schema', 'результат валидации': False, 'ошибки': 'No such file or directory'}

{'event': 'events/bb998113-bc02-4cd1-9410-d9ae94f53eb0.json', 'schema': 'schemas/sleep_created.schema', 'результат валидации': False, 'ошибки': "'source' is a required property"}

Нету schema для events/c72d21cf-1152-4d8e-b649-e198149d5bbb.json ( event type: meditation_created)

{'event': 'events/c72d21cf-1152-4d8e-b649-e198149d5bbb.json', 'schema': 'schemas/meditation_created.schema', 'результат валидации': False, 'ошибки': 'No such file or directory'}

{'event': 'events/cc07e442-7986-4714-8fc2-ac2256690a90.json', 'schema': 'schemas/label_selected.schema', 'результат валидации': False, 'ошибки': "'id' is a required property"}

{'event': 'events/e2d760c3-7e10-4464-ab22-7fda6b5e2562.json', 'schema': 'schemas/cmarker_created.schema', 'результат валидации': False, 'ошибки': "'cmarkers' is a required property"}

{'event': 'events/f5656ff6-29e1-46b0-8d8a-ff77f9cc0953.json', 'schema': 'schemas/sleep_created.schema', 'результат валидации': False, 'ошибки': "'source' is a required property"}

{'event': 'events/fb1a0854-9535-404d-9bdd-9ec0abb6cd6c.json', 'schema': 'schemas/cmarker_created.schema', 'результат валидации': False, 'ошибки': "'cmarkers' is a required property"}

{'event': 'events/ffe6b214-d543-40a8-8da3-deb0dc5bbd8c.json', 'schema': 'schemas/cmarker_created.schema', 'результат валидации': False, 'ошибки': "'cmarkers' is a required property"}
