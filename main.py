from flask import Flask, request
from Src.Logics.storage_prototype import storage_prototype
from Src.settings_manager import settings_manager
from Src.Storage.storage import storage
from Src.errors import error_proxy
from Src.Logics.report_factory import report_factory
from Src.Logics.start_factory import start_factory
from datetime import datetime
from Src.Logics.storage_service import storage_service


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


@app.route("/api/storage/turns", methods = ["GET"] )
def get_turns():
    """ # Получить параметры
    args = request.args
    if "start_period" not in args.keys():
        return error_proxy.create_error_response(app, "Необходимо передать параметры: start_period, stop_period!", 500)
        
    if "stop_period" not in args.keys():
        return error_proxy.create_error_response(app, "Необходимо передать параметры: start_period, stop_period!", 500)
    
    start_date = datetime.strptime(args["start_period"], "%Y-%m-%d")
    stop_date = datetime.strptime(args["stop_period"], "%Y-%m-%d") """

    start_date = datetime.strptime('2024-01-01', "%Y-%m-%d")
    stop_date = datetime.strptime('2024-01-10', "%Y-%m-%d")
    
    source_data = start.storage.data[  storage.storage_transaction_key()   ]      
    data = storage_service( source_data   ).create_turns( start_date, stop_date )      
    result = storage_service.create_response( data, app )
    
    return result


@app.route("/api/storage/<nomenclature_id>/turns", methods = ["GET"])
def get_nomenclature_turns(nomenclature_id: str):
    nomenclature_id = int(nomenclature_id)
    manager = settings_manager()
    start = start_factory(manager.settings)
    start.create()

    transaction_key = storage.storage_transaction_key()
    transaction_data = start.storage.data[transaction_key]

    nomenclature_key = storage.nomenclature_key()
    nomenclature_data = start.storage.data[nomenclature_key][nomenclature_id]

    prototype = storage_prototype(transaction_data)
    result = prototype.nomenclature_filter(nomenclature_data)

    return storage_service.create_response(result.data, app)


if __name__ == "__main__":
    app.run(debug = True)