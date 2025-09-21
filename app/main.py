import snowflake.connector
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Get credentials from .env
USER = os.getenv('SNOWFLAKE_USER')
PASSWORD = os.getenv('SNOWFLAKE_PASSWORD')
ACCOUNT = os.getenv('SNOWFLAKE_ACCOUNT')

# SQL file name
SQL_FILE_CREATE = "app/commands_create_structure.sql"
SQL_FILE_DROP = "app/commands_drop_structure.sql"

def create_structure():
    # Connect to Snowflake
    try:
        conn = snowflake.connector.connect(
            user=USER,
            password=PASSWORD,
            account=ACCOUNT
        )
    except Exception as e:
        print(f"Connection error: {e}")
        print("Check your credentials in .env file")
        exit()

    cursor = conn.cursor()

    # Read and execute SQL file
    try:
        with open(SQL_FILE_CREATE, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Split commands by semicolon
        commands = [cmd.strip() for cmd in content.split(';') if cmd.strip()]
        
        print(f"Executing {len(commands)} commands from {SQL_FILE_CREATE}...")
        
        for i, command in enumerate(commands, 1):
            print(f"[{i}] Executing...")
            cursor.execute(command)
            print("✓ OK")
            
        print("All commands executed successfully!")
        
    except FileNotFoundError:
        print(f"File {SQL_FILE_CREATE} not found!")
    except Exception as e:
        print(f"Error: {e}")

    cursor.close()
    conn.close()


def drop_structure():
    # Connect to Snowflake
    try:
        conn = snowflake.connector.connect(
            user=USER,
            password=PASSWORD,
            account=ACCOUNT
        )
    except Exception as e:
        print(f"Connection error: {e}")
        print("Check your credentials in .env file")
        exit()

    cursor = conn.cursor()

    # Read and execute SQL file
    try:
        with open(SQL_FILE_DROP, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Split commands by semicolon
        commands = [cmd.strip() for cmd in content.split(';') if cmd.strip()]
        
        print(f"Executing {len(commands)} cleanup commands from {SQL_FILE_DROP}...")
        
        for i, command in enumerate(commands, 1):
            try:
                print(f"[{i}] Executing...")
                cursor.execute(command)
                print("✓ OK")
            except Exception as e:
                print(f"✗ Error: {e}")
                # Continue with other commands even if one fails
                continue
            
        print("Cleanup completed!")
        
    except FileNotFoundError:
        print(f"File {SQL_FILE_DROP} not found!")
    except Exception as e:
        print(f"Error: {e}")

    cursor.close()
    conn.close()