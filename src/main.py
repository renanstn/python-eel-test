import eel
from exposed_functions import send_data


eel.init('web')
eel.start('index.html', port=8001)
