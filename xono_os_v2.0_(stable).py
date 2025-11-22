import time
from tqdm import tqdm
import os
import shutil, json
from datetime import datetime

# ==============================
# PATHS & FOLDER SETUP
# ==============================
BASE_FOLDER = os.path.expanduser("C:\\Users\\pasnsilu\\Documents\\XONO_OS_v2.0")
APPSAVES = os.path.join(BASE_FOLDER, "appsaves")
XONO_WRITER = os.path.join(BASE_FOLDER, "xonowriter")
RECYCLE_BIN = os.path.join(BASE_FOLDER, "RecycleBin")

# Make sure all folders exist
os.makedirs(BASE_FOLDER, exist_ok=True)
os.makedirs(APPSAVES, exist_ok=True)
os.makedirs(XONO_WRITER, exist_ok=True)
os.makedirs(RECYCLE_BIN, exist_ok=True)

MANIFEST_PATH = os.path.join(RECYCLE_BIN, "manifest.json")
if not os.path.exists(MANIFEST_PATH):
    with open(MANIFEST_PATH, "w", encoding="utf-8") as mf:
        json.dump([], mf, indent=2)

# ==============================
# BOOT SYSTEM
# ==============================
print("""╔════════════════╗
║   𝓧𝓞𝓝𝓞       ║
║   Terminal OS  ║
╚════════════════╝""")

print("---Welcome to XONO!", end="")
for _ in range(3):
    time.sleep(0.8)
    print("-", end="")

print("                            ")

print("Loading XONO OS...")
time.sleep(1)
print("✓ File Viewer")
time.sleep(0.7)
print("✓ Calculator")
time.sleep(0.7)
print("✓ Notepad")
time.sleep(0.7)
print("✓ Settings")
time.sleep(0.7)
print("✓ XONO Post")
time.sleep(0.7)
print("✓ XONO Store")
time.sleep(0.7)
print("✓ Command Prompt")
time.sleep(0.7)
print("✓ Recycle Bin")
time.sleep(0.7)
print("✓ XONO Office")
time.sleep(0.7)

print("\nSystem Ready ✔️")
time.sleep(1)
#########################

print("=== Welcome to XONO OS ===")

