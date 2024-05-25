import os

class Error_Log_Monitor:
    def __init__(self):
        self.logs = []
        self.log_type_map = {}

    def add_log_entry(self, timestamp, log_type, severity):
        log_entry = (timestamp, log_type, severity)
        self.logs.append(log_entry)
        if log_type not in self.log_type_map:
            self.log_type_map[log_type] = []
        self.log_type_map[log_type].append(log_entry)

    def get_stats(self, log_entries):
        if not log_entries:
            return 'No output'

        min_severity = min(entry[2] for entry in log_entries)
        max_severity = max(entry[2] for entry in log_entries)
        mean_severity = sum(entry[2] for entry in log_entries) / len(log_entries)

        return f"Min: {min_severity:.2f}, Max: {max_severity:.2f}, Mean: {mean_severity:.6f}"

    def process_query(self, query, output_file):
        query_parts = query.split()
        log_entries = []

        if len(query_parts) == 2 and query_parts[0] == "2":
            log_type = query_parts[1]
            log_entries = self.log_type_map.get(log_type, [])
        elif len(query_parts) == 3:
            if query_parts[0] == "3" and query_parts[1] == "BEFORE":
                timestamp = int(query_parts[2])
                log_entries = [entry for entry in self.logs if entry[0] < timestamp]
            elif query_parts[0] == "3" and query_parts[1] == "AFTER":
                timestamp = int(query_parts[2])
                log_entries = [entry for entry in self.logs if entry[0] > timestamp]
        elif len(query_parts) == 4:
            log_type = query_parts[1]
            timestamp = int(query_parts[3])
            if query_parts[0] == "4" and query_parts[2] == "BEFORE":
                log_entries = [entry for entry in self.log_type_map.get(log_type, []) if entry[0] < timestamp]
            elif query_parts[0] == "4" and query_parts[2] == "AFTER":
                log_entries = [entry for entry in self.log_type_map.get(log_type, []) if entry[0] > timestamp]

        result = self.get_stats(log_entries)
        output_file.write(result + "\n" if result != "No output" else "No output\n")

if __name__ == "__main__":
    monitor = Error_Log_Monitor()

    input_file_path = "input.txt"
    output_file_path = "output.txt"

    if not os.path.exists(input_file_path):
        print(f"Input file '{input_file_path}' not found.")
    else:
        with open(input_file_path, "r") as input_file, open(output_file_path, "w") as output_file:
            for line in input_file:
                line = line.strip()
                if line.startswith("1"):
                    timestamp, log_type, severity = line.split(";")
                    monitor.add_log_entry(int(timestamp.strip()), log_type.strip(), float(severity.strip()))
                else:
                    monitor.process_query(line.strip(), output_file)