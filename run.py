from dummyapp import app_obj


def main():
    app_obj.run(debug=True, host="0.0.0.0")


if __name__ == "__main__":
    main()
