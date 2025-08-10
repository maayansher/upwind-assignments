# generate_report.py

def parse_trace_log(log_path, report_path):
    keywords = ["open", "write", "connect", "execve"]

    try:
        with open(log_path, "r") as log_file:
            lines = log_file.readlines()
    except FileNotFoundError:
        print(f"Error: {log_path} not found. Please run the container with strace first.")
        return

    with open(report_path, "w") as report:
        report.write("Malware Analysis Report\n\n")
        for keyword in keywords:
            report.write(f"--- {keyword.upper()} ---\n")
            for line in lines:
                if keyword in line:
                    report.write(line)
            report.write("\n")

    print(f"Report generated: {report_path}")


if __name__ == "__main__":
    parse_trace_log("trace.log", "report.txt")
