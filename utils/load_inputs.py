def load_file(file_dir: str, filename: str) -> list[str]:
    with open(f'{file_dir}/{filename}', mode='r', encoding='utf-8') as file:
        raw_inputs = file.readlines()

    return raw_inputs


def load_matrix(raw_inputs: list[str], sep: str = None) -> list[list[str]]:
    return [list(line.strip(sep)) for line in raw_inputs]
