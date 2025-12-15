IS_FINAL_REPORT = True
USER_ID = 150
STATUS_CODE = 404
def check_status(code):
    return "operation successful" if code == 201 else "connection failed"
def print_completion():
    print("script execution finished")
if __name__ == "__main__":
    result = check_status(STATUS_CODE)
    print(f"API Check Result: {result}")
   if IS_FINAL_REPORT:
      print_completion()

    
