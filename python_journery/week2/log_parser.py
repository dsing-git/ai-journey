from pathlib import Path

log_dir = Path("C:\\ai_journey\\python_journery\\week2")

for log_file in log_dir.glob("*.log"):
    print(f"Found log file: {log_file.name}\n")

    try: 
        with open(log_file, "r") as f:
            #log_data = f.readlines()
            line_count = 0
            error_count = 0
            unique_words = set()
            for line in f:
                line_count += 1
                if "ERROR" in line:
                    error_count += 1
                print(f"{line.strip()}")
                unique_words.update(line.split())
        print(f"\nTotal lines in log file: {line_count}")
        print(f"\nERROR lines in log file: {error_count}")
        print(f"\nAll unique words: {unique_words}")
    except FileNotFoundError:
        print("Log file not found.")
        #log_data = []
        #f = []
    except PermissionError:
        print("\nPermission denied to read the log file.")
    except Exception as e:
        print(f"\nAn error occurred while reading the log file: {e}")
    finally:
        print(f"\nLog parsing completed for {log_file.name}\n")