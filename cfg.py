def read_config(file_name: str) -> dict[str, str]:
    ret = dict()
    with open(file_name) as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if not line or len(line) == 0 or line.startswith('#'):
                continue

            key, value = line.split('=')
            key = key.strip()
            value = value.strip()
            ret[key] = value
    return ret
