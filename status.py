from db import get_db

def get_status():
    light = get_db().execute(
        'SELECT * FROM luminosity'
        'ORDER BY timestamp DESC'
    ).fetchone()

    temperature = get_db().execute(
        'SELECT * FROM temperature'
        'ORDER BY timestamp DESC'
    ).fetchone()

    humidity = get_db().execute(
        'SELECT * FROM humidity'
        'ORDER BY timestamp DESC'
    ).fetchone()

    movement = get_db().execute(
        'SELECT * FROM movement'
        'ORDER BY timestamp DESC'
    ).fetchone()

    if light is None:
        return {'status': 'Get light data'}

    if temperature is None:
        return {'status': 'Get temperature data'}

    if humidity is None:
        return {'status': 'Get humidity data'}

    if movement is None:
        return {'status': 'Get humidity data'}

    return {
        'data': {
            'light': light['timestamp'],
            'temperature': temperature['timestamp'],
            'humidty': humidity['timestamp'],
            'movement': movement['timestamp']
        }
    }