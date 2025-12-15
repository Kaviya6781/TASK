USER_ID = 100
STATUS_CODE = 200

def check_status(code):
    return "Success" if code == 200 else "Failure"

if __name__ == "__main__":
    result = check_status(STATUS_CODE)
    print(f"API Check Result: {result}")
    