from authentication.login import login


success = login()


if success:
    print("Assistant can start")
else:
    print("Access denied")