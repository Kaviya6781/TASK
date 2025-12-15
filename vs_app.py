USER_ID = 150
STATUS_CODE = 404

def check_status(code):
    return "operation successful" if code == 200 else "connection failed"

if __name__ == "__main__":
    result = check_status(STATUS_CODE)
    print(f"API Check Result: {result}")
    
