from app import create_app

if __name__ == "__main__":
    print("__main__.py running")
    app = create_app()
    app.run(8000)