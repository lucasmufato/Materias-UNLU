from SE.QueryProcessingCoordinator import QueryProcessingCoordinator


class QueryInterface:

    def __init__(self, query_processor: QueryProcessingCoordinator) -> None:
        super().__init__()
        self.queryProcessor = query_processor

    def main_menu_loop(self):
        self.explicar_menu()
        query = self.pedir_query()
        while query != "/q":
            results = self.queryProcessor.process(query)
            self.show_query_results(results)
            self.print_space_between_result_and_new_query()
            query = self.pedir_query()
        self.print_end()

    def explicar_menu(self):
        print("--- Menu de querys --- \r \r")
        print("--- Ingrese en el input la query a realizar y aprete enter ---")
        print("--- Para salir ingrese: /q ---")

    def pedir_query(self) -> str:
        return input("query: ")

    def show_query_results(self, results):
        print(" \r Resultados del query: \r")
        for r in results:
            print(str(r))

    def print_space_between_result_and_new_query(self):
        print("\r \r")

    def print_end(self):
        print("Saliendo de interfaz de consulta")
