import hashlib

def calculate_md5(file_path):
    # 파일의 MD5 해시 값을 계산합니다.
    md5 = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                md5.update(chunk)
    except FileNotFoundError:
        print(f"파일을 찾을 수 없습니다: {file_path}")
        return None
    return md5.hexdigest()

def is_virus(file_path, virus_database):
    # 파일의 MD5 해시 값을 계산합니다.
    file_md5 = calculate_md5(file_path)
    if file_md5 is None:
        return False  # 파일을 찾을 수 없는 경우 악성 코드로 간주하지 않습니다.
    # 악성 코드 데이터베이스와 비교하여 악성 코드인지 확인합니다.
    if file_md5 in virus_database:
        return True
    return False

# 악성 코드 데이터베이스 예시
virus_database = {
    "e44f7404d89d6511c27d215d1df1a53f": "Trojan.Generic",
    "2f0e15902b0a6ef676f64c6b34363df3": "Ransomware.WannaCry",
    "9a3b4b4e37907ba47b08edff5d9f4b23": "Spyware.Keylogger",
    "5a0380c16550ff736535b97b5b779be9": "Backdoor.Pandora",
    "3ca25ae354e9736b5d8b81f2e5e2fa4a": "Adware.PopUpGenius",
    # 추가적인 악성 코드의 MD5 해시 값과 이름을 여기에 추가할 수 있습니다.
}

# 테스트할 파일 경로
file_path = "test_file.exe"

# 파일이 악성 코드인지 확인합니다.
if is_virus(file_path, virus_database):
    print("악성 코드가 감지되었습니다!")
else:
    print("악성 코드가 감지되지 않았습니다.")
