from dummyapp import create_app


def main():
    app_obj = create_app("development")
    app_obj.run(debug=True, host="0.0.0.0")


if __name__ == "__main__":
    main()
