inp = input("Filename: ").strip().lower()

if inp.endswith(".jpg"):
    print("image/jpg")
elif inp.endswith("jpeg"):
    print("image/jpeg")
elif inp.endswith(".png"):
    print("image/png")
elif inp.endswith(".gif"):
    print("image/gif")
elif inp.endswith(".pdf"):
    print("application/pdf")
elif inp.endswith(".txt"):
    print("application/txt")
else:
    print("application/octet-stream")

