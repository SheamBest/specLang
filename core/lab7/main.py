from .API.api import APIClient, prompt_for_endpoint, safe_api_request, display_data, save_data
from .history.history import CalculationHistory

def main():
    api_client = APIClient('https://jsonplaceholder.typicode.com')
    history = CalculationHistory()
    while True:
        endpoint = prompt_for_endpoint()
        if endpoint.lower() == 'exit':
            break

        data = safe_api_request(api_client.get, f'/{endpoint}')
        if data:
            display_data(data)
            history.add(data)


            if input("Would you like to save the data? (yes/no): ").lower() == 'yes':
                format = input("Which format would you like to use? (json/csv): ").lower()
                save_data(data, format)

if __name__ == '__main__':
    main()