user_quit = ""  # (also corrected typo from "quite" to "quit")
while user_quit != "quit":
    print("\n==============================")
    print("         XONO Desktop         ")
    print("==============================")
    print("1. File Viewer")
    print("2. Calculator")
    print("3. Notepad")
    print("4. Settings")
    print("5. About your PC")
    print("6. XONO Post")
    print("7. XONO Store")
    print("8. Command Prompt")
    print("9. Recycle Bin")
    print("10. XONO Office")
    print("11. Shutdown")
    print("==============================")

    choice = input("Enter the app number to open: ")


    # These are the apps.

    #################
    def install(version, steps):
        print(f"\n🔄 Installing {version}...\n")
        for step in tqdm(steps, desc=f"Installing {version}", unit="step"):
            time.sleep(1)
            print(f"{step}")
        print(f"\n✅ {version} installed successfully!\n")
        time.sleep(0.7)
    #################

    #Recycl bin.
    def recycle_bin():
        RECYCLE_BIN = os.path.join(BASE_FOLDER, "RecycleBin")
        manifest_path = os.path.join(RECYCLE_BIN, "manifest.json")
        os.makedirs(RECYCLE_BIN, exist_ok=True)

        # Load manifest
        try:
            with open(manifest_path, "r", encoding="utf-8") as mf:
                manifest = json.load(mf)
        except (FileNotFoundError, json.JSONDecodeError):
            manifest = []

        while True:
            if not manifest:
                print("\n🗑️ Recycle Bin is empty!")
                input("Press Enter to return to Desktop...")
                break

            print("\n--- Recycle Bin ---")
            for i, entry in enumerate(manifest, start=1):
                print(f"{i}. {entry['original_name']} (deleted at {entry['deleted_at']})")

            print(f"{len(manifest) + 1}. Return to Desktop")
            choice = input("Select a file number to restore or delete: ")

            if choice.isdigit():
                num_choice = int(choice)
                if 1 <= num_choice <= len(manifest):
                    entry = manifest[num_choice - 1]
                    bin_path = os.path.join(RECYCLE_BIN, entry["bin_name"])

                    print(f"\nSelected: {entry['original_name']}")
                    action = input("Choose action - Restore (r) / Permanently Delete (d): ").lower()

                    if action == "r":
                        restore_path = entry["original_path"]
                        if os.path.exists(restore_path):
                            # Restore to correct folder type
                            if restore_path.endswith(".xdoc"):
                                restore_path = os.path.join(XONO_WRITER, entry["original_name"])
                                print("⚠️ Restoring to XONO Writer folder...")
                            else:
                                restore_path = os.path.join(APPSAVES, entry["original_name"])
                                print("⚠️ Restoring to appsaves folder...")

                        shutil.move(bin_path, restore_path)
                        print(f"✅ {entry['original_name']} restored successfully!")
                        manifest.pop(num_choice - 1)

                    elif action == "d":
                        os.remove(bin_path)
                        print(f"🗑️ {entry['original_name']} permanently deleted.")
                        manifest.pop(num_choice - 1)

                    else:
                        print("❌ Invalid action. Choose 'r' or 'd'.")

                    # Save updated manifest
                    with open(manifest_path, "w", encoding="utf-8") as mf:
                        json.dump(manifest, mf, indent=2)

                elif num_choice == len(manifest) + 1:
                    break
                else:
                    print("❌ Invalid choice.")
            else:
                print("❌ Please enter a number.")



    #XONO Store
    def xono_store():
        while True:
            print("1. Speed Boost")
            print("2. Graphic Upgrade")
            print("3. Security Upgrade")
            print("4. Battery Saver Pro")
            print("5. RAM Overdrive")
            print("6. AI Auto Optimizer")
            print("7. Ultra Processor Mode")
            print("8. FPS Booster X")
            print("9. Deep Clean Engine")
            print("                       ")
            print("10. Exit")
            store_choice = input("Enter the number of the performance to install: ")

            if store_choice == "1":
                install("Speed Boost", [
                    "Activating turbo core...",
                    "Optimizing CPU threads...",
                    "Removing slow bits...",
                    "Charging up performance...",
                    "Installing speed module...",
                    "Analyzing bottlenecks...",
                    "Adjusting fans...",
                    "Turbo mode check...",
                    "Compiling energy...",
                    "Boost algorithms loaded...",
                    "Clock speed upgraded...",
                    "Burning digital fuel...",
                    "Overclocking safely...",
                    "Warming up cores...",
                    "Speed limit removed...",
                    "Finalizing changes...",
                    "Stabilizing system...",
                    "Cooling turbo engine...",
                    "Sealing improvements...",
                    "Speed Boost complete!"
                ])

            if store_choice == "2":
                install("Graphic Upgrade", [
                "Loading pixels...",
                "Installing shaders...",
                "Enhancing resolution...",
                "Boosting GPU power...",
                "Drawing faster frames...",
                "Loading textures...",
                "Calibrating colors...",
                "Upgrading visual drivers...",
                "Anti-aliasing enabled...",
                "Smoothing edges...",
                "Rendering test frames...",
                "Frame rate optimized...",
                "Shadow engine updated...",
                "Lighting enhanced...",
                "3D mode activated...",
                "Polishing pixels...",
                "Retina mode added...",
                "Final render check...",
                "Saving visual config...",
                "Graphics Upgrade complete!"
            ])

            if store_choice == "3":
                install("Security Upgrade", [
                    "Scanning threats...",
                    "Building firewall...",
                    "Updating virus database...",
                    "Installing shields...",
                    "Encrypting data...",
                    "Securing ports...",
                    "Locking vulnerabilities...",
                    "Activating spy-trap...",
                    "Deep scan in progress...",
                    "Malware blocker loaded...",
                    "Spyware neutralized...",
                    "Defense system initialized...",
                    "Hacking detector active...",
                    "Creating vault walls...",
                    "Installing security guard AI...",
                    "Protecting secrets...",
                    "Threat level: Zero",
                    "Closing backdoors...",
                    "Activating final lock...",
                    "Security Shield installed!"
                ])

            if store_choice == "4":
                install("Battery Saver Pro", [
                    "Analyzing power usage...",
                    "Disabling unnecessary services...",
                    "Optimizing background tasks...",
                    "Switching to eco-mode...",
                    "Calibrating power cells...",
                    "Installing smart battery AI...",
                    "Reducing screen brightness...",
                    "Auto-managing app energy...",
                    "Upgrading battery drivers...",
                    "Saving charge profiles...",
                    "Scanning battery health...",
                    "Applying low-energy protocol...",
                    "Balancing performance and power...",
                    "Cooling battery unit...",
                    "Minimizing drain rate...",
                    "Blocking power-hungry apps...",
                    "Finalizing saver settings...",
                    "Locking power plan...",
                    "Green mode engaged...",
                    "Battery Saver Pro installed!"
                ])

            if store_choice == "5":
                install("RAM Overdrive", [
                    "Allocating extra memory blocks...",
                    "Clearing RAM cache...",
                    "Speeding up memory channels...",
                    "Enabling fast access mode...",
                    "Compressing data streams...",
                    "Optimizing memory paging...",
                    "Reducing latency timers...",
                    "Syncing RAM modules...",
                    "Testing memory bandwidth...",
                    "Upgrading RAM drivers...",
                    "Balancing load distribution...",
                    "Installing memory booster AI...",
                    "Enabling hyper-threading...",
                    "Adjusting timing cycles...",
                    "Locking memory frequency...",
                    "Flushing old data...",
                    "Increasing cache size...",
                    "Finalizing memory profile...",
                    "RAM Overdrive engaged!",
                    "Performance maximized!"
                ])

            if store_choice == "6":
                install("AI Auto Optimizer", [
                    "Booting AI core...",
                    "Analyzing system usage patterns...",
                    "Learning user habits...",
                    "Optimizing background processes...",
                    "Prioritizing active apps...",
                    "Managing resources dynamically...",
                    "Adjusting CPU load distribution...",
                    "Balancing power and performance...",
                    "Forecasting system demands...",
                    "Applying smart tweaks...",
                    "Reducing unnecessary tasks...",
                    "Updating AI knowledge base...",
                    "Enhancing decision algorithms...",
                    "Activating self-healing mode...",
                    "Debugging minor issues...",
                    "Reallocating memory pools...",
                    "Optimizing network bandwidth...",
                    "Verifying optimizations...",
                    "AI Auto Optimizer active!",
                    "System running smoothly!"
                ])

            if store_choice == "7":
                install("Ultra Processor Mode", [
                    "Unlocking processor cores...",
                    "Increasing clock frequency...",
                    "Recalibrating power supply...",
                    "Overclocking safely...",
                    "Boosting thread count...",
                    "Installing new firmware...",
                    "Enhancing instruction pipeline...",
                    "Loading ultra mode profiles...",
                    "Testing thermal limits...",
                    "Adjusting voltage regulators...",
                    "Syncing multi-core operations...",
                    "Reducing processing latency...",
                    "Activating turbo boost...",
                    "Finalizing processor tweaks...",
                    "Stabilizing clock speed...",
                    "Optimizing cache access...",
                    "Ensuring error correction...",
                    "Processor ready for ultra mode!",
                    "Performance unleashed!",
                    "Enjoy the power boost!"
                ])

            if store_choice == "8":
                install("FPS Booster X", [
                    "Closing background apps...",
                    "Allocating GPU resources...",
                    "Clearing frame buffer...",
                    "Optimizing game engine...",
                    "Boosting refresh rate...",
                    "Disabling unnecessary overlays...",
                    "Adjusting graphics settings...",
                    "Reducing input lag...",
                    "Increasing frame pacing...",
                    "Optimizing network latency...",
                    "Installing frame rate stabilizer...",
                    "Enabling V-Sync override...",
                    "Tuning GPU clocks...",
                    "Optimizing shader cache...",
                    "Preloading game assets...",
                    "Adjusting resolution scale...",
                    "Finalizing performance tweaks...",
                    "Running FPS diagnostics...",
                    "FPS Booster X activated!",
                    "Game ready to dominate!"
                ])

            if store_choice == "9":
                install("Deep Clean Engine", [
                    "Scanning junk files...",
                    "Clearing temp folders...",
                    "Removing cache data...",
                    "Deleting unused logs...",
                    "Cleaning browser history...",
                    "Optimizing disk space...",
                    "Deleting obsolete registry keys...",
                    "Removing startup clutter...",
                    "Clearing recycle bin...",
                    "Optimizing file system...",
                    "Compressing large files...",
                    "Removing duplicate files...",
                    "Scanning for malware traces...",
                    "Optimizing disk defragmentation...",
                    "Cleaning system restore points...",
                    "Purging old backups...",
                    "Verifying clean status...",
                    "Finalizing cleanup...",
                    "Deep Clean Engine ready!",
                    "System sparkling clean!"
                ])

            if store_choice == "10":
                print("Exiting XONO Store!")
                time.sleep(1.0)
                break

    # About app
    def about_xono():
        print("\n--- About XONO ---")
        print("XONO Terminal OS v2.0")
        print("Installed RAM: 8GB")
        print("Storage: 242GB")
        print("Processer: Intel(R) core(TM) i5-8250U CPU @ 1.60GHz")
        print("Graphic cards: 2GB")
        print("                       ")
        print("Device Specifications.")
        print("                       ")
        print("Device ID: 5481D081-271B-4EC5-92F7-48A0FBCD7AB")
        print("Product ID: 00331-207350-02293-AA460")
        print("System Type: 64-bit operating system, x64-based processor")
        print("                       ")
        print("XONO specifications")
        print("                       ")
        print("Edition: XONO Terminal edition.")
        print("Version: 01X2")
        print("OS build: 26100.45946")
        print("Experience: XONO Feature Experience Pack 1000.265100.197.0")
        print("--------------------\n")

    # ===============
    # NOTEPAD
    #================
    def notepad():
        print("\n--- Notepad ---")
        print("Type your note below. Type 'SAVE' on a new line to save the note.\n")

        lines = []
        while True:
            line = input()
            if line.upper() == "SAVE":
                break
            lines.append(line)

        note_content = "\n".join(lines)
        existing_notes = [f for f in os.listdir(APPSAVES) if f.endswith(".txt")]
        note_number = len(existing_notes) + 1
        note_file = os.path.join(APPSAVES, f"note{note_number}.txt")

        with open(note_file, "w", encoding="utf-8") as f:
            f.write(note_content)

        print(f"✅ Note saved as note{note_number}.txt in appsaves folder!")

    #Calculator
    def calculator():
        print("\n--- Calculator ---")
        print("Type 'quit' at any time to exit.\n")

        while True:
            num1 = input("Enter first number: ")
            if num1.lower() == "quit": break
            num2 = input("Enter second number: ")
            if num2.lower() == "quit": break
            op = input("Enter operation (+, -, *, /): ")
            if op.lower() == "quit": break

            try:
                n1, n2 = float(num1), float(num2)
            except ValueError:
                print("❌ Invalid number! Try again.")
                continue

            if op == "+": result = n1 + n2
            elif op == "-": result = n1 - n2
            elif op == "*": result = n1 * n2
            elif op == "/":
                if n2 == 0:
                    print("❌ Cannot divide by zero!")
                    continue
                result = n1 / n2
            else:
                print("❌ Invalid operation!")
                continue

            print("✅ Result:", result, "\n")

    
    def recycle_bin():
        # Load manifest
        try:
            with open(MANIFEST_PATH, "r", encoding="utf-8") as mf:
                manifest = json.load(mf)
        except (FileNotFoundError, json.JSONDecodeError):
            manifest = []

        while True:
            if not manifest:
                print("\n🗑️ Recycle Bin is empty!")
                input("Press Enter to return to Desktop...")
                break

            print("\n--- Recycle Bin ---")
            for i, entry in enumerate(manifest, start=1):
                print(f"{i}. {entry['original_name']} (deleted at {entry['deleted_at']})")
            print(f"{len(manifest)+1}. Return to Desktop")

            choice = input("Select a file number: ")

            if choice.isdigit():
                num_choice = int(choice)
                if 1 <= num_choice <= len(manifest):
                    entry = manifest[num_choice - 1]
                    bin_path = os.path.join(RECYCLE_BIN, entry["bin_name"])

                    print(f"\nSelected: {entry['original_name']}")
                    action = input("Restore (r) / Delete (d): ").lower()

                    if action == "r":
                        restore_folder = XONO_WRITER if entry["original_name"].endswith(".xdoc") else APPSAVES
                        shutil.move(bin_path, os.path.join(restore_folder, entry["original_name"]))
                        print(f"✅ Restored {entry['original_name']}!")
                        manifest.pop(num_choice - 1)

                    elif action == "d":
                        os.remove(bin_path)
                        print(f"🗑️ Permanently deleted {entry['original_name']}.")
                        manifest.pop(num_choice - 1)
                    else:
                        print("❌ Invalid choice.")

                    with open(MANIFEST_PATH, "w", encoding="utf-8") as mf:
                        json.dump(manifest, mf, indent=2)

                elif num_choice == len(manifest) + 1:
                    break
                else:
                    print("❌ Invalid choice.")
            else:
                print("❌ Please enter a number.")


    def file_viewer():
        try:
            with open(MANIFEST_PATH, "r", encoding="utf-8") as mf:
                manifest = json.load(mf)
        except (FileNotFoundError, json.JSONDecodeError):
            manifest = []

        while True:
            print("\n--- FILE VIEWER ---")
            files = []
            for folder in [APPSAVES, XONO_WRITER]:
                for f in os.listdir(folder):
                    if f.endswith(".txt") or f.endswith(".xdoc"):
                        files.append((folder, f))

            if not files:
                print("No files found!")
            else:
                for i, (_, file) in enumerate(files, start=1):
                    print(f"{i}. {file}")
            print(f"{len(files)+1}. Return to Desktop")

            choice = input("Enter number: ")

            if choice.isdigit():
                num_choice = int(choice)
                if 1 <= num_choice <= len(files):
                    folder, name = files[num_choice - 1]
                    filepath = os.path.join(folder, name)

                    with open(filepath, "r", encoding="utf-8") as f:
                        print("\n--- File Content ---")
                        print(f.read())
                        print("-------------------")

                    delete = input("Delete this file? (y/n): ").lower()
                    if delete == "y":
                        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                        bin_name = f"{name}_deleted_{timestamp}"
                        shutil.move(filepath, os.path.join(RECYCLE_BIN, bin_name))
                        manifest.append({
                            "original_name": name,
                            "bin_name": bin_name,
                            "deleted_at": datetime.now().isoformat()
                        })
                        with open(MANIFEST_PATH, "w", encoding="utf-8") as mf:
                            json.dump(manifest, mf, indent=2)
                        print("🗑️ File moved to Recycle Bin.")
                elif num_choice == len(files) + 1:
                    break
                else:
                    print("❌ Invalid choice.")
            else:
                print("❌ Please enter a number.")



    def run_update(version, steps):
        print(f"\n🔄 Installing {version}...\n")
        for step in tqdm(steps, desc=f"Updating {version}", unit="step"):
            time.sleep(1)  # 1 second per step = total 10 seconds for 10 steps
            print(f"{step}")
        print(f"\n✅ {version} installed successfully!\n")
        time.sleep(0.7)


    def settings():
        settings_data = {
            "theme": "Light",
            "username": "User",
            "sound": "On"
        }

        while True:
            print("\n--- XONO Settings ---")
            print("1. Change OS Theme")
            print("2. Change Username")
            print("3. Toggle Sound Effects")
            print("4. View Current Settings")
            print("5. XONO updates")
            print("6. Return to Desktop")

            set_choice = input("Choose an option: ")

            if set_choice == "1":
                print("\nChoose a theme:")
                print("1. Light")
                print("2. Dark")
                theme_choice = input("Enter your choice: ")

                if theme_choice == "1":
                    settings_data["theme"] = "Light"
                    print("✅ Theme changed to Light!")
                elif theme_choice == "2":
                    settings_data["theme"] = "Dark"
                    print("✅ Theme changed to Dark!")
                else:
                    print("❌ Invalid choice. Theme not changed.")

            elif set_choice == "2":
                print("=== Change Username ===")

                new_username = input("Enter your new username: ")

                print("✅ Username changed successfully!")

            elif set_choice == "3":
                current_sound = settings_data["sound"]
                print(f"\nCurrent sound setting: {current_sound}")
                toggle = input("Toggle sound? (y/n): ").lower()

                if toggle == "y":
                    if current_sound == "On":
                        settings_data["sound"] = "Off"
                        print("✅ Sound turned OFF.")
                    else:
                        settings_data["sound"] = "On"
                        print("✅ Sound turned ON.")
                else:
                    print("Sound setting unchanged.")

            elif set_choice == "4":
                print("\n--- Current Settings ---")
                for key, value in settings_data.items():
                    print(f"{key.capitalize()}: {value}")
                print("------------------------\n")
                input("Press Enter to return to the menu...")

            elif set_choice == "5":
                print("\n----- XONO Updates (v1.2) -----")
                print("1. XONO 1.7, version 702A7")
                print("2. XONO 1.7, version 713B8")
                print("3. XONO 1.7, version 724C9")
                print("4. XONO 1.7, version 735D2")
                print("5. XONO 1.7, version 746E3")
                print("6. XONO 1.7, version 757F4")
                print("7. XONO 1.7, version 768G5")

                update_enter = input("Enter a number (1-7): ")

                if update_enter == "1":
                    run_update("XONO 1, version 602A7", [
                        "Collecting files for Smart Dashboard",
                        "Installing Smart Dashboard UI",
                        "✓ Adding customizable widgets",
                        "✓ Optimizing desktop animations",
                        "✓ Configuring widget settings",
                        "✓ Testing widget responsiveness",
                        "✓ Integrating weather and clock widgets",
                        "✓ Finalizing widget placements",
                        "✓ Saving dashboard preferences",
                        "✓ Finishing setup"
                    ])

                elif update_enter == "2":
                    run_update("XONO 1, version 613B8", [
                        "Checking system requirements",
                        "Downloading Performance Patch",
                        "✓ Enhancing CPU usage",
                        "✓ Reducing background process load",
                        "✓ Updating thermal control settings",
                        "✓ Optimizing memory management",
                        "✓ Improving battery efficiency",
                        "✓ Refining disk access speeds",
                        "✓ Running performance tests",
                        "✓ Finalizing patch installation"
                    ])

                elif update_enter == "3":
                    run_update("XONO 1, version 624C9", [
                        "Preparing app manager module",
                        "Installing app manager UI",
                        "✓ Enabling uninstall feature",
                        "✓ Showing app sizes and usage",
                        "✓ Optimizing app launch speed",
                        "✓ Adding app sorting options",
                        "✓ Integrating search functionality",
                        "✓ Improving user interface",
                        "✓ Testing uninstall safety",
                        "✓ Completing installation"
                    ])

                elif update_enter == "4":
                    run_update("XONO 1, version 635D2", [
                        "Connecting to update servers",
                        "Downloading UI enhancements",
                        "✓ Installing new system icons",
                        "✓ Adding window transition effects",
                        "✓ Enabling light & dark mode switch",
                        "✓ Refining color schemes",
                        "✓ Improving font rendering",
                        "✓ Updating notification styles",
                        "✓ Running UI stability tests",
                        "✓ Completing UI upgrade"
                    ])

                elif update_enter == "5":
                    run_update("XONO 1, version 646E3", [
                        "Checking storage space",
                        "Installing Security Suite",
                        "✓ Adding firewall upgrade",
                        "✓ Enhancing anti-malware system",
                        "✓ Fixing permission bugs",
                        "✓ Updating encryption protocols",
                        "✓ Implementing login alerts",
                        "✓ Strengthening password policies",
                        "✓ Running security scans",
                        "✓ Finalizing security setup"
                    ])

                elif update_enter == "6":
                    run_update("XONO 1, version 657F4", [
                        "Collecting multimedia modules",
                        "Installing media improvements",
                        "✓ Improving audio drivers",
                        "✓ Boosting video performance",
                        "✓ Fixing screen resolution bugs",
                        "✓ Adding support for new codecs",
                        "✓ Enhancing media player UI",
                        "✓ Optimizing streaming quality",
                        "✓ Testing playback stability",
                        "✓ Finishing multimedia update"
                    ])

                elif update_enter == "7":
                    run_update("XONO 1, version 668G5", [
                        "Launching AI assistant setup",
                        "Downloading speech models",
                        "✓ Activating voice command feature",
                        "✓ Adding smart reply options",
                        "✓ Finalizing AI training",
                        "✓ Integrating assistant with apps",
                        "✓ Setting up privacy controls",
                        "✓ Testing voice recognition",
                        "✓ Improving response times",
                        "✓ Finalizing assistant installation"
                    ])

                else:
                    print("❌ Invalid input. Please enter a number from 1 to 7.")

            elif set_choice == "6":
                print("Returning to Desktop...")
                break

            else:
                print("❌ Invalid option. Please choose a number from 1 to 6.")

    #XONO Post
    sent_messages = []
    def xono_post():
        print("\n---XONO Post---")
        while True:
            print("\n--- XONO Mail Menu ---")
            print("1. Compose Message")
            print("2. View Sent Messages")
            print("3. Create a account")
            print("4. Exit Messenger")

            mes_choice = input("Choose an option: ")

            if mes_choice == "1":
                receiver = input("To: ")
                message = input("Message: ")

                print("\n📤 Sending message...")
                time.sleep(3.0)
                print(f"✅ Message sent to {receiver}!\n")

                # You can store it in a list to "view sent messages" later
                sent_messages.append((receiver, message))

            elif mes_choice == "2":
                if not sent_messages:
                    print("\n📭 No sent messages yet.")
                else:
                    print("\n--- Sent Messages ---")
                    for i, (to, msg) in enumerate(sent_messages, start=1):
                        print(f"{i}. To: {to} | Message: {msg}")
                input("Press Enter to return...")

            elif mes_choice == "3":
                print("-----Hi. Welcome to XONO Post-----")
                name = input("Enter your name: ")
                age = input("Enter your date of birth: ")
                phone = input("Enter your phone number: ")
                country = input("Enter your country: ")

                print("Account created successfully!")
                print("-------------------------------------")
                print(f"Your post account is {name}@XONO.com")
                time.sleep(1.0)

            elif mes_choice == "4":
                print("👋 Exiting XONO Post... See you next time!")
                time.sleep(1.0)
                break

            else:
                print("❌ Invalid choice. Try again.")

    #Command Prompt
    def terminal():

        while True:
            print("Type /exit to exit the Command Prompt")
            comm = str(input("Enter the command: "))

            if comm == "/keys":
                print("Note: You should add a '/' mark in all the commands before typing.")

                print("Press R to refresh when in the desktop.")
                print("Type: /file viewer to open File Viewer.")
                print("Type: /calculator to open Calculator.")
                print("Type: /notepad to open Notepad.")
                print("Type: /settings to open Settings.")
                print("Type: /about xono to open About your PC.")
                print("Type: /xono post to open XONO Post.")
                print("Type: /xono store to open XONO Store.")
                print("Type: run in desktop to open run.")

                print("Note: You should type commands only in simple form!")
                print("Note: You should type the spellings correctly!")

            elif comm == "/file viewer":
                time.sleep(0.7)
                file_viewer()

            elif comm == "/calculator":
                time.sleep(0.7)
                calculator()

            elif comm == "/notepad":
                time.sleep(0.7)
                notepad()

            elif comm == "/settings":
                time.sleep(0.7)
                settings()

            elif comm == "/about xono":
                time.sleep(0.7)
                about_xono()

            elif comm == "/xono post":
                time.sleep(0.7)
                xono_post()

            elif comm == "/xono store":
                time.sleep(0.7)
                xono_store()

            elif comm == "/exit":
                print("Exiting Command Prompt.")
                time.sleep(0.7)
                break

            else:
                print("Invalid choice. Try again.")
    
    def xono_writer():
        os.makedirs(XONO_WRITER, exist_ok=True)
        while True:
            print("\n--- XONO Writer ---")
            print("1. Create New Document")
            print("2. View/Edit Existing Document")
            print("3. Return to XONO Office")

            choice = input("Enter your choice: ")

            if choice == "1":
                existing_docs = [f for f in os.listdir(XONO_WRITER) if f.endswith(".xdoc")]
                doc_number = len(existing_docs) + 1
                doc_name = f"document{doc_number}.xdoc"
                doc_path = os.path.join(XONO_WRITER, doc_name)

                print(f"\nCreating {doc_name}")
                print("Type text below. Type 'SAVE' to save.")
                print("Formatting: **bold**, __underline__, ~~italic~~\n")

                lines = []
                while True:
                    line = input()
                    if line.upper() == "SAVE":
                        break
                    line = line.replace("**", "[BOLD]").replace("__", "[UNDERLINE]").replace("~~", "[ITALIC]")
                    lines.append(line)

                with open(doc_path, "w", encoding="utf-8") as f:
                    f.write("\n".join(lines))
                print(f"✅ Saved as {doc_name} in xonowriter folder!")

            elif choice == "2":
                docs = [f for f in os.listdir(XONO_WRITER) if f.endswith(".xdoc")]
                if not docs:
                    print("No XONO Writer documents found!")
                    continue

                print("\n--- Existing Documents ---")
                for i, doc in enumerate(docs, start=1):
                    print(f"{i}. {doc}")
                print(f"{len(docs)+1}. Return")

                select = input("Enter document number: ")
                if not select.isdigit():
                    print("❌ Invalid input.")
                    continue
                num = int(select)
                if 1 <= num <= len(docs):
                    filename = docs[num - 1]
                    path = os.path.join(XONO_WRITER, filename)

                    with open(path, "r", encoding="utf-8") as f:
                        print("\n--- Document Content ---")
                        print(f.read())
                        print("-----------------------")

                    edit = input("Edit this document? (y/n): ").lower()
                    if edit == "y":
                        print("Type new content. Type 'SAVE' to save.")
                        new_lines = []
                        while True:
                            line = input()
                            if line.upper() == "SAVE":
                                break
                            line = line.replace("**", "[BOLD]").replace("__", "[UNDERLINE]").replace("~~", "[ITALIC]")
                            new_lines.append(line)
                        with open(path, "w", encoding="utf-8") as f:
                            f.write("\n".join(new_lines))
                        print(f"✅ Changes saved to {filename}!")

            elif choice == "3":
                print("Returning to XONO Office...")
                break
            else:
                print("❌ Invalid input.")

    
    def office():
        while True:
            print("\n--- XONO Office ---")
            print("1. XONO Writer")
            print("2. Return to Desktop")

            choice = input("Choose: ")
            if choice == "1":
                xono_writer()
            elif choice == "2":
                break
            else:
                print("❌ Invalid option.")


    if choice == "1":
        print(f"Opening app {choice}...")
        time.sleep(0.7)
        file_viewer()

    elif choice == "2":
        print(f"Opening app {choice}...")
        time.sleep(0.7)
        calculator()

    elif choice == "3":
        print(f"Opening app {choice}...")
        time.sleep(0.7)
        notepad()
    
    elif choice == "4":
        print(f"Opening app {choice}...")
        time.sleep(0.7)
        settings()

    elif choice == "5":
        print(f"Opening app {choice}...")
        time.sleep(0.7)
        about_xono()

    elif choice == "6":
        print(f"Opening app {choice}...")
        time.sleep(1.0)
        xono_post()

    elif choice == "7":
        print(f"Opening app {choice}...")
        time.sleep(1.0)
        xono_store()

    elif choice == "8":
        print(f"Opening app {choice}...")
        time.sleep(1.0)
        terminal()

    elif choice == "9":
        print(f"Opening app {choice}...")
        time.sleep(0.7)
        recycle_bin()

    elif choice == "10":
        print(f"Opening app {choice}...")
        time .sleep(0.7)
        office()

    elif choice == "11":
        print("Shutting down XONO OS... 📴")
        time.sleep(0.7)
        user_quit = "quit"

    
    elif choice == "r":
        print("Refreshing the OS!")
        print("✓ File Viewer")
        time.sleep(0.7)
        print("✓ Calculator")
        time.sleep(0.7)
        print("✓ Notepad")
        time.sleep(0.7)
        print("✓ Settings")
        time.sleep(0.7)
        print("✓ About your PC")
        time.sleep(0.7)
        print("✓ XONO Post")
        time.sleep(0.7)
        print("✓ XONO Store")
        time.sleep(0.7)
        print("✓ Command Prompt")
        time.sleep(0.7)
        print("✓ Recycle Bin")
        time.sleep(0.7)
        print("✓ XONO Office")
        time.sleep(0.7)

    elif choice == "run":
        while True:
            print("-----Run-----")
            run = str(input("Open: "))

            if run == "junk":
                delete = str(input("Are you sure to delete junk files? (yes/no)"))
                if delete == "yes":
                    time.sleep(1.0)
                    print("Junk files are successfully deleted!")
                    break
                elif delete == "no":
                    break
                else:
                    print("Invalid option. Try again.")
    else:
        print("Invalid choice. Try again.")
