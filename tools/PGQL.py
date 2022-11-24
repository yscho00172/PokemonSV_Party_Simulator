import psycopg2

class PGQL:
    def __init__(self, host, port, dbname, user, password):
        self.conn = psycopg2.connect(host=host, port=port, dbname=dbname, user=user, password=password)
        self.cur = self.conn.cursor()

    def query(self, execute_query):
        self.cur.execute(execute_query)
        self.conn.commit()

    def fetch(self):
        return self.cur.fetchall()

    def close(self):
        self.cur.close()
        self.conn.close()

def insert_pokemon(pgql):
    with open("PokeDex.txt", "r") as pokemon_file:
        for types in pokemon_file:
            _type = types.strip()
            _type12 = _type.split('  ')
            if(len(_type12) > 2):
                insert_types = [_type12[0], _type12[1], _type12[2]]
            else:
                insert_types = [_type12[0], _type12[1], 'None']
            pgql.query("INSERT INTO \"Pokemon_compare_pokemon_dictionary\" (\"Type1\", \"Type2\") VALUES ('%s', '%s')" % (insert_types[1], insert_types[2]))

def insert_compare(pgql):
    with open("Type_Compatibility.txt", "r") as compare_file:
        for types in compare_file:
            _type = types.strip()
            _compare_types = _type.split(':')
            target_type = _compare_types[0]
            opposite_types = _compare_types[1].split(',')
            for opposite_type in opposite_types:
                pgql.query("INSERT INTO \"Pokemon_compare_type_compatibility\" (\"Type\", \"Opposite\") VALUES ('%s', '%s')" % (target_type, opposite_type))

if __name__ == '__main__':
    pgql = PGQL('127.0.0.1', 5432, 'pokemon', 'postgres', 'postgres')

    insert_pokemon(pgql)
    insert_compare(pgql)

    pgql.close()