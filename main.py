from datetime import datetime
import json
from flask import Flask, request
from Src.settings_manager import settings_manager
from Src.Storage.storage import storage
from Src.errors import error_proxy
from Src.Logics.report_factory import report_factory
from Src.Logics.start_factory import start_factory
from Src.Logics.storage_prototype import storage_prototype
from Src.Logics.process_factory import process_factory
from Src.Logics.convert_factory import convert_factory


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

# Сформировать начальный набор данных
options = settings_manager() 
start = start_factory(options.settings)
start.create()


@app.route("/api/report/<storage_key>", methods = ["GET"])
def get_report(storage_key: str):
    """
        Сформировать отчет
    Args:
        storage_key (str): Ключ - тип данных: номенклатура, группы и т.д.
    """
    
    keys = storage.storage_keys( start.storage )
    if storage_key == "" or  storage_key not in keys:
        return error_proxy.create_error_response(app, f"Некорректный передан запрос! Необходимо передать: /api/report/<storage_key>. Список ключей (storage_key): {keys}.", 400)
    
    # Создаем фабрику
    report = report_factory()
    data = start.storage.data
    
    # Формируем результат
    try:
        result = report.create_response( options.settings.report_mode, data, storage_key, app )  
        return result
    except Exception as ex:
        return error_proxy.create_error_response(app, f"Ошибка при формировании отчета {ex}", 500)

@app.route("/api/storage/rests", methods = ["GET"])
def get_rests():
    args = request.args
    
    start_date = datetime.strptime('2024-01-01', '%Y-%m-%d')
    stop_date = datetime.strptime('2024-01-01', '%Y-%m-%d')

    prototype = storage_prototype(start.storage.data[storage.storage_transaction_key()])
    transactions = prototype.filter_date(start_date, stop_date)
    processing = process_factory().create(process_factory.turn_key())
    
    rests = processing().process(transactions.data)

    rests_data = convert_factory().serialize(rests)
    json_text = json.dumps(rests_data, sort_keys=True, indent=4, ensure_ascii=False)

    result = app.response_class(
            response = f"{json_text}",
            status = 200,
            mimetype = 'application/json; charset=utf-8'
        )
    
    return result

if __name__ == "__main__":
    app.run(debug = True)