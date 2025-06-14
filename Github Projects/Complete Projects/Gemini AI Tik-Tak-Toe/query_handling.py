def load_queries(file_path):
    with open(file_path, "r") as file:
        content = file.read().split("-- name:")
        queries = {}
        for each in content:
            if each.strip(): 
                name, sql = each.strip().split("\n", 1) 
                queries[name.strip()] = sql.strip()
        return queries
    
def initiate_query_runner():
    queries = load_queries(r"D:\College\Programming Files\Codes\Projects\Github Projects\Complete Projects\Gemini AI Tik-Tak-Toe\queries.sql")
    return queries
