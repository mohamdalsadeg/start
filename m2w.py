import json
import random

CONFIG_FILE = "config.json"

def shuffle_pools():
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as file:
            config = json.load(file)

        if "pools" not in config or not isinstance(config["pools"], list):
            print("❌ خطأ: لم يتم العثور على قائمة السيرفرات في config.json")
            return

        random.shuffle(config["pools"])

        with open(CONFIG_FILE, "w", encoding="utf-8") as file:
            json.dump(config, file, indent=4, ensure_ascii=False)

        print("✅")

    except Exception as e:
        print(f"❌ خطأ أثناء تعديل الملف: {e}")

if __name__ == "__main__":
    shuffle_pools()
