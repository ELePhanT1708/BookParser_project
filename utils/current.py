import requests
def main():
    s1 = 'https://www.roslit.ru/catalog/901/65663234/'
    print(requests.get(s1).status_code)

if __name__=='__main__':
    main()

