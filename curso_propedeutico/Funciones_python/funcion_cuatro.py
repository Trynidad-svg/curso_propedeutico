def main():
    c=0
    while True:
        try:
            s=input("Ingrese una palabra o número: ")
            if not s.strip(): break
            if s.isdigit(): s=str(s)
            print(s.upper()); c+=1
        except Exception as e: print("Error:", e)
    print("Palabras procesadas:", c)
main()
 