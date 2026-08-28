class LogFileParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.line_count = 0
        self.error_count = 0
        self.unique_words = set()

    def parse(self):
        try: 
            with open(self.file_path, "r") as f:
                #log_data = f.readlines()
                self.line_count = 0
                self.error_count = 0
                self.unique_words = set()
                for line in f:
                    self.line_count += 1
                    if "ERROR" in line:
                        self.error_count += 1
                    print(f"{line.strip()}")
                    self.unique_words.update(line.split())
            print(f"\nTotal lines in log file: {self.line_count}")
            print(f"\nERROR lines in log file: {self.error_count}")
            print(f"\nAll unique words: {self.unique_words}")
        except FileNotFoundError:
            print("Log file not found.")
            #log_data = []
            #f = []
        except PermissionError:
            print("\nPermission denied to read the log file.")
        except Exception as e:
            print(f"\nAn error occurred while reading the log file: {e}")
        finally:
            print(f"\nLog parsing completed for {self.file_path}\n")
    def error_rate(self):
        if self.line_count == 0:
            return 0
        return (self.error_count / self.line_count) *100

my_log_file = LogFileParser("C:\\ai_journey\\python_journery\\week2\\server.log")
my_log_file.parse()
print (f"Log file: {my_log_file.file_path}, Total lines: {my_log_file.line_count}, ERROR lines: {my_log_file.error_count}, Error rate: {my_log_file.error_rate():.2f}%  ")