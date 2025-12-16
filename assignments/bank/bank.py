greeting = input("Greeting: ").strip();

if greeting.lower().startswith("hello"):
    print(f"${0}");
elif greeting.lower().startswith("h"):
    print(f"${20}");
else:
    print(f"${100}");