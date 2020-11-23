import json
import os
from jsonschema import validate, ValidationError


class WelltoryEventCheck:
    def __init__(self):
        self.logs = []
        self.events = self.get_event_paths()
        self.schemas = self.get_schemas_paths()

    @staticmethod
    def get_event_paths():
        """
        Получение списка событий из папки events
        """
        _directory = "events"
        files = os.listdir(_directory)
        return ["events/" + file for file in files]

    @staticmethod
    def get_schemas_paths():
        """
        Получение списка схем из папки schemas
        """
        _directory = "schemas"
        files = os.listdir(_directory)
        return ["schemas/" + file for file in files]

    def scan(self, event):
        # Todo: в дальгейшем добавить некоторые осыбе случае, например "label_   selected" или None
        """
        Метод-распределитель, который в зависимости от типа event'а  выполяняет ту или иную валидацию
        """
        try:
            if self.get_event_type(event) == "cmarker_created": self.validation(event=event, schema=self.define_schema_for_event(event))
            elif self.get_event_type(event) == "label_selected": self.validation(event=event, schema=self.define_schema_for_event(event))
            elif self.get_event_type(event) == "sleep_created": self.validation(event=event, schema=self.define_schema_for_event(event))
            elif self.get_event_type(event) == "workout_created": self.validation(event=event, schema=self.define_schema_for_event(event))
            elif self.get_event_type(event) == "meditation_created":self.validation(event=event, schema=self.define_schema_for_event(event))

        except Exception as error:
            print(error)

    def validation(self, event: str, schema: str):
        error_messages = ""
        validation_result = False
        # Todo (в дальнейшем) модернизировать(заменить) метод для проверки каждого ключа (для детализированной проверки)
        """
        Этот метод осуществляет проверку: соответствует ли event соответствующей schem'е
        Делает запись в лог-файл

        @param event: json-файл события, которое будет анализироваться с помощью event_scheme
        @param schema:  schema-файл
        """
        try:
            with open(event, "r") as event_read_file:
                event_dict = json.load(event_read_file)

            with open(schema, "r") as schema_read_file:
                schema_dict = json.load(schema_read_file)
            try:
                validate(instance=event_dict, schema=schema_dict)
                validation_result = True
            except ValidationError as validation_error:
                error_message = validation_error.message
        except OSError as os_err:
            self.logs.append(f"Нету schema для {event} ( event type: {self.get_event_type(event)})")
            error_message = error_messages + os_err.strerror

        # save result
        self.logs.append({
            "event": event,
            "schema": schema if schema else "Нет подходящей схемы",
            "результат валидации": validation_result,
            "ошибки": error_message if error_message else None
        })

    def run_validation(self):
        for event in self.events:
            self.scan(event)

    def get_result(self):
        return self.logs

    def save_result(self, res):
        with open("log.txt", "w") as logfile:
            for line in res:
                logfile.write(str(line)+"\n")
        return True

    def define_schema_for_event(self, event):
        """
        Получаем имя схемы для текущего event'а
        """
        event_type = self.get_event_type(event)
        schemas_name = f"schemas/{event_type}.schema"
        return schemas_name

    def get_event_type(self, event):
        """
        Определяем тип события(event) из файла event
        """
        try:
            with open(event, "r") as event_read_file:
                event_instance_obj = json.load(event_read_file)
                try:
                    event_type = event_instance_obj.get("event", "None")
                except AttributeError:
                    self.logs.append(f"У {event} нет параметра event")
        except Exception as err:
            print("Error", err)

        return event_type


if __name__ == "__main__":
    wec = WelltoryEventCheck()
    wec.run_validation()
    result = wec.get_result()
    wec.save_result(result)




