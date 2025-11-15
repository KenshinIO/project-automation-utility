import os
import time
import datetime

class FileManager:
    def __init__(self, base_path="."):
        self.base_path = base_path

    def create_directory(self, dir_name):
        path = os.path.join(self.base_path, dir_name)
        if not os.path.exists(path):
            os.makedirs(path)
            return f"Direktori dibuat: {path}"
        return f"Direktori sudah ada: {path}"

    def create_dummy_file(self, file_name, content=""):
        path = os.path.join(self.base_path, file_name)
        with open(path, 'w') as f:
            f.write(content)
        return f"Berkas dibuat: {path}"

    def cleanup_old_files(self, directory, days_old):
        cutoff_time = time.time() - (days_old * 86400)
        cleaned_count = 0
        target_path = os.path.join(self.base_path, directory)

        if not os.path.exists(target_path):
            return "Direktori tidak ditemukan."

        for filename in os.listdir(target_path):
            filepath = os.path.join(target_path, filename)
            if os.path.isfile(filepath):
                file_stat = os.stat(filepath)
                if file_stat.st_mtime < cutoff_time:
                    os.remove(filepath)
                    cleaned_count += 1
        return f"Pembersihan selesai. Dihapus {cleaned_count} berkas lama di {target_path}."

class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, function, args=(), schedule_type="immediate"):
        self.tasks.append({
            "name": name,
            "function": function,
            "args": args,
            "schedule": schedule_type
        })

    def run_tasks(self):
        results = []
        now = datetime.datetime.now()
        for task in self.tasks:
            if task["schedule"] == "immediate":
                try:
                    result = task["function"](*task["args"])
                    results.append(f"Tugas '{task['name']}' berhasil: {result}")
                except Exception as e:
                    results.append(f"Tugas '{task['name']}' gagal: {e}")
            elif task["schedule"] == "daily":
                results.append(f"Tugas harian '{task['name']}' dijadwalkan untuk dieksekusi oleh sistem cron eksternal.")
            else:
                results.append(f"Tipe jadwal tidak dikenal untuk tugas '{task['name']}'.")
        return results

def log_message(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] - {message}"
    return f"LOG: {log_entry}"

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    file_manager = FileManager(base_path=current_dir)
    scheduler = TaskScheduler()

    print(log_message("Memulai alat otomatisasi proyek."))

    print(file_manager.create_directory("proyek_logs"))
    print(file_manager.create_directory("proyek_cache"))

    dummy_content = "Ini adalah konten berkas dummy untuk pengujian."
    print(file_manager.create_dummy_file("proyek_logs/init_log.txt", log_message("Sistem diinisialisasi.")))
    print(file_manager.create_dummy_file("proyek_cache/temp_file_1.cache", dummy_content))

    time.sleep(1)

    print(file_manager.create_dummy_file("proyek_cache/temp_file_2.cache", dummy_content + " (baru)"))

    scheduler.add_task(
        name="Bersihkan Cache Lama",
        function=file_manager.cleanup_old_files,
        args=("proyek_cache", 0),
        schedule="immediate"
    )

    scheduler.add_task(
        name="Catat Status Harian",
        function=log_message,
        args=("Status harian dicatat.",),
        schedule="daily"
    )

    print("\n--- Menjalankan Tugas Segera ---")
    task_results = scheduler.run_tasks()
    for result in task_results:
        print(log_message(result))

    print(log_message("Otomatisasi proyek selesai."))