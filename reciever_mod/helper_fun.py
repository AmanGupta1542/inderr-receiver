from decouple import config

def get_env_data():
    print(config('IP',None